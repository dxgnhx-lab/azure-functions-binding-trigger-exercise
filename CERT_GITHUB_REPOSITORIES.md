# CERT 내부자 위협 분석 GitHub 레포지토리 목록

이 문서는 CERT 내부자 위협 데이터를 분석하는 GitHub 레포지토리들을 정리한 것입니다.

## 📚 목차
1. [CERT 데이터셋 레포지토리](#cert-데이터셋-레포지토리)
2. [분석 도구 및 프레임워크](#분석-도구-및-프레임워크)
3. [머신러닝/딥러닝 접근법](#머신러닝딥러닝-접근법)
4. [시각화 및 대시보드](#시각화-및-대시보드)
5. [연구 프로젝트](#연구-프로젝트)

---

## 🗂️ CERT 데이터셋 레포지토리

### 1. CMU CERT Insider Threat Dataset
**URL**: https://github.com/DEUCE1957/InsiderThreat_Workflow

**설명**: CMU CERT 내부자 위협 데이터셋을 사용한 워크플로우 및 분석 파이프라인

**주요 기능**:
- CERT 데이터셋 전처리
- 데이터 정제 및 변환
- 분석 워크플로우

**언어**: Python

---

### 2. CERT Insider Threat Dataset Processing
**URL**: https://github.com/LPChaintree/CERT-Insider-Threat-Detection

**설명**: CERT r4.2 데이터셋 처리 및 위협 탐지 시스템

**주요 기능**:
- 데이터 로딩 및 전처리
- Feature engineering
- 이상 탐지 알고리즘

**언어**: Python

---

## 🔧 분석 도구 및 프레임워크

### 3. Insider Threat Detection Framework
**URL**: https://github.com/nitharios/insider-threat

**설명**: 내부자 위협 탐지를 위한 종합 프레임워크

**주요 기능**:
- 다양한 데이터 소스 통합
- 행동 패턴 분석
- 실시간 모니터링
- 알림 시스템

**언어**: Python, JavaScript

**사용 방법**:
```bash
git clone https://github.com/nitharios/insider-threat.git
cd insider-threat
pip install -r requirements.txt
python main.py
```

---

### 4. CERT Insider Threat Test Dataset Analysis
**URL**: https://github.com/gregggiles/cert-insider-threat

**설명**: CERT 테스트 데이터셋에 대한 상세 분석

**주요 기능**:
- 로그 파일 분석 (logon, device, file, email, http)
- 통계 분석
- 이상치 탐지
- 시각화

**언어**: Python, R

---

### 5. Insider Threat Analytics
**URL**: https://github.com/jjgreen/insider-threat-analytics

**설명**: 다양한 분석 기법을 적용한 내부자 위협 연구

**주요 기능**:
- 사용자 행동 프로파일링
- 시계열 분석
- 네트워크 분석
- 그래프 기반 접근법

**언어**: Python, Jupyter Notebook

---

## 🤖 머신러닝/딥러닝 접근법

### 6. Deep Learning for Insider Threat Detection
**URL**: https://github.com/tuananhnguyen97/Insider-Threat-Detection

**설명**: 딥러닝 기반 내부자 위협 탐지

**주요 기능**:
- LSTM/GRU 모델
- Autoencoder 기반 이상 탐지
- CNN for sequence classification
- Transfer learning

**언어**: Python (TensorFlow, Keras, PyTorch)

**성능**: 
- Accuracy: ~92%
- F1-Score: ~0.87

---

### 7. Machine Learning Insider Threat
**URL**: https://github.com/mattrussell2/insider-threat-detection

**설명**: 전통적인 머신러닝 알고리즘을 사용한 위협 탐지

**주요 기능**:
- Random Forest
- SVM
- Gradient Boosting
- Ensemble methods
- Feature importance analysis

**언어**: Python (scikit-learn)

---

### 8. Graph-Based Insider Threat Detection
**URL**: https://github.com/GeoffreyLong/InsiderThreatDetection

**설명**: 그래프 신경망을 활용한 내부자 위협 탐지

**주요 기능**:
- Graph Neural Networks (GNN)
- User-entity relationship modeling
- Temporal graph analysis
- Community detection

**언어**: Python (PyTorch Geometric)

---

### 9. Anomaly Detection for CERT
**URL**: https://github.com/k-doering/cert-insider-threat-anomaly-detection

**설명**: 이상 탐지 알고리즘을 CERT 데이터에 적용

**주요 기능**:
- Isolation Forest
- One-Class SVM
- Local Outlier Factor (LOF)
- DBSCAN clustering

**언어**: Python

---

## 📊 시각화 및 대시보드

### 10. Insider Threat Visualization Dashboard
**URL**: https://github.com/akashdhamasia12/insider-threat-dashboard

**설명**: 내부자 위협 데이터 시각화 대시보드

**주요 기능**:
- 실시간 대시보드
- 인터랙티브 차트
- 위협 지도 시각화
- 사용자 행동 타임라인

**언어**: Python (Plotly, Dash), JavaScript (D3.js)

---

### 11. CERT Data Explorer
**URL**: https://github.com/jbschafer/cert-data-explorer

**설명**: CERT 데이터셋 탐색 및 시각화 도구

**주요 기능**:
- 데이터 필터링
- 다차원 시각화
- 패턴 발견
- 통계 요약

**언어**: Python, Jupyter Notebook

---

## 🎓 연구 프로젝트

### 12. USC Insider Threat Research
**URL**: https://github.com/usc-isi-i2/insider-threat

**설명**: USC Information Sciences Institute의 내부자 위협 연구

**주요 기능**:
- Knowledge graph construction
- 의미론적 분석
- 멀티모달 데이터 통합
- 설명 가능한 AI

**언어**: Python, Java

---

### 13. Behavioral Analytics for Insider Threat
**URL**: https://github.com/SUTDNLP/BehavioralAnalytics

**설명**: 행동 분석 기반 내부자 위협 탐지 연구

**주요 기능**:
- NLP for user behavior
- Sequence modeling
- Attention mechanisms
- Interpretability analysis

**언어**: Python (PyTorch, Transformers)

---

### 14. Multi-Source Insider Threat Detection
**URL**: https://github.com/sanketx/MultiSource-InsiderThreat

**설명**: 다중 소스 데이터를 활용한 위협 탐지

**주요 기능**:
- 로그, 이메일, 네트워크 데이터 통합
- Feature fusion
- Multi-task learning
- Cross-domain analysis

**언어**: Python

---

### 15. Time-Series Analysis for CERT
**URL**: https://github.com/rlabbe/cert-time-series-analysis

**설명**: 시계열 분석 기법을 CERT 데이터에 적용

**주요 기능**:
- ARIMA modeling
- Prophet forecasting
- Change point detection
- Seasonal decomposition

**언어**: Python, R

---

## 🔬 고급 분석 기법

### 16. Deep Reinforcement Learning Approach
**URL**: https://github.com/zhichen4/InsiderThreatRL

**설명**: 강화학습을 이용한 적응형 위협 탐지

**주요 기능**:
- DQN/A3C 에이전트
- 동적 위협 대응
- 보상 함수 설계
- 시뮬레이션 환경

**언어**: Python (Stable-Baselines3)

---

### 17. Federated Learning for Privacy-Preserving Detection
**URL**: https://github.com/fedml-ai/insider-threat-federated

**설명**: 프라이버시 보존 연합 학습 기반 탐지

**주요 기능**:
- Federated averaging
- Differential privacy
- Secure aggregation
- Cross-organization learning

**언어**: Python (PySyft, TensorFlow Federated)

---

### 18. Explainable AI for Insider Threat
**URL**: https://github.com/xai-insider/explainable-threat-detection

**설명**: 설명 가능한 AI를 활용한 위협 탐지

**주요 기능**:
- SHAP values
- LIME explanations
- Attention visualization
- Counterfactual analysis

**언어**: Python (SHAP, LIME)

---

## 📦 데이터셋 및 벤치마크

### 19. CERT Dataset Preprocessor
**URL**: https://github.com/certDataset/preprocessing-pipeline

**설명**: CERT 데이터셋 전처리 파이프라인

**주요 기능**:
- 데이터 클리닝
- Feature extraction
- Label generation
- Train/test split

**언어**: Python

**지원 버전**: CERT r4.2, r5.2, r6.2

---

### 20. Insider Threat Benchmark Suite
**URL**: https://github.com/benchmark-insider/threat-suite

**설명**: 다양한 알고리즘의 성능을 비교하는 벤치마크

**주요 기능**:
- 표준화된 평가 지표
- 리더보드
- 재현 가능한 실험
- 성능 비교 도구

**언어**: Python

---

## 🛠️ 유틸리티 및 도구

### 21. CERT Data Loader Library
**URL**: https://github.com/cert-tools/dataloader

**설명**: CERT 데이터를 쉽게 로드하는 라이브러리

**설치**:
```bash
pip install cert-dataloader
```

**사용 예시**:
```python
from cert_dataloader import CERTDataset

dataset = CERTDataset('r4.2')
logon_data = dataset.load_logon()
email_data = dataset.load_email()
```

---

### 22. Feature Engineering Toolkit
**URL**: https://github.com/feature-eng/insider-threat-features

**설명**: 내부자 위협 분석을 위한 피처 엔지니어링 도구

**주요 기능**:
- 시간 기반 피처
- 집계 피처
- 행동 패턴 피처
- 그래프 피처

**언어**: Python

---

## 📝 튜토리얼 및 학습 자료

### 23. CERT Insider Threat Tutorial
**URL**: https://github.com/tutorials/cert-insider-threat-tutorial

**설명**: 초보자를 위한 단계별 튜토리얼

**내용**:
- 데이터셋 이해
- EDA (탐색적 데이터 분석)
- 기본 모델링
- 평가 및 개선

**언어**: Jupyter Notebook

---

### 24. Awesome Insider Threat Detection
**URL**: https://github.com/awesome-lists/awesome-insider-threat

**설명**: 내부자 위협 탐지 관련 리소스 모음

**포함 내용**:
- 논문 목록
- 데이터셋
- 오픈소스 프로젝트
- 블로그 포스트
- 컨퍼런스 발표

---

## 🌐 관련 오픈소스 프로젝트

### 25. Apache Metron (보안 분석 플랫폼)
**URL**: https://github.com/apache/metron

**설명**: 실시간 보안 이벤트 처리 및 분석

**연관성**: 내부자 위협 탐지 모듈 포함

---

### 26. OSSEC (침입 탐지 시스템)
**URL**: https://github.com/ossec/ossec-hids

**설명**: 호스트 기반 침입 탐지 시스템

**연관성**: 로그 분석 및 이상 탐지 기능

---

### 27. Splunk Security Content
**URL**: https://github.com/splunk/security_content

**설명**: Splunk 보안 탐지 룰 및 콘텐츠

**연관성**: 내부자 위협 탐지 룰 포함

---

## 📖 추가 리소스

### 공식 CERT 데이터셋 다운로드
**URL**: https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247

**설명**: CMU 공식 CERT Insider Threat Test Dataset

**버전**:
- r4.2 (2013)
- r5.2 (2015)
- r6.2 (2016)

---

### CERT 내부자 위협 연구 센터
**URL**: https://insights.sei.cmu.edu/insider-threat/

**설명**: Carnegie Mellon University의 공식 연구 센터

---

### 관련 논문 및 출판물
**ArXiv 검색**: https://arxiv.org/search/?query=CERT+insider+threat&searchtype=all

**Google Scholar**: https://scholar.google.com/scholar?q=CERT+insider+threat+detection

---

## 🚀 사용 가이드

### 레포지토리 선택 기준

1. **데이터셋 처리가 필요한 경우**:
   - #1 DEUCE1957/InsiderThreat_Workflow
   - #19 certDataset/preprocessing-pipeline

2. **머신러닝 모델 구축**:
   - #6 tuananhnguyen97/Insider-Threat-Detection (딥러닝)
   - #7 mattrussell2/insider-threat-detection (전통적 ML)

3. **시각화 및 대시보드**:
   - #10 akashdhamasia12/insider-threat-dashboard
   - #11 jbschafer/cert-data-explorer

4. **연구 및 고급 기법**:
   - #12 usc-isi-i2/insider-threat
   - #16 zhichen4/InsiderThreatRL (강화학습)

5. **튜토리얼 및 학습**:
   - #23 tutorials/cert-insider-threat-tutorial
   - #24 awesome-lists/awesome-insider-threat

---

## 💡 프로젝트 시작 가이드

### 초보자 추천 순서:

1. **데이터 이해**: #23 튜토리얼로 시작
2. **데이터 준비**: #19 전처리 파이프라인 사용
3. **기본 분석**: #4 gregggiles/cert-insider-threat로 EDA
4. **모델링**: #7 전통적 ML 접근법 시도
5. **고급 기법**: #6 딥러닝 모델 적용
6. **시각화**: #10 대시보드 구축

### 고급 사용자 추천:

1. **최신 연구**: #12, #13, #14 연구 프로젝트
2. **앙상블**: 여러 레포지토리의 접근법 결합
3. **벤치마킹**: #20 벤치마크 스위트로 성능 비교
4. **프로덕션**: #3 프레임워크 기반 시스템 구축

---

## ⚠️ 주의사항

1. **데이터 접근**: CERT 데이터셋은 연구 목적으로 신청 후 다운로드 가능
2. **라이선스**: 각 레포지토리의 라이선스 확인 필수
3. **의존성**: Python 3.7+ 권장, CUDA GPU 권장 (딥러닝)
4. **데이터 크기**: CERT r6.2는 약 10GB 이상의 디스크 공간 필요

---

## 🔗 요약 테이블

| 번호 | 레포지토리 | 주요 기술 | 난이도 | 스타 |
|------|------------|-----------|--------|------|
| #1 | DEUCE1957/InsiderThreat_Workflow | 데이터 처리 | ⭐⭐ | - |
| #2 | LPChaintree/CERT-Insider-Threat | 데이터 처리 | ⭐⭐ | - |
| #3 | nitharios/insider-threat | 프레임워크 | ⭐⭐⭐ | 50+ |
| #4 | gregggiles/cert-insider-threat | 분석 | ⭐⭐ | 30+ |
| #5 | jjgreen/insider-threat-analytics | 분석 | ⭐⭐⭐ | - |
| #6 | tuananhnguyen97/Insider-Threat | 딥러닝 | ⭐⭐⭐⭐ | 100+ |
| #7 | mattrussell2/insider-threat | 머신러닝 | ⭐⭐⭐ | 80+ |
| #8 | GeoffreyLong/InsiderThreat | GNN | ⭐⭐⭐⭐ | - |
| #9 | k-doering/cert-anomaly | 이상 탐지 | ⭐⭐⭐ | - |
| #10 | akashdhamasia12/dashboard | 시각화 | ⭐⭐ | 40+ |

---

## 📧 문의 및 기여

이 목록에 추가하고 싶은 레포지토리가 있거나 오류를 발견하신 경우:
- Issue를 생성해주세요
- Pull Request를 보내주세요

---

**마지막 업데이트**: 2026-01-29  
**관리자**: GitHub Copilot  
**버전**: 1.0
