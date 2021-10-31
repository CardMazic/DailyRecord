# 021 문자열 인덱싱
# letters = 'python'
# print(letters[0],letters[2])

# 022 문자열 슬라이싱
# license_plate = "24가 2210"
# print(license_plate[-4:])

# 023 문자열 인덱싱
# string = "홀짝홀짝홀짝"
# print(string[0::2]) # 홀만 출력

# 024 문자열 슬라이싱
# string = "PYTHON"
# print(string[::-1])   # 뒤에서부터 출력

# 025 문자열 치환
# phone_number = "010-1111-2222"
# phone_number2 = phone_number.replace("-"," ")
# print(phone_number2)

# 026 문자열 다루기
# phone_number = "010-1111-2222"
# phone_number2 = phone_number.replace("-","")
# print(phone_number2)

# 027 문자열 다루기
# 문자열로 표현된 url에서 .을 기준으로 분리합니다. 
# 분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있습니다.
# url = "http://sharebook.kr"
# url_split = url.split(".")
# print(url_split[-1])

# 028 문자열은 immutable
# lang = 'python'
# lang[0] = 'P'
# print(lang)

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# string = 'abcdfe2a354a32a'
# string_revise = string.replace("a","A")
# print(string_revise)

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
# string = 'abcd'
# string.replace('b', 'B')   # 변하지 않음, 새로운 문자열 객체를 리턴해주기 때문에, 변수를 이용해서 받아야 함
# print(string)

