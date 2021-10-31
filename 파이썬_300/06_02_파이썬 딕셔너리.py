# 091 딕셔너리 생성
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}

# 092 딕셔너리 인덱싱
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# print(inventory["메로나"][0])

# 093 딕셔너리 인덱싱
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# print(inventory["메로나"][1])

# 094 딕셔너리 추가
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# inventory["월드콘"] = [500,7]
# print(inventory)

# 095 딕셔너리 keys() 메서드
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream_keys = list(icecream.keys())
# print(icecream_keys)

# 096 딕셔너리 values() 메서드
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream_values = list(icecream.values())
# print(icecream_values)

# 098 딕셔너리 update 메서드
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)

# 099 zip과 dict
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# new = dict(zip(keys,vals))    # zip을 통해서 엮고, dict를 통해서 형변환을 이루어낸다
# print(new)

# 100 zip과 dict
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date,close_price))
# print(close_table)

