# CERT 내부자 위협 분석 - 사용 가이드

## 📌 개요

이 프로젝트는 CERT (Computer Emergency Response Team) 내부자 위협 데이터를 분석하기 위한 완전한 솔루션을 제공합니다. 
`answers` 폴더의 정답 데이터를 활용하여 실제 조직의 보안 위협을 탐지하고 분석할 수 있습니다.

## 🎯 주요 특징

### 1. answers 폴더 포함
프로젝트는 정답 데이터가 포함된 `answers` 폴더를 제공합니다:
- **threat_indicators.json**: 위협 탐지를 위한 지표와 임계값
- **known_threats.csv**: 과거에 탐지된 실제 위협 사례 10건
- **README.md**: 정답 데이터에 대한 상세 설명

### 2. 종합 분석 도구
두 가지 방식으로 분석을 수행할 수 있습니다:
- **cert_analysis.py**: 커맨드라인 실행 가능한 Python 스크립트
- **cert_analysis.ipynb**: 대화형 Jupyter Notebook

### 3. 4가지 차원의 위협 분석
- 파일 접근 패턴 분석
- 이메일 활동 분석
- 로그인 행동 분석
- 네트워크 활동 분석

## 🚀 빠른 시작

### 1단계: 의존성 설치
```bash
pip install -r requirements.txt
```

### 2단계: Python 스크립트 실행
```bash
python cert_analysis.py
```

출력 예시:
```
CERT 내부자 위협 분석 시스템 시작...

✓ 위협 지표 데이터 로드 완료: answers/threat_indicators.json
✓ 알려진 위협 데이터 로드 완료: answers/known_threats.csv (10 건)

================================================================================
CERT 내부자 위협 분석 보고서
================================================================================
생성 시각: 2024-01-29 15:30:00
================================================================================

[과거 위협 통계]
총 탐지된 위협: 10건
가장 흔한 위협 유형: ('data_exfiltration', 3)
해결률: 80.0%
...
```

### 3단계: Jupyter Notebook으로 상세 분석
```bash
jupyter notebook cert_analysis.ipynb
```

## 📊 제공되는 분석 기능

### 1. 과거 위협 데이터 분석
`answers/known_threats.csv`에서 로드한 10건의 실제 위협 사례를 분석합니다:

```python
from cert_analysis import CERTInsiderThreatAnalyzer

analyzer = CERTInsiderThreatAnalyzer(answers_folder="answers")
historical_analysis = analyzer.analyze_historical_threats()

print(f"총 위협: {historical_analysis['total_threats']}")
print(f"가장 흔한 위협: {historical_analysis['most_common_threat']}")
print(f"해결률: {historical_analysis['resolution_rate']}")
```

출력:
- 위협 유형별 분포 (data_exfiltration, credential_theft, sabotage 등)
- 심각도별 분포 (critical, high, medium, low)
- 월별 위협 발생 추이
- 해결 상태 통계

### 2. 사용자 행동 분석
사용자의 행동 패턴을 분석하여 위협 점수를 계산합니다:

```python
user_data = {
    'user_id': 'USR001',
    'daily_file_access': 1200,        # 일일 파일 접근 횟수
    'unique_files': 600,              # 접근한 고유 파일 수
    'sensitive_files': 55,            # 민감한 파일 접근 횟수
    'external_emails': 120,           # 외부 이메일 발송 수
    'email_attachment_size_mb': 150,  # 이메일 첨부 파일 크기(MB)
    'off_hours_logins': 15,           # 업무 외 시간 로그인
    'failed_logins': 25,              # 로그인 실패 횟수
    'data_transfer_gb': 60,           # 데이터 전송량(GB)
    'external_connections': 250       # 외부 연결 횟수
}

result = analyzer.analyze_user_behavior(user_data)
```

반환되는 결과:
```python
{
    'user_id': 'USR001',
    'risk_scores': {
        'file_access': 1.0,
        'email_activity': 1.0,
        'login_behavior': 1.0,
        'network_activity': 1.0
    },
    'total_risk_score': 1.0,
    'threat_level': 'CRITICAL',
    'alerts': [
        '일일 파일 접근 횟수 초과: 1200 > 1000',
        '외부 이메일 수신자 수 초과: 120 > 100',
        ...
    ],
    'potential_threats': [
        {
            'type': 'data_exfiltration',
            'confidence': 'high',
            'scenario': {
                'severity': 'critical',
                'recommended_actions': [
                    'Immediate investigation',
                    'Disable account',
                    'Review access logs'
                ]
            }
        }
    ]
}
```

### 3. 위협 지표 기반 탐지
`answers/threat_indicators.json`에 정의된 임계값을 사용하여 위협을 탐지합니다:

**파일 접근 지표:**
- 일일 파일 접근 임계값: 1,000건
- 고유 파일 접근 임계값: 500개
- 민감한 파일 접근 임계값: 50개

**이메일 패턴 지표:**
- 외부 수신자 임계값: 100명
- 첨부파일 크기 임계값: 100MB
- 의심 키워드: confidential, secret, password, credentials

**로그인 패턴 지표:**
- 업무 외 로그인 임계값: 10회
- 로그인 실패 임계값: 20회
- 다중 위치 접속 임계값: 5곳

**네트워크 활동 지표:**
- 데이터 전송 임계값: 50GB
- 외부 연결 임계값: 200회
- 의심 포트: 22, 23, 3389

## 📈 분석 결과 예시

### 실행 시 생성되는 파일

1. **cert_analysis_results.json** - 전체 분석 결과 (JSON 형식)
2. **cert_analysis_results.csv** - 사용자별 요약 (CSV 형식) [Notebook 실행 시]
3. **cert_threat_analysis.png** - 과거 위협 통계 시각화 [Notebook 실행 시]
4. **user_risk_analysis.png** - 사용자별 위험 점수 시각화 [Notebook 실행 시]

### 콘솔 출력 예시

```
================================================================================
CERT 내부자 위협 분석 보고서
================================================================================

[과거 위협 통계]
총 탐지된 위협: 10건
가장 흔한 위협 유형: ('data_exfiltration', 3)
해결률: 80.0%

위협 유형별 분포:
  - data_exfiltration: 3건
  - credential_theft: 2건
  - sabotage: 2건
  - insider_trading: 1건
  - intellectual_property_theft: 1건
  - policy_violation: 1건

심각도별 분포:
  - critical: 4건
  - high: 3건
  - medium: 2건
  - low: 1건

--------------------------------------------------------------------------------
[사용자 행동 분석 결과]
--------------------------------------------------------------------------------

사용자 ID: USR999
전체 위험 점수: 1.0 (CRITICAL)
세부 위험 점수:
  - file_access: 1.000
  - email_activity: 1.000
  - login_behavior: 1.000
  - network_activity: 1.000

발생한 알림 (9건):
  ⚠ 일일 파일 접근 횟수 초과: 1200 > 1000
  ⚠ 고유 파일 접근 수 초과: 600 > 500
  ⚠ 민감한 파일 접근 초과: 55 > 50
  ⚠ 외부 이메일 수신자 수 초과: 120 > 100
  ⚠ 이메일 첨부파일 크기 초과: 150MB > 100MB
  ⚠ 업무 외 시간 로그인 초과: 15 > 10
  ⚠ 로그인 실패 횟수 초과: 25 > 20
  ⚠ 데이터 전송량 초과: 60GB > 50GB
  ⚠ 외부 연결 횟수 초과: 250 > 200

잠재적 위협 (3건):
  🔴 유형: data_exfiltration (신뢰도: high)
     심각도: critical
     권장 조치: Immediate investigation, Disable account, Review access logs
  🔴 유형: credential_theft (신뢰도: medium)
     심각도: high
     권장 조치: Force password reset, Review account activity, Check for lateral movement
  🔴 유형: sabotage (신뢰도: medium)
     심각도: critical
     권장 조치: Immediate isolation, Backup verification, Forensic analysis
```

## 💡 사용 시나리오

### 시나리오 1: 정기 보안 감사
```python
# 모든 직원의 행동 데이터를 DB에서 가져옴
employees = get_all_employees_from_database()

analyzer = CERTInsiderThreatAnalyzer(answers_folder="answers")
high_risk_users = []

for employee in employees:
    result = analyzer.analyze_user_behavior(employee)
    if result['threat_level'] in ['CRITICAL', 'HIGH']:
        high_risk_users.append(result)

# 고위험 사용자에 대한 보고서 생성
generate_security_report(high_risk_users)
```

### 시나리오 2: 실시간 위협 모니터링
```python
# 실시간으로 사용자 활동 모니터링
def monitor_user_activity(user_id):
    analyzer = CERTInsiderThreatAnalyzer(answers_folder="answers")
    
    while True:
        current_behavior = get_current_user_behavior(user_id)
        result = analyzer.analyze_user_behavior(current_behavior)
        
        if result['threat_level'] == 'CRITICAL':
            send_alert_to_security_team(result)
            log_incident(result)
        
        time.sleep(300)  # 5분마다 체크
```

### 시나리오 3: 과거 데이터 학습 및 패턴 분석
```python
analyzer = CERTInsiderThreatAnalyzer(answers_folder="answers")

# 과거 위협 데이터 분석
historical = analyzer.analyze_historical_threats()

# 가장 흔한 위협 유형 파악
print(f"주요 위협: {historical['most_common_threat']}")
print(f"월별 추이: {historical['monthly_trend']}")

# 이 정보를 바탕으로 임계값 조정
adjust_thresholds_based_on_history(historical)
```

## 🔧 커스터마이징

### 1. 임계값 조정
`answers/threat_indicators.json` 파일을 수정하여 조직에 맞는 임계값을 설정:

```json
{
  "high_risk_indicators": {
    "file_access": {
      "threshold_daily_access": 2000,  // 1000에서 2000으로 변경
      "threshold_unique_files": 1000,  // 500에서 1000으로 변경
      ...
    }
  }
}
```

### 2. 새로운 위협 시나리오 추가
```json
{
  "threat_scenarios": {
    "data_exfiltration": { ... },
    "new_threat_type": {
      "indicators": ["custom_indicator_1", "custom_indicator_2"],
      "severity": "high",
      "recommended_actions": ["Action 1", "Action 2"]
    }
  }
}
```

### 3. 가중치 조정
분석 파라미터의 가중치를 조정하여 특정 카테고리를 더 중요하게 평가:

```json
{
  "analysis_parameters": {
    "risk_score_weights": {
      "file_access": 0.4,        // 30%에서 40%로 증가
      "email_activity": 0.3,     // 25%에서 30%로 증가
      "login_behavior": 0.2,     // 25%에서 20%로 감소
      "network_activity": 0.1    // 20%에서 10%로 감소
    }
  }
}
```

## 📚 추가 리소스

- **CERT_ANALYSIS_README.md**: 전체 프로젝트 문서 (영문)
- **answers/README.md**: 정답 데이터 상세 설명
- **cert_analysis.py**: 소스 코드 (주석 포함)
- **cert_analysis.ipynb**: 대화형 분석 노트북

## ❓ FAQ

### Q: answers 폴더는 무엇인가요?
A: 정답 데이터가 포함된 폴더로, 위협 탐지를 위한 지표와 과거 위협 사례가 포함되어 있습니다. 이 데이터를 참조하여 새로운 위협을 탐지합니다.

### Q: 실제 데이터를 사용하려면 어떻게 해야 하나요?
A: `analyze_user_behavior()` 메소드에 실제 사용자 행동 데이터를 전달하면 됩니다. 데이터는 데이터베이스, 로그 파일, API 등에서 가져올 수 있습니다.

### Q: 위협 임계값을 어떻게 결정하나요?
A: 조직의 정상 행동 패턴을 분석하여 적절한 임계값을 설정합니다. `answers/threat_indicators.json`에서 값을 조정할 수 있습니다.

### Q: 결과를 다른 시스템과 통합할 수 있나요?
A: 네, JSON 형식으로 결과가 저장되므로 SIEM, 티켓팅 시스템, 알림 시스템 등과 쉽게 통합할 수 있습니다.

## 🎓 학습 목적

이 코드는 다음을 배우는 데 유용합니다:
1. 내부자 위협 탐지 알고리즘 구현
2. 다차원 위험 점수 계산
3. 과거 데이터 기반 패턴 분석
4. 보안 알림 시스템 설계
5. 위협 인텔리전스 활용

## 📝 라이센스

교육 및 연구 목적으로 자유롭게 사용하실 수 있습니다.
