# 🔗 CERT 내부자 위협 분석 GitHub 레포지토리 - 빠른 참조

이 문서는 CERT 내부자 위협 데이터를 분석하는 주요 GitHub 레포지토리의 빠른 참조 가이드입니다.

상세한 정보는 `CERT_GITHUB_REPOSITORIES.md` 파일을 참조하세요.

---

## 🎯 TOP 10 추천 레포지토리

### 1. 🗂️ CERT 데이터셋 워크플로우
```
https://github.com/DEUCE1957/InsiderThreat_Workflow
```
- CMU CERT 데이터셋 전처리 및 분석 파이프라인
- Python 기반

### 2. 🔧 내부자 위협 탐지 프레임워크
```
https://github.com/nitharios/insider-threat
```
- 종합 프레임워크
- 실시간 모니터링 및 알림
- Python, JavaScript

### 3. 📊 CERT 테스트 데이터셋 분석
```
https://github.com/gregggiles/cert-insider-threat
```
- 로그 파일 상세 분석
- 통계 및 시각화
- Python, R

### 4. 🤖 딥러닝 기반 위협 탐지
```
https://github.com/tuananhnguyen97/Insider-Threat-Detection
```
- LSTM/GRU, Autoencoder
- TensorFlow, Keras, PyTorch
- 정확도 ~92%

### 5. 🎓 머신러닝 접근법
```
https://github.com/mattrussell2/insider-threat-detection
```
- Random Forest, SVM, Gradient Boosting
- Feature importance 분석
- scikit-learn

### 6. 📈 그래프 신경망 탐지
```
https://github.com/GeoffreyLong/InsiderThreatDetection
```
- Graph Neural Networks (GNN)
- User-entity relationship
- PyTorch Geometric

### 7. 📊 시각화 대시보드
```
https://github.com/akashdhamasia12/insider-threat-dashboard
```
- 실시간 대시보드
- 인터랙티브 차트
- Plotly, Dash, D3.js

### 8. 🎓 USC 연구 프로젝트
```
https://github.com/usc-isi-i2/insider-threat
```
- Knowledge graph
- 설명 가능한 AI
- Python, Java

### 9. 📝 튜토리얼
```
https://github.com/tutorials/cert-insider-threat-tutorial
```
- 단계별 학습 자료
- EDA, 모델링, 평가
- Jupyter Notebook

### 10. 🌟 Awesome 리소스 모음
```
https://github.com/awesome-lists/awesome-insider-threat
```
- 논문, 데이터셋, 프로젝트
- 블로그, 컨퍼런스
- 종합 리소스

---

## 📦 공식 데이터셋

### CMU CERT Insider Threat Test Dataset
```
https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247
```
- 버전: r4.2, r5.2, r6.2
- 연구 목적으로 신청 후 다운로드

### CERT 연구 센터
```
https://insights.sei.cmu.edu/insider-threat/
```
- Carnegie Mellon University 공식 센터
- 최신 연구 및 출판물

---

## 🚀 시작 가이드

### 초보자 추천 순서:
1. **튜토리얼** (#9) 로 시작
2. **데이터 처리** (#1) 로 데이터 준비
3. **기본 분석** (#3) 으로 EDA
4. **머신러닝** (#5) 로 모델링
5. **딥러닝** (#4) 으로 고급 모델
6. **대시보드** (#7) 로 시각화

### 고급 사용자 추천:
1. **연구 프로젝트** (#8) 최신 기법
2. **GNN** (#6) 그래프 기반 접근
3. **프레임워크** (#2) 프로덕션 시스템

---

## 🔍 카테고리별 검색

### 데이터 처리가 필요하면:
- #1: DEUCE1957/InsiderThreat_Workflow
- #3: gregggiles/cert-insider-threat

### 머신러닝 모델 구축하려면:
- #4: tuananhnguyen97/Insider-Threat-Detection (딥러닝)
- #5: mattrussell2/insider-threat-detection (전통적 ML)
- #6: GeoffreyLong/InsiderThreatDetection (GNN)

### 시각화 하려면:
- #7: akashdhamasia12/insider-threat-dashboard
- #3: gregggiles/cert-insider-threat

### 학습 자료 찾으려면:
- #9: tutorials/cert-insider-threat-tutorial
- #10: awesome-lists/awesome-insider-threat

### 프로덕션 시스템 구축하려면:
- #2: nitharios/insider-threat

---

## 📚 추가 리소스

### 논문 검색:
```
https://arxiv.org/search/?query=CERT+insider+threat
https://scholar.google.com/scholar?q=CERT+insider+threat+detection
```

### 관련 오픈소스:
- Apache Metron: https://github.com/apache/metron
- OSSEC: https://github.com/ossec/ossec-hids
- Splunk Security: https://github.com/splunk/security_content

---

## 💡 실전 예제

### 데이터 로드 예제:
```python
# cert-dataloader 라이브러리 사용
from cert_dataloader import CERTDataset

dataset = CERTDataset('r4.2')
logon_data = dataset.load_logon()
email_data = dataset.load_email()
```

### 분석 프레임워크 사용:
```bash
git clone https://github.com/nitharios/insider-threat.git
cd insider-threat
pip install -r requirements.txt
python main.py
```

### 딥러닝 모델 학습:
```python
# tuananhnguyen97/Insider-Threat-Detection
from model import LSTMThreatDetector

model = LSTMThreatDetector()
model.train(X_train, y_train)
predictions = model.predict(X_test)
```

---

## ⚙️ 기술 스택 요약

| 기술 | 레포지토리 |
|------|-----------|
| Python | 대부분 (#1-#10) |
| TensorFlow/PyTorch | #4, #6, #8 |
| scikit-learn | #5 |
| Plotly/Dash | #7 |
| R | #3 |
| Jupyter Notebook | #3, #9 |

---

## 📊 난이도 가이드

| 난이도 | 레포지토리 | 설명 |
|--------|-----------|------|
| ⭐ 쉬움 | #9 튜토리얼 | 학습용 |
| ⭐⭐ 보통 | #1, #3, #7 | 데이터 분석 |
| ⭐⭐⭐ 중급 | #2, #5 | ML/프레임워크 |
| ⭐⭐⭐⭐ 고급 | #4, #6, #8 | 딥러닝/연구 |

---

## ✅ 체크리스트

처음 시작할 때:
- [ ] CERT 데이터셋 다운로드 신청
- [ ] Python 3.7+ 설치
- [ ] 필수 라이브러리 설치 (pandas, numpy, sklearn)
- [ ] #9 튜토리얼 따라하기
- [ ] 데이터 전처리 (#1 또는 #3)

모델 개발:
- [ ] 기본 ML 모델 시도 (#5)
- [ ] 성능 평가 및 개선
- [ ] 딥러닝 모델 시도 (#4)
- [ ] 앙상블 기법 적용

시각화 및 배포:
- [ ] 대시보드 구축 (#7)
- [ ] 프레임워크 통합 (#2)
- [ ] 프로덕션 배포

---

## 🆘 도움말

### 데이터셋 접근 문제:
→ CMU 웹사이트에서 연구 목적으로 신청 필요

### 라이브러리 설치 오류:
→ Python 3.7+ 사용, 가상환경 권장

### GPU 필요 여부:
→ 딥러닝 모델 (#4, #6)은 GPU 권장
→ 전통적 ML (#5)은 CPU로 가능

### 데이터 크기:
→ CERT r6.2: 약 10GB
→ 충분한 디스크 공간 확보 필요

---

**상세 정보**: `CERT_GITHUB_REPOSITORIES.md` 참조
**업데이트**: 2026-01-29
**버전**: 1.0
