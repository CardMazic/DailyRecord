# 031 문자열 합치기
# a = "3"
# b = "4"
# print(a+b)  # 34

# 032 문자열 곱하기
# print("Hi" * 3)

# 033 문자열 곱하기
# print("-" * 80)

# 034 문자열 곱하기
# t1 = 'python'
# t2 = 'java'
# print((t1 + " " + t2 + " ") * 4)

# 035 문자열 출력
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# # print 포맷팅에서 %s는 문자열 데이터 타입의 값을 %d는 정수형 데이터 타입 값의 출력을 의미합니다.
# print("이름 : %s 나이 %d " %(name1,age2))
# print("이름 : %s 나이 %d " % (name2,age2))

# 036 문자열 출력
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름 : {} 나이 {} ".format(name1,age1))
# print("이름 : {} 나이 {} ".format(name2,age2))


# 037 문자열 출력
# f-string을 사용
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름 : {name1} 나이 {age1}")
# print(f"이름 : {name2} 나이 {age2}")

# 038 컴마 제거하기
# 상장주식수 = "5,969,782,550"
# 컴마제거 = 상장주식수.replace(",", "")
# 타입변환 = int(컴마제거)
# print(타입변환, type(타입변환))

# 039 문자열 슬라이싱
# 분기 = "2020/03(E) (IFRS연결)"
# 인덱스 = 분기.index("(")
# print(분기[:인덱스])

# 040 strip 메서드
# strip 메소드를 이용하면, 좌우 공백 제거 됨
# data = "   삼성전자    "
# data_revise = data.split()
# print(data_revise)
