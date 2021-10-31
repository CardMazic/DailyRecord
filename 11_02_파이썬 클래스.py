# 261
# class Stock:
#   pass

# 262
# class Stock:
#   def __init__(self,name,code):
#     self.name = name
#     self.code = code
# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
    
# 263
# class Stock:
#   def __init__(self,name,code):
#     self.name = name
#     self.code = code
#   def set_name(self,name):
#     self.name = name
# a = Stock(None, None)
# a.set_name("삼성전자")
# print(a.name)

# 264
# class Stock:
#   def __init__(self,name,code):
#     self.name = name
#     self.code = code
#   def set_name(self,name):
#     self.name = name
#   def set_code(self,code):
#     self.code = code
# a = Stock(None, None)
# a.set_name("삼성전자")
# a.set_code("005930")
# print(a.name)
# print(a.code)

# 265
# class Stock:
#   def __init__(self,name,code):
#     self.name = name
#     self.code = code
#   def set_name(self,name):
#     self.name = name
#   def set_code(self,code):
#     self.code = code
#   def get_name(self):
#     return self.name
#   def get_code(self):
#     return self.code
# a = Stock("삼성전자", "005930")
# print(a.get_name(), a.get_code())

# 266
# class Stock:
#   def __init__(self,name,code,per,pbr,배당수익률):
#     self.name = name
#     self.code = code
#     self.per = per
#     self.pbr = pbr
#     self.배당수익률 = 배당수익률
#   def set_name(self,name):
#     self.name = name
#   def set_code(self,code):
#     self.code = code
#   def get_name(self):
#     return self.name
#   def get_code(self):
#     return self.code

# 267
# class Stock:
#   def __init__(self,name,code,per,pbr,배당수익률):
#     self.name = name
#     self.code = code
#     self.per = per
#     self.pbr = pbr
#     self.배당수익률 = 배당수익률
#   def set_name(self,name):
#     self.name = name
#   def set_code(self,code):
#     self.code = code
#   def get_name(self):
#     return self.name
#   def get_code(self):
#     return self.code
# a = Stock("삼성전자","005930",15.79,1.33,2.83)

# 268
# class Stock:
#   def __init__(self,name,code,per,pbr,배당수익률):
#     self.name = name
#     self.code = code
#     self.per = per
#     self.pbr = pbr
#     self.배당수익률 = 배당수익률
#   def set_name(self,name):
#     self.name = name
#   def set_code(self,code):
#     self.code = code
#   def set_per(self,per):
#     self.per = per
#   def set_pbr(self,pbr):
#     self.pbr = pbr
#   def set_dividend(self,배당수익률):
#     self.배당수익률 = 배당수익률  
#   def get_name(self):
#     return self.name
#   def get_code(self):
#     return self.code
# a = Stock("삼성전자","005930",15.79,1.33,2.83)

# 269
# class Stock:
#   def __init__(self,name,code,per,pbr,배당수익률):
#     self.name = name
#     self.code = code
#     self.per = per
#     self.pbr = pbr
#     self.배당수익률 = 배당수익률
#   def set_name(self,name):
#     self.name = name
#   def set_code(self,code):
#     self.code = code
#   def set_per(self,per):
#     self.per = per
#   def set_pbr(self,pbr):
#     self.pbr = pbr
#   def set_dividend(self,배당수익률):
#     self.배당수익률 = 배당수익률  
#   def get_name(self):
#     return self.name
#   def get_code(self):
#     return self.code
  
# a = Stock("삼성전자","005930",15.79,1.33,2.83)
# a.set_per(12.75)
# print(a.per)

# 270
class Stock:
  def __init__(self,name,code,per,pbr,배당수익률):
    self.name = name
    self.code = code
    self.per = per
    self.pbr = pbr
    self.배당수익률 = 배당수익률
  def set_name(self,name):
    self.name = name
  def set_code(self,code):
    self.code = code
  def set_per(self,per):
    self.per = per
  def set_pbr(self,pbr):
    self.pbr = pbr
  def set_dividend(self,배당수익률):
    self.배당수익률 = 배당수익률  
  def get_name(self):
    return self.name
  def get_code(self):
    return self.code
  
samsung = Stock("삼성전자","005930",15.79,1.33,2.83)
hyundai = Stock("현대차","005380",8.70,0.35,4.27)
lg = Stock("LG전자","066570",317.34,0.69,1.37)

ls = [samsung,hyundai,lg]
for per in ls:
  print(per.per)

print("깃허브 수정사항")
