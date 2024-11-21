import os
import requests
from datetime import datetime

def fetch_naver_events(region, start_date, end_date):
    """네이버 API를 통해 이벤트 정보를 가져오는 함수"""
    client_id = os.getenv('NAVER_CLIENT_ID')
    client_secret = os.getenv('NAVER_CLIENT_SECRET')
    
    # 디버깅을 위해 API 키 출력
    print(f"Client ID: {client_id}")
    print(f"Client Secret: {client_secret}")
    
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
        "Content-Type": "application/json"  # 헤더 추가
    }
    
    # 검색어 생성 (예: "서울 축제 이벤트 2024")
    query = f"{region} 축제 이벤트 {start_date.year}"
    
    url = f"https://openapi.naver.com/v1/search/blog.json"
    params = {
        "query": query,
        "display": 20,
        "sort": "date"
    }
    
    # 디버깅용 출력
    print(f"Headers: {headers}")
    print(f"URL: {url}")
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get("items", [])
    except Exception as e:
        print(f"API 호출 중 오류 발생: {str(e)}")
        return []