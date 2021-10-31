# 252
# class Human:
#   pass

# 253
# class Human:
#   def __init__(self):
#     print("응애응애")
# areum = Human()

# 254
# class Human:
#   def __init__(self):
#     print("응애응애")
#   def __init__(self,name,age,gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
# areum = Human("이름",25,"남자")
# print(areum.name)

# 256
# class Human:
#   def __init__(self):
#     print("응애응애")
#   def __init__(self,name,age,gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
# areum = Human("이름",25,"남자")
# print(f'이름 : {areum.name} 나이 : {areum.age} 성별 : {areum.gender}')

# 257
# class Human:
#   def __init__(self):
#     print("응애응애")
#   def __init__(self,name,age,gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
#   def who(self):
#     print(f'이름 : {self.name} 나이 : {self.age} 성별 : {self.gender}')
# areum = Human("이름",25,"남자")
# areum.who()

# 258
# class Human:
#   def __init__(self):
#     print("응애응애")
#   def __init__(self,name,age,gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
#   def who(self):
#     print(f'이름 : {self.name} 나이 : {self.age} 성별 : {self.gender}')
#   def setInfo(self, name, age, gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
# areum = Human("이름",25,"남자")
# areum.who()
# areum.setInfo("아름", 25, "여자")
# areum.who()

# 259
class Human:
  def __init__(self):
    print("응애응애")
  def __init__(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender
  def who(self):
    print(f'이름 : {self.name} 나이 : {self.age} 성별 : {self.gender}')
  def setInfo(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  def __del__(self):                  # 생성자 소멸시 나타낼 수 있는 함수
    print("나의 죽음을 알리지마라")
areum = Human("이름",25,"남자")
areum.who()
del areum
