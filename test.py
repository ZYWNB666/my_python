import json

# ip_list = []
# while True:
#     ip = input("请输入一个 IP 地址 (或输入 '结束' 来退出): ")
#
#     # 检查用户是否输入 '结束'，如果是则退出循环
#     if ip == '结束':
#         break
#     # 将输入的 IP 地址添加到列表中
#     ip_list.append(ip)
# print(ip_list)
# for slm in ip_list:
#     print(slm)

# 读取 JSON 文件
json_file = 'C:\\Users\\user\\Desktop\\fsdownload\\output.json'  # 替换为你的 JSON 文件路径
with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
slm = input("请输入本次和服的主服IP:")
# 创建一个字典以存储内网 IP 和外网 IP 到 "短字符、实例名和大区id" 的映射
ip_to_info = {}
# 遍历每个 JSON 块
for item in data:
    # 提取内网 IP、外网 IP、短字符、实例名和大区id字段的值
    inner_ip = item.get("内网ip")
    public_ip = item.get("外网ip(必填)")
    short_character = item.get("合服属性")
    instance_name = item.get("实例名(必填)")
    region_id = item.get("大区id(必填)")
    kaifu_zt = item.get("开服状态(必填)")

    # 如果内网 IP 和外网 IP 都存在并且不为空
    if inner_ip and public_ip and short_character and inner_ip == slm:
        # if inner_ip and public_ip and short_character:
        # 创建一个唯一标识，结合内网 IP 和外网 IP
        unique_key = f"{inner_ip}_{public_ip}"

        # 如果唯一标识已经在字典中，将记录添加到对应的列表中
        if unique_key in ip_to_info:
            ip_to_info[unique_key].append((short_character, instance_name, region_id, kaifu_zt))
        else:
            # 否则，创建一个新的列表并添加记录
            ip_to_info[unique_key] = [(short_character, instance_name, region_id, kaifu_zt)]

# 输出具有相同内网 IP 和外网 IP 的所有记录的 "合服属性"、"实例名(必填)" 和 "大区id(必填)"
for unique_key, info_list in ip_to_info.items():
    if len(info_list) > 1:  # 只输出具有多个记录的唯一标识
        inner_ip, public_ip = unique_key.split('_')
        print(f"相同  内网IP: {inner_ip}, 外网IP: {public_ip}")
        for info in info_list:
            short_character, instance_name, region_id, kaifu_zt = info
            print(f"合服属性: {short_character}, 实例名: {instance_name}, 大区id: {region_id}, 开服状态：{kaifu_zt}")
