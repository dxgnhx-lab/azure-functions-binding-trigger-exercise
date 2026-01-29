"""
CERT 내부자 위협 데이터 분석 스크립트

이 스크립트는 CERT (Computer Emergency Response Team) 내부자 위협 데이터를 분석합니다.
answers 폴더의 정답 데이터를 활용하여 위협을 탐지하고 분석합니다.
"""

import json
import csv
import os
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import statistics

class CERTInsiderThreatAnalyzer:
    """CERT 내부자 위협 분석 클래스"""
    
    def __init__(self, answers_folder="answers"):
        """
        초기화 함수
        
        Args:
            answers_folder: 정답 데이터가 있는 폴더 경로
        """
        self.answers_folder = answers_folder
        self.threat_indicators = None
        self.known_threats = []
        self.analysis_params = None
        
        # 정답 데이터 로드
        self.load_answer_data()
    
    def load_answer_data(self):
        """answers 폴더에서 정답 데이터를 로드합니다."""
        # threat_indicators.json 로드
        indicators_path = os.path.join(self.answers_folder, "threat_indicators.json")
        if os.path.exists(indicators_path):
            with open(indicators_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.threat_indicators = data.get('high_risk_indicators', {})
                self.threat_scenarios = data.get('threat_scenarios', {})
                self.analysis_params = data.get('analysis_parameters', {})
            print(f"✓ 위협 지표 데이터 로드 완료: {indicators_path}")
        else:
            print(f"⚠ 위협 지표 파일을 찾을 수 없습니다: {indicators_path}")
        
        # known_threats.csv 로드
        threats_path = os.path.join(self.answers_folder, "known_threats.csv")
        if os.path.exists(threats_path):
            with open(threats_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.known_threats = list(reader)
            print(f"✓ 알려진 위협 데이터 로드 완료: {threats_path} ({len(self.known_threats)} 건)")
        else:
            print(f"⚠ 알려진 위협 파일을 찾을 수 없습니다: {threats_path}")
    
    def analyze_user_behavior(self, user_data):
        """
        사용자 행동 데이터를 분석하여 위협 점수를 계산합니다.
        
        Args:
            user_data: 사용자 행동 데이터 딕셔너리
                {
                    'user_id': 'USR001',
                    'daily_file_access': 1200,
                    'unique_files': 600,
                    'sensitive_files': 55,
                    'external_emails': 120,
                    'email_attachment_size_mb': 150,
                    'off_hours_logins': 15,
                    'failed_logins': 25,
                    'data_transfer_gb': 60,
                    'external_connections': 250
                }
        
        Returns:
            dict: 위협 분석 결과
        """
        risk_scores = {}
        alerts = []
        
        # 파일 접근 패턴 분석
        file_indicators = self.threat_indicators.get('file_access', {})
        file_score = 0
        if user_data.get('daily_file_access', 0) > file_indicators.get('threshold_daily_access', 1000):
            file_score += 0.4
            alerts.append(f"일일 파일 접근 횟수 초과: {user_data.get('daily_file_access')} > {file_indicators.get('threshold_daily_access')}")
        
        if user_data.get('unique_files', 0) > file_indicators.get('threshold_unique_files', 500):
            file_score += 0.3
            alerts.append(f"고유 파일 접근 수 초과: {user_data.get('unique_files')} > {file_indicators.get('threshold_unique_files')}")
        
        if user_data.get('sensitive_files', 0) > file_indicators.get('threshold_sensitive_files', 50):
            file_score += 0.3
            alerts.append(f"민감한 파일 접근 초과: {user_data.get('sensitive_files')} > {file_indicators.get('threshold_sensitive_files')}")
        
        risk_scores['file_access'] = file_score
        
        # 이메일 패턴 분석
        email_indicators = self.threat_indicators.get('email_patterns', {})
        email_score = 0
        if user_data.get('external_emails', 0) > email_indicators.get('external_recipients_threshold', 100):
            email_score += 0.5
            alerts.append(f"외부 이메일 수신자 수 초과: {user_data.get('external_emails')} > {email_indicators.get('external_recipients_threshold')}")
        
        if user_data.get('email_attachment_size_mb', 0) > email_indicators.get('attachment_size_threshold_mb', 100):
            email_score += 0.5
            alerts.append(f"이메일 첨부파일 크기 초과: {user_data.get('email_attachment_size_mb')}MB > {email_indicators.get('attachment_size_threshold_mb')}MB")
        
        risk_scores['email_activity'] = email_score
        
        # 로그인 패턴 분석
        login_indicators = self.threat_indicators.get('login_patterns', {})
        login_score = 0
        if user_data.get('off_hours_logins', 0) > login_indicators.get('off_hours_login_threshold', 10):
            login_score += 0.5
            alerts.append(f"업무 외 시간 로그인 초과: {user_data.get('off_hours_logins')} > {login_indicators.get('off_hours_login_threshold')}")
        
        if user_data.get('failed_logins', 0) > login_indicators.get('failed_login_threshold', 20):
            login_score += 0.5
            alerts.append(f"로그인 실패 횟수 초과: {user_data.get('failed_logins')} > {login_indicators.get('failed_login_threshold')}")
        
        risk_scores['login_behavior'] = login_score
        
        # 네트워크 활동 분석
        network_indicators = self.threat_indicators.get('network_activity', {})
        network_score = 0
        if user_data.get('data_transfer_gb', 0) > network_indicators.get('data_transfer_threshold_gb', 50):
            network_score += 0.6
            alerts.append(f"데이터 전송량 초과: {user_data.get('data_transfer_gb')}GB > {network_indicators.get('data_transfer_threshold_gb')}GB")
        
        if user_data.get('external_connections', 0) > network_indicators.get('external_connection_threshold', 200):
            network_score += 0.4
            alerts.append(f"외부 연결 횟수 초과: {user_data.get('external_connections')} > {network_indicators.get('external_connection_threshold')}")
        
        risk_scores['network_activity'] = network_score
        
        # 전체 위험 점수 계산 (가중 평균)
        weights = self.analysis_params.get('risk_score_weights', {
            'file_access': 0.3,
            'email_activity': 0.25,
            'login_behavior': 0.25,
            'network_activity': 0.2
        })
        
        total_risk_score = sum(risk_scores.get(key, 0) * weight 
                              for key, weight in weights.items())
        
        # 위협 분류
        threat_level = self._classify_threat_level(total_risk_score)
        potential_threats = self._identify_potential_threats(risk_scores, alerts)
        
        return {
            'user_id': user_data.get('user_id'),
            'risk_scores': risk_scores,
            'total_risk_score': round(total_risk_score, 3),
            'threat_level': threat_level,
            'alerts': alerts,
            'potential_threats': potential_threats,
            'timestamp': datetime.now().isoformat()
        }
    
    def _classify_threat_level(self, score):
        """위험 점수를 기반으로 위협 수준을 분류합니다."""
        if score >= 0.7:
            return "CRITICAL"
        elif score >= 0.5:
            return "HIGH"
        elif score >= 0.3:
            return "MEDIUM"
        elif score > 0:
            return "LOW"
        else:
            return "NORMAL"
    
    def _identify_potential_threats(self, risk_scores, alerts):
        """위험 점수와 알림을 기반으로 잠재적 위협 유형을 식별합니다."""
        potential = []
        
        # 데이터 유출 가능성
        if risk_scores.get('file_access', 0) > 0.5 and risk_scores.get('email_activity', 0) > 0.3:
            potential.append({
                'type': 'data_exfiltration',
                'confidence': 'high',
                'scenario': self.threat_scenarios.get('data_exfiltration', {})
            })
        
        # 자격 증명 도용 가능성
        if risk_scores.get('login_behavior', 0) > 0.6:
            potential.append({
                'type': 'credential_theft',
                'confidence': 'medium',
                'scenario': self.threat_scenarios.get('credential_theft', {})
            })
        
        # 시스템 파괴 가능성
        if risk_scores.get('file_access', 0) > 0.6 and any('민감한 파일' in alert for alert in alerts):
            potential.append({
                'type': 'sabotage',
                'confidence': 'medium',
                'scenario': self.threat_scenarios.get('sabotage', {})
            })
        
        return potential
    
    def analyze_historical_threats(self):
        """과거 위협 데이터를 분석하여 통계를 생성합니다."""
        if not self.known_threats:
            print("⚠ 분석할 과거 위협 데이터가 없습니다.")
            return None
        
        # 위협 유형별 통계
        threat_types = Counter(threat['threat_type'] for threat in self.known_threats)
        
        # 심각도별 통계
        severity_stats = Counter(threat['severity'] for threat in self.known_threats)
        
        # 해결 상태 통계
        resolution_stats = Counter(threat['resolved'] for threat in self.known_threats)
        
        # 월별 위협 발생 추이
        monthly_threats = defaultdict(int)
        for threat in self.known_threats:
            date = datetime.strptime(threat['detection_date'], '%Y-%m-%d')
            month_key = date.strftime('%Y-%m')
            monthly_threats[month_key] += 1
        
        analysis = {
            'total_threats': len(self.known_threats),
            'threat_type_distribution': dict(threat_types),
            'severity_distribution': dict(severity_stats),
            'resolution_status': dict(resolution_stats),
            'monthly_trend': dict(sorted(monthly_threats.items())),
            'most_common_threat': threat_types.most_common(1)[0] if threat_types else None,
            'resolution_rate': f"{(list(resolution_stats.values())[0] / len(self.known_threats) * 100):.1f}%" if resolution_stats else "N/A"
        }
        
        return analysis
    
    def generate_report(self, user_analysis_results, historical_analysis):
        """분석 결과를 종합하여 보고서를 생성합니다."""
        print("\n" + "="*80)
        print("CERT 내부자 위협 분석 보고서")
        print("="*80)
        print(f"생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)
        
        # 과거 위협 통계
        if historical_analysis:
            print("\n[과거 위협 통계]")
            print(f"총 탐지된 위협: {historical_analysis['total_threats']}건")
            print(f"가장 흔한 위협 유형: {historical_analysis['most_common_threat']}")
            print(f"해결률: {historical_analysis['resolution_rate']}")
            
            print("\n위협 유형별 분포:")
            for threat_type, count in historical_analysis['threat_type_distribution'].items():
                print(f"  - {threat_type}: {count}건")
            
            print("\n심각도별 분포:")
            for severity, count in historical_analysis['severity_distribution'].items():
                print(f"  - {severity}: {count}건")
        
        # 사용자 분석 결과
        if user_analysis_results:
            print("\n" + "-"*80)
            print("[사용자 행동 분석 결과]")
            print("-"*80)
            
            for result in user_analysis_results:
                print(f"\n사용자 ID: {result['user_id']}")
                print(f"전체 위험 점수: {result['total_risk_score']} ({result['threat_level']})")
                print(f"세부 위험 점수:")
                for category, score in result['risk_scores'].items():
                    print(f"  - {category}: {score:.3f}")
                
                if result['alerts']:
                    print(f"\n발생한 알림 ({len(result['alerts'])}건):")
                    for alert in result['alerts']:
                        print(f"  ⚠ {alert}")
                
                if result['potential_threats']:
                    print(f"\n잠재적 위협 ({len(result['potential_threats'])}건):")
                    for threat in result['potential_threats']:
                        scenario = threat['scenario']
                        print(f"  🔴 유형: {threat['type']} (신뢰도: {threat['confidence']})")
                        print(f"     심각도: {scenario.get('severity', 'N/A')}")
                        print(f"     권장 조치: {', '.join(scenario.get('recommended_actions', []))}")
        
        print("\n" + "="*80)
        print("보고서 끝")
        print("="*80 + "\n")


def main():
    """메인 함수 - 샘플 데이터로 분석을 실행합니다."""
    print("CERT 내부자 위협 분석 시스템 시작...\n")
    
    # 분석기 초기화
    analyzer = CERTInsiderThreatAnalyzer(answers_folder="answers")
    
    # 샘플 사용자 데이터 (실제 환경에서는 DB나 로그에서 가져옴)
    sample_users = [
        {
            'user_id': 'USR999',
            'daily_file_access': 1200,
            'unique_files': 600,
            'sensitive_files': 55,
            'external_emails': 120,
            'email_attachment_size_mb': 150,
            'off_hours_logins': 15,
            'failed_logins': 25,
            'data_transfer_gb': 60,
            'external_connections': 250
        },
        {
            'user_id': 'USR888',
            'daily_file_access': 500,
            'unique_files': 200,
            'sensitive_files': 10,
            'external_emails': 30,
            'email_attachment_size_mb': 20,
            'off_hours_logins': 2,
            'failed_logins': 3,
            'data_transfer_gb': 5,
            'external_connections': 50
        },
        {
            'user_id': 'USR777',
            'daily_file_access': 2000,
            'unique_files': 800,
            'sensitive_files': 100,
            'external_emails': 200,
            'email_attachment_size_mb': 300,
            'off_hours_logins': 30,
            'failed_logins': 50,
            'data_transfer_gb': 100,
            'external_connections': 400
        }
    ]
    
    # 각 사용자에 대해 분석 수행
    user_results = []
    for user_data in sample_users:
        result = analyzer.analyze_user_behavior(user_data)
        user_results.append(result)
    
    # 과거 위협 분석
    historical_analysis = analyzer.analyze_historical_threats()
    
    # 종합 보고서 생성
    analyzer.generate_report(user_results, historical_analysis)
    
    # JSON 형식으로도 결과 저장 가능
    output_file = "cert_analysis_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'user_analysis': user_results,
            'historical_analysis': historical_analysis
        }, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 분석 결과가 {output_file}에 저장되었습니다.\n")


if __name__ == "__main__":
    main()
