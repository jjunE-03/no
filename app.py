import streamlit as st
import pandas as pd
from datetime import datetime
from utils.api_handler import fetch_naver_events
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 페이지 설정
st.set_page_config(
    page_title="KEventFinder - 한국 행사 정보 검색",
    page_icon="🎉",
    layout="wide"
)

# 타이틀 및 설명
st.title("🎉 KEventFinder")
st.subheader("대한민국 지역별 행사 및 이벤트 정보")

# 사이드바 설정
with st.sidebar:
    st.header("검색 옵션")
    
    # 지역 선택
    regions = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
              "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
    selected_region = st.selectbox("지역을 선택하세요", regions)
    
    # 날짜 선택
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("시작일", datetime.now())
    with col2:
        end_date = st.date_input("종료일", datetime.now())
    
    # 검색 버튼
    search_button = st.button("검색", type="primary")

# 메인 컨텐츠
if search_button:
    st.header(f"📍 {selected_region} 지역 행사 정보")
    st.caption(f"기간: {start_date} ~ {end_date}")
    
    # 로딩 표시
    with st.spinner('데이터를 가져오는 중...'):
        events = fetch_naver_events(selected_region, start_date, end_date)
    
    if not events:
        st.info("해당 조건에 맞는 행사 정보를 찾을 수 없습니다.")
    else:
        # 이벤트 정보 표시
        for idx, event in enumerate(events, 1):
            with st.container():
                col1, col2 = st.columns([7,3])
                with col1:
                    st.subheader(f"{idx}. {event['title'].replace('<b>','').replace('</b>','')}")
                    st.write(event['description'].replace('<b>','').replace('</b>',''))
                with col2:
                    st.link_button("자세히 보기", event['link'])
                st.divider()

# 푸터
st.markdown("---")
st.caption("© 2024 KEventFinder. Powered by Naver Open API")
