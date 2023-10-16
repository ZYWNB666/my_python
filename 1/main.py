rabbit = 3  # 初始兔子个数

N = int(input("请输入年份N："))

for i in range(0,N):
    rabbit = rabbit * 2

# print(N + "年后兔子数量为" + rabbit + "个")
print("%d年后兔子的总数为%d"%(N,rabbit))