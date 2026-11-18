## 📄 License

### Font

This project uses **Sandoll SamLip Hobang Font**, provided by Samlip Co., Ltd.

- Font: Sandoll SamLip Hobang
- Copyright: Samlip Co., Ltd.
- License: Refer to the license file in `dashboard/LICENSES/`
- Source: [Sandoll SamLip Hobang Font](https://spcsamlip.co.kr/brand/bakery/hopang/typography)

The font is redistributed in accordance with its license terms.

<br/>

---
# 📰 KoSTOPnews Dashboard

기업별 뉴스 데이터를 조회하고 AI 기반 감성 분석 및 키워드 분석 결과를 시각화하는 대시보드입니다.

Streamlit을 활용해 기업과 날짜별 뉴스 분석 결과를 확인할 수 있으며, FastAPI 서버와 연동하여 데이터를 조회합니다.

---

## 🏗️ Architecture

- **Streamlit**: API를 활용한 분석 결과 시각화
- **FastAPI**: API 엔드포인트 및 비즈니스 로직 처리
- **PostgreSQL (Supabase)**: 뉴스 원본 및 AI 분석 결과 저장

<br/>

#### 1차 Architecture - AWS 기반 서비스 구축
<div align="center">
  <img src="https://github.com/2026-KoSTOPnews/.github/blob/main/profile/assets/architecture.png" alt="KoSTOPnews Architecture" width="700">
</div>

<br/>

#### 2차 Architecture - 배포 환경 개선 및 비용 최적화
<div align="center">
  <img src="https://github.com/2026-KoSTOPnews/.github/blob/main/profile/assets/architecture2.png" alt="KoSTOPnews Architecture2" width="700">
</div>

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Frontend | Streamlit |
| Data Visualization | Plotly, WordCloud, Matplotlib |
| HTTP Client | Requests |
| Data Processing | Pandas |
| Backend | FastAPI |
| Database | PostgreSQL (Supabase) |
| Deployment | Streamlit Community Cloud |

---

## ✨ 주요 기능

### 1. 기업 및 날짜 선택
- 분석할 기업 선택
- 조회할 날짜 선택
- 선택한 기업과 날짜를 기준으로 분석 결과 조회

### 2. 뉴스 감성 분석
- 기업 관련 뉴스의 감성 분석 결과 시각화
- 긍정·중립·부정 감성 분포 확인

### 3. 키워드 분석
- 뉴스에서 추출한 주요 키워드 시각화
- 기업별 뉴스에서 자주 등장하는 키워드 확인

### 4. 워드 클라우드
- 뉴스 데이터를 기반으로 주요 단어 시각화
- 단어의 등장 빈도를 시각적으로 확인

### 5. 뉴스 조회
- 선택한 기업과 날짜에 해당하는 뉴스 기사 조회
- 페이지 단위로 뉴스 목록 확인

---

## 📂 Project Structure

```text
.
├── dashboard/
│   ├── app.py
│   ├── api.py
│   ├── components/
│   │   ├── analysis_section.py
│   │   ├── company_selector.py
│   │   ├── date_selector.py
│   │   ├── keywords.py
│   │   ├── news.py
│   │   ├── news_section.py
│   │   ├── sentiment.py
│   │   ├── wordcloud.py
│   │   └── wordcloud_section.py
│   ├── fonts/
│   │   └── SDSamliphopangcheTTFBasic.ttf
│   └── LICENSES/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

FastAPI 서버 주소를 환경 변수로 설정합니다.

```env
FASTAPI_URL=https://your-fastapi-server-url
```

Streamlit Community Cloud에서는 앱의 Secrets에 다음 값을 설정합니다.

```toml
FASTAPI_URL = "https://your-fastapi-server-url"
```

대시보드는 Streamlit Secrets를 우선적으로 확인하며, 설정이 없으면 환경 변수의 `FASTAPI_URL`을 사용합니다.

### 4. Run Dashboard

```bash
streamlit run dashboard/app.py
```

브라우저에서 Streamlit이 제공하는 로컬 주소로 접속합니다.

---

## ☁️ Deployment

Streamlit Community Cloud를 통해 대시보드를 배포합니다.

1. GitHub 저장소를 Streamlit Community Cloud에 연결합니다.
2. 실행 파일로 `dashboard/app.py`를 지정합니다.
3. 앱의 Secrets에 `FASTAPI_URL`을 설정합니다.
4. 배포된 대시보드에서 FastAPI 서버와 연동되는지 확인합니다.
