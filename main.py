import json

import pandas as pd

input_excel = input("请输入xlsx文件地址：")
output_dir = "C:\\Users\\user\\Documents\\"   # 替换为你要保存的JSON文件路径,默认是保存在此电脑的文章目录下的output.json
# print(input_excel)
if input_excel and output_dir:
    try:
        df = pd.read_excel(input_excel)
        json_file = f'{output_dir}output.json'
        print("JSON文件保存在" + json_file)
        data_dict = df.to_dict(orient='records')

        # 将字典写入JSON文件并设置缩进格式
        with open(json_file, 'w', encoding='utf-8') as json_out:
            json.dump(data_dict, json_out, ensure_ascii=False, indent=4) 

        json_file = f"{output_dir}/output.json"
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception as e:
        print(f"发生错误: {e}")

ip_list = []
while True:
    ip = input("请输入 IP 地址 (不输入直接回车即为开始检索): ")

    # 检查用户是否输入，如果没输入则退出循环
    if ip == '':
        break
    # 将输入的 IP 地址添加到列表中
    ip_list.append(ip)

for slm in ip_list:

    ip_to_info = {}
    # 遍历每个 JSON 块
    for item in data:
        # 提取字段值
        inner_ip = item.get("内网ip")
        public_ip = item.get("外网ip(必填)")
        short_character = item.get("合服属性")
        instance_name = item.get("实例名(必填)")
        region_id = item.get("大区id(必填)")
        open_zt = item.get("开服状态(必填)")
        open_date = item.get("大区开启时间")

        # 如果内网 IP 和外网 IP 都存在并且不为空
        if inner_ip and public_ip and short_character and slm == inner_ip or slm == public_ip:
            # if inner_ip and public_ip and short_character:
            # 创建一个唯一标识，结合内网 IP 和外网 IP
            unique_key = f"{inner_ip}_{public_ip}"
            if unique_key in ip_to_info:
                ip_to_info[unique_key].append((short_character, instance_name, region_id, open_zt, open_date))
            else:
                ip_to_info[unique_key] = [(short_character, instance_name, region_id, open_zt, open_date)]

    for unique_key, info_list in ip_to_info.items():
        if len(info_list) > 1:
            inner_ip, public_ip = unique_key.split('_')
            print("")
            print("-------------------------------------------------------------------------")
            print(f"相同  内网IP: {inner_ip}, 外网IP: {public_ip}")
            for info in info_list:
                short_character, instance_name, region_id, open_zt, open_date = info
                print(
                    f"实例名: {instance_name}, 大区id: {region_id}, 大区开启时间: {open_date}, 合服属性: {short_character}, 开服状态：{open_zt}")
