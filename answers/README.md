# CERT 내부자 위협 분석 정답 데이터

이 폴더에는 CERT 내부자 위협 분석을 위한 참고 데이터와 정답이 포함되어 있습니다.

## 파일 설명

### threat_indicators.json
내부자 위협을 탐지하기 위한 주요 지표와 임계값이 정의되어 있습니다:
- **high_risk_indicators**: 위험 행동 패턴의 임계값
  - file_access: 파일 접근 패턴
  - email_patterns: 이메일 활동 패턴
  - login_patterns: 로그인 행동 패턴
  - network_activity: 네트워크 활동 패턴

- **threat_scenarios**: 위협 시나리오 분류
  - data_exfiltration: 데이터 유출
  - credential_theft: 자격 증명 도용
  - sabotage: 시스템 파괴

- **analysis_parameters**: 분석 파라미터
  - 분석 기간, 이상 탐지 임계값, 위험 점수 가중치 등

### known_threats.csv
과거에 탐지된 실제 위협 사례 데이터:
- user_id: 사용자 ID
- threat_type: 위협 유형
- detection_date: 탐지 날짜
- severity: 심각도
- description: 설명
- resolved: 해결 여부

## 사용 방법

`cert_analysis.py` 스크립트에서 이 데이터를 참조하여 새로운 위협을 탐지하고 분석합니다.
