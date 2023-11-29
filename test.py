# import random
#
# # 生成6个1到33之间的随机整数
# random_integers_33 = [random.randint(1, 33) for _ in range(6)]
#
# # 生成1个1到16之间的随机整数
# random_integer_16 = random.randint(1, 16)
#
# # 输出生成的随机整数
# print("6个1到33之间的随机整数:", random_integers_33)
# print("1个1到16之间的随机整数:", random_integer_16)
import random

# 随机生成6个1-33之间的整数
rand_num = [random.randint(1, 33) for _ in range(6)]

# 随机生成1个1-16范围内的整数
rand_bonus_num = random.randint(1, 16)

# 输出这些数字
print("6个1-33之间的整数是：", rand_num)
print("1个1-16范围内的整数是：", rand_bonus_num)

# # test
# for num in rand_num:
#     print(num)
# print(bonus_num)
