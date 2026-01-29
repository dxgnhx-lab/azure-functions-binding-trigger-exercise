# CERT 내부자 위협 데이터 분석

이 프로젝트는 CERT (Computer Emergency Response Team) 내부자 위협 데이터를 분석하는 도구를 제공합니다.

## 📋 목차

- [개요](#개요)
- [기능](#기능)
- [설치](#설치)
- [사용 방법](#사용-방법)
- [파일 구조](#파일-구조)
- [분석 결과](#분석-결과)

## 🎯 개요

CERT 내부자 위협 분석 시스템은 조직 내부의 잠재적 위협을 탐지하고 분석하기 위한 도구입니다. 
사용자의 행동 패턴을 모니터링하고 과거 위협 데이터를 활용하여 이상 행위를 식별합니다.

## ✨ 기능

### 1. 다차원 위협 분석
- **파일 접근 패턴 분석**: 일일 파일 접근, 고유 파일 수, 민감한 파일 접근 모니터링
- **이메일 활동 분석**: 외부 수신자, 첨부파일 크기, 의심스러운 키워드 탐지
- **로그인 행동 분석**: 업무 외 시간 로그인, 로그인 실패, 다중 위치 접속 분석
- **네트워크 활동 분석**: 데이터 전송량, 외부 연결, 의심스러운 포트 사용 감지

### 2. 위협 시나리오 분류
- **데이터 유출 (Data Exfiltration)**: 대량의 파일 접근과 외부 전송 패턴 탐지
- **자격 증명 도용 (Credential Theft)**: 비정상적인 로그인 패턴 식별
- **시스템 파괴 (Sabotage)**: 중요 시스템 파일 수정 및 삭제 시도 감지

### 3. 위험 점수 계산
- 4가지 카테고리별 위험 점수 계산
- 가중 평균을 통한 전체 위험 점수 산출
- 5단계 위협 수준 분류 (CRITICAL, HIGH, MEDIUM, LOW, NORMAL)

### 4. 과거 위협 데이터 분석
- 위협 유형별 통계 및 추이 분석
- 심각도 분포 및 해결률 계산
- 월별 위협 발생 패턴 분석

## 🚀 설치

### 사전 요구사항
- Python 3.8 이상
- pip (Python 패키지 관리자)

### 패키지 설치
```bash
pip install -r requirements.txt
```

필요한 패키지:
- `pandas`: 데이터 처리 및 분석
- `numpy`: 수치 계산
- `matplotlib`: 데이터 시각화
- `seaborn`: 고급 시각화

## 📖 사용 방법

### 1. Python 스크립트 실행

```bash
python cert_analysis.py
```

이 스크립트는:
- `answers` 폴더에서 정답 데이터를 로드합니다
- 샘플 사용자 데이터를 분석합니다
- 콘솔에 상세한 분석 보고서를 출력합니다
- 결과를 `cert_analysis_results.json` 파일로 저장합니다

### 2. Jupyter Notebook 사용

```bash
jupyter notebook cert_analysis.ipynb
```

노트북은 다음 섹션으로 구성되어 있습니다:
1. 데이터 로드 및 준비
2. 과거 위협 데이터 분석
3. 사용자 행동 분석
4. 위험 점수 시각화
5. 위협 탐지 및 권장 조치
6. 결과 저장

### 3. 사용자 정의 데이터 분석

Python 코드에서 직접 사용:

```python
from cert_analysis import CERTInsiderThreatAnalyzer

# 분석기 초기화
analyzer = CERTInsiderThreatAnalyzer(answers_folder="answers")

# 사용자 데이터 분석
user_data = {
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

result = analyzer.analyze_user_behavior(user_data)
print(result)
```

## 📁 파일 구조

```
.
├── cert_analysis.py          # 메인 분석 스크립트
├── cert_analysis.ipynb        # Jupyter Notebook 분석 도구
├── CERT_ANALYSIS_README.md    # 이 파일
├── requirements.txt           # Python 패키지 의존성
└── answers/                   # 정답 데이터 폴더
    ├── README.md              # 정답 데이터 설명
    ├── threat_indicators.json # 위협 지표 및 임계값
    └── known_threats.csv      # 과거 위협 사례 데이터
```

## 📊 분석 결과

### 출력 예시

```
================================================================================
CERT 내부자 위협 분석 보고서
================================================================================
생성 시각: 2024-01-29 15:30:00
================================================================================

[과거 위협 통계]
총 탐지된 위협: 10건
가장 흔한 위협 유형: ('data_exfiltration', 3)
해결률: 80.0%

위협 유형별 분포:
  - data_exfiltration: 3건
  - credential_theft: 2건
  - sabotage: 2건
  ...

--------------------------------------------------------------------------------
[사용자 행동 분석 결과]
--------------------------------------------------------------------------------

사용자 ID: USR999
전체 위험 점수: 0.915 (CRITICAL)
세부 위험 점수:
  - file_access: 1.000
  - email_activity: 1.000
  - login_behavior: 1.000
  - network_activity: 1.000

발생한 알림 (8건):
  ⚠ 일일 파일 접근 횟수 초과: 1200 > 1000
  ⚠ 고유 파일 접근 수 초과: 600 > 500
  ...

잠재적 위협 (2건):
  🔴 유형: data_exfiltration (신뢰도: high)
     심각도: critical
     권장 조치: Immediate investigation, Disable account, Review access logs
```

### 생성되는 파일

1. **cert_analysis_results.json**: 전체 분석 결과 (JSON 형식)
2. **cert_analysis_results.csv**: 사용자별 위험 점수 및 권장 조치 (CSV 형식)
3. **cert_threat_analysis.png**: 과거 위협 통계 시각화
4. **user_risk_analysis.png**: 사용자별 위험 점수 시각화

## 🔍 위협 지표 상세

### 임계값 설정

| 카테고리 | 지표 | 임계값 |
|---------|------|--------|
| 파일 접근 | 일일 파일 접근 | 1,000건 |
| 파일 접근 | 고유 파일 수 | 500개 |
| 파일 접근 | 민감한 파일 | 50개 |
| 이메일 | 외부 수신자 | 100명 |
| 이메일 | 첨부파일 크기 | 100MB |
| 로그인 | 업무 외 로그인 | 10회 |
| 로그인 | 실패 로그인 | 20회 |
| 네트워크 | 데이터 전송 | 50GB |
| 네트워크 | 외부 연결 | 200회 |

### 위험 점수 가중치

- 파일 접근: 30%
- 이메일 활동: 25%
- 로그인 행동: 25%
- 네트워크 활동: 20%

### 위협 수준 분류

- **CRITICAL** (0.7 이상): 즉시 조사 필요
- **HIGH** (0.5-0.7): 24시간 내 상세 검토 필요
- **MEDIUM** (0.3-0.5): 면밀한 모니터링
- **LOW** (0-0.3): 정기 모니터링
- **NORMAL** (0): 조치 불필요

## 🛡️ 보안 권장사항

1. **실시간 모니터링**: 시스템을 실시간으로 배포하여 지속적인 위협 탐지
2. **정기 검토**: 주간 또는 월간 단위로 위협 패턴 검토
3. **임계값 조정**: 조직의 특성에 맞게 임계값 조정
4. **교육 및 훈련**: 직원 대상 보안 인식 교육 실시
5. **사고 대응 계획**: 탐지된 위협에 대한 대응 절차 수립

## 📝 라이센스

이 프로젝트는 교육 및 연구 목적으로 제공됩니다.

## 🤝 기여

버그 리포트나 기능 제안은 이슈로 등록해주세요.

## 📧 연락처

문의사항이 있으시면 프로젝트 관리자에게 연락해주세요.
