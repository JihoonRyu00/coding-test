"""
백준 문제 풀이 파일 자동 생성기 (Baekjoon Problem Boilerplate Generator)

이 스크립트는 백준 온라인 저지(BOJ)의 문제 번호나 URL을 입력받아,
해당 문제의 제목을 크롤링하고 기본 템플릿 코드가 포함된 Python 파일을 생성합니다.

사용법:
    python base.py [문제번호]
    python base.py [문제URL]

예시:
    python base.py 1000
    python base.py https://www.acmicpc.net/problem/1000

필요 라이브러리:
    pip install requests beautifulsoup4
"""

import sys
import os
import requests
from bs4 import BeautifulSoup

# 입력값 검증
if len(sys.argv) < 2:
    print(f"사용법: python {sys.argv[0]} [문제번호] 또는 [URL]")
    sys.exit()

arg = sys.argv[1]

# 입력값이 숫자인지 URL인지 판단하여 ID와 URL 설정
if arg.isdigit():
    problem_id = arg
    url = f"https://www.acmicpc.net/problem/{problem_id}"
else:
    url = arg
    problem_id = url.rstrip("/").split("/")[-1]

filename = f"{problem_id}.py"

# 파일 중복 확인
if os.path.exists(filename):
    print(f"⚠️  {filename} 파일이 이미 존재합니다.")
    sys.exit()

# 문제 제목 크롤링
title = ""
try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title_element = soup.select_one("#problem_title")

    if title_element:
        title = title_element.text.strip()
    else:
        print("❌ 문제 제목을 찾을 수 없습니다. (올바른 문제 번호인가요?)")
        sys.exit()

except Exception as e:
    print(f"❌ 정보 가져오기 실패: {e}")
    sys.exit()

# 파일 생성 (기본 템플릿 포함)
content = f"""# {filename}
# {title}
# {url}

"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ {filename} 생성 완료! ({title})")
