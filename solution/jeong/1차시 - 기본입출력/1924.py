from datetime import datetime

# 사용자에게 월과 일이 공백으로 구분된 문자열을 입력 받는다.
user_input = input()

# 1월 1일 월요일을 기준으로 두 날짜의 일수 차이를 구한다.
dt1 = datetime.strptime("1 1", "%m %d")
dt2 = datetime.strptime(user_input, "%m %d")
td = (dt2 - dt1).days

# 요일 리스트
# td를 7로 나눈 나머지를 구한다.
# 나머지가 0이면 MON, 1이면 TUE, ..., 6이면 SUN 출력하도록 구현
l = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(l[td%7])

# 블로그 자료 정리 : https://jyostudy.tistory.com/82 
