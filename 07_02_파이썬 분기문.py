# 111
# s1 = input("")
# print(s1 * 2)

# 112
# s = int(input("숫자를 입력하세요 : "))
# print(s + 10)

# 113
# s = int(input(""))
# if s % 2 == 0:
#   print("짝수")
# else:
#   print("홀수")

# 114
# s = int(input("입력값 : "))
# if (s + 20) > 255:
#   print("출력값 : {}".format(255))
# else:
#   print("출력값 : {}".format(s + 20))

# 115
# s = int(input("입력값 : "))
# s = s - 20
# if s < 0:
#   print("출력값 : {}".format(0))
# elif s > 255:
#   print("출력값 : {}".format(255))

# 116
# s = input("현재시간 : ")
# if(s[3:5] == "00"):
#   print("정각입니다.")
# else:
#   print("정각이 아닙니다.")

# 117
# fruit = ["사과", "포도", "홍시"]
# input_fruit = input("좋아하는 과일은? ")

# if input_fruit in fruit:
#   print("정답입니다.")
# else:
#   print("아닙니다.")


# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# name = input("투자 종목 입력 : ")

# if name in warn_investment_list:
#   print("투자 경고 종목입니다")
# else:
#   print("투자 경고 종목이 아닙니다.")

# 119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# input_fruit = input("제가 좋아하는 계절은? ")

# if input_fruit in fruit.keys():
#   print("정답입니다")
# else:
#   print("오답입니다.")

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
input_fruit = input("제가 좋아하는 과일은? ")

if input_fruit in fruit.values():
  print("정답입니다")
else:
  print("오답입니다.")  