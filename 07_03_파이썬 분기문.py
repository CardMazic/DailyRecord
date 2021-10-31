# 121
# number = input("입력 : ")
# if number.isupper():
#   print(number.lower())
# elif number.islower():
#   print(number.upper())
# else:
#   print("오류입니다.")

# 122
# score = int(input("score : "))

# if 81 <= score <= 100:
#   grade = "A"
# elif 61 <= score <= 80:
#   grade = "B"
# elif 41 <= score <= 60:
#   grade = "C"
# elif 21 <= score <= 40:
#   grade = "D"
# elif 0 <= score <= 20:
#   grade = "E"

# print("grade is {}".format(grade))

# 123
# input_money = input("입력 : ")
# input_money = input_money.split()

# if input_money[1] == "달러":
#   print("{}원".format(1167 * int(input_money[0])))
# elif input_money[1] == "엔":
#   print("{}원".format(1096 * int(input_money[0])))
# if input_money[1] == "유로":
#   print("{}원".format(1268 * int(input_money[0])))

# 124
# n1 = input("input number1 : ")
# n2 = input("input number2 : ")
# n3 = input("input number3 : ")

# max = 0

# if n1 > n2:
#   if n1 > n3:
#     max = n1
#   else:
#     max = n3
# elif n1 < n2:
#   if n2 > n3:
#     max = n2
#   else:
#     max = n3

# 125
# phone = input("휴대전화 번호 입력 : ")
# first_phone = phone.split("-")
# ageny = ""

# if first_phone[0] == "011":
#   ageny = "SKT"
# elif first_phone[0] == "016":
#   ageny = "KT"
# elif first_phone[0] == "019":
#   ageny = "LGU"
# else:
#   ageny = "알수없음"
# print("당신은 {} 사용자입니다.".format(ageny))

# 126
# address = input("우편번호 : ")
# if address in ["010","011","012"]:
#   print("강북구")
# elif address in ["014","015","016"]:
#   print("도봉구")
# else:
#   print("노원구")

# 127
# id = input("주민등록번호 : ")
# id_gender = id.split("-")[1][0]

# if id_gender == "1" or id_gender == "3":
#   print("남성")
# else:
#   print("여성")

# 128
# 주민번호 = input("주민등록번호: ")
# 뒷자리 = 주민번호.split("-")[1]
# if 0 <= int(뒷자리[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

# 129
# num = input("주민등록번호: ")
# 계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#         int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#         int(num[11])* 4 + int(num[12]) * 5
# 계산2 = 11 - (계산1 % 11)
# 계산3 = str(계산2)

# if num[-1] == 계산3[-1]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

# 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# mv_range = btc["max_price"] - btc["min_price"]
# standard = mv_range + btc["opening_price"]

# if standard > btc["opening_price"]:
#   print("상승장")
# else:
#   print("하락장")








