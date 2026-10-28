# 1. 오늘 공부한 거 기록하면 현재 날짜로 저장
# 2. 저장한 것을 오늘을 기준으로 내일, 3일 뒤, 1주일 뒤 시간으로 복습 주기 저장
# 3. `1` 입력하면 현재 날짜의 해야하는 복습 과제 목록 출력
# 4. `2` 입력하면 현재 JLPT 시험까지 디데이 며칠인지 출력

from datetime import date, timedelta
import time
import json

# 저장된 데이터 불러오기
try:
    with open("to_do_list.json", "r", encoding="utf-8") as f:
        to_do_list = json.load(f)
        
    # 기존 문자열 데이터를 리스트로 변환
    for k, v in to_do_list.items():
        if isinstance(v, str):
            to_do_list[k] = [v]
            
except FileNotFoundError:
    to_do_list = {}


today = date.today()
tomorrow = str(today + timedelta(days=1))
three_days_later = str(today + timedelta(days=3))
next_week = str(today + timedelta(weeks=1))
is_hide_menu = False

# 디데이는 이 코드를 바꾸면 쓸 수 있습니다!!!!
target_date = date(2026, 12, 6)
d_day = (target_date - today).days

print("프로그램이 시작됐습니다")

while True:

    if is_hide_menu:
        print(" ")
    else:
        time.sleep(0.5)
        print(" ")
        print("=== 메뉴 ===")
        print("1: 오늘 공부 입력 | 2: 금일 복습 목록 | 3: JLPT 디데이 | 4: 메뉴 숨기기 | 5: 종료")
        print("============")
        print(" ")

    menu = int(input("메뉴 입력: "))
    print(" ")

    if menu == 1:
        TIL = input("오늘은 뭘 했니: ")

        to_do_list.setdefault(tomorrow, []).append("[공부한 지 하루 지남] " + TIL)
        
        to_do_list.setdefault(three_days_later, []).append("[복습한 지 3일 지남] " + TIL)
        
        to_do_list.setdefault(next_week, []).append("[복습한 지 1주일 지남] " + TIL)

        with open("to_do_list.json", "w", encoding="utf-8") as f:
            json.dump(to_do_list, f, ensure_ascii=False, indent=4)
            

    elif menu == 2:
        print("========================")
        for k, v in to_do_list.items():
            if str(today) == k:
                for task in v:
                    time.sleep(0.3)
                    print(" ")
                    print(task)
        print("========================")
        print(" ")

    elif menu == 3:
        if d_day > 0:
            print(f"D-{d_day}")
        elif d_day == 0:
            print("D-Day!!!!!!!")
        else:
            print(f"D+{abs(d_day)}")
        print(" ")

    elif menu == 4:
        is_hide_menu = True
        print("\033[32m메뉴 숨김\033[0m")

    elif menu == 5:
        print("프로그램을 종료합니다")
        time.sleep(0.1)
        
        for i in range(3):
            time.sleep(0.2)
            print(".")
        
        time.sleep(0.2)
        print("\033[32mexit\033[0m")
        break
    
    else:
        print(" ")
        print("\033[31m올바른 메뉴를 입력해주세요!\033[0m")
        print(" ")