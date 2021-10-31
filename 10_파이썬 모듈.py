# 241. 242
# import datetime
# now = datetime.datetime.now()

# 243
# for day in range(5,0,-1):
#   delta = datetime.timedelta(days=day)
#   date = now - delta
#   print(delta)

# 244
# import datetime
# now = datetime.datetime.now()

# print(now.strftime("%H:%M:%S"))

# 245
# import datetime
# day = "2021-09-27"
# ret = datetime.datetime.strftime(day,"%Y-%M-%D")
# print(ret, type(ret))

# 246
# import time
# import datetime
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 248
# import os
# ret = os.getcwd()
# print(ret, type(ret))


# 249
# text파일 이름 바꿈
# import os
# os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

# 250
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)
