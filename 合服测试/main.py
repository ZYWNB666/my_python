import datetime
import json
import os

import pandas as pd

# 获取windows系统变量
datetime_now_1 = datetime.datetime.now()
now_time = datetime_now_1.strftime('%Y年%m月%d日')      # 日期
username = os.environ.get('USERNAME')
now_time = "2023年10月16日"
# 变量赋值
json_save = fr"C:\\Users\\{username}\\Desktop\\合服\\json\\"          # JSON文件保存的目录
# input_excel = f"C:\\Users\\{username}\\Desktop\\合服\\{now_time}\\bk_cmdb_export_inst_3kd_gameserver (2).xlsx"  # 替换为从cow导出的Excel文件路径
input_excel = fr"C:\Users\user\Desktop\合服\output.xlsx"  # 替换为从cow导出的Excel文件路径
input_excel_hf = f"C:\\Users\\{username}\\Desktop\\合服\\{now_time}\\越南第七次合服合服方案23年10月16日_150人.xlsx"    # 替换为和服需求Excel的路径
sheet_name = "运维用分组"    # 替换为和服需求Excel的sheet名
output_dir = json_save
output_dir_hf = json_save
json_file_path1 = os.path.join(output_dir_hf, "hf_output.json")
json_file_path2 = os.path.join(output_dir_hf, "cow_output.json")
excel_output_path = fr"C:\Users\{username}\Desktop\合服\json\output.xlsx"  # 替换为你的输出 Excel 文件位置
zhufu_ip_path = os.path.join(output_dir_hf, "主服IP.txt")
beihefu_ip_path = os.path.join(output_dir_hf, "被和服IP.txt")
tmp_dir = os.environ.get('TMP', os.environ.get('TEMP'))
beihefu_ip_tmp_path = os.path.join(tmp_dir, "被和服IP_tmp.txt")

# check path
if beihefu_ip_tmp_path:
    if os.path.exists(beihefu_ip_tmp_path):
        os.remove(beihefu_ip_tmp_path)
if not os.path.exists(json_save):
    try:
        os.makedirs(json_save, exist_ok=True)
        print(f"目录 {json_save} 创建成功")
    except Exception as e:
        print(f"目录 {json_save} 创建失败，错误信息：{e}")



# ========================================生成JSON文件===========================================
if input_excel and output_dir:
    try:
        df = pd.read_excel(input_excel)
        json_file = f'{output_dir}cow_output.json'
        print("JSON文件保存在" + json_file)
        data_dict = df.to_dict(orient='records')
        with open(json_file, 'w', encoding='utf-8') as json_out:
            json.dump(data_dict, json_out, ensure_ascii=False, indent=4)
        json_file = f"{output_dir}/cow_output.json"
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception as e:
        print(f"发生错误: {e}")
if input_excel_hf and output_dir_hf:
    try:
        df = pd.read_excel(input_excel_hf, sheet_name=sheet_name)
        json_blocks = []
        grouped = df.groupby('A列')
        for name, group in grouped:
            group_data = {'主服务器': int(name), 'data': []}
            for _, row in group.iterrows():
                non_empty_data = {str(col): int(row[col]) for col in group.columns[1:] if pd.notna(row[col])}
                if non_empty_data:
                    group_data['data'].append(non_empty_data)
            if group_data['data']:
                json_blocks.append(group_data)
        json_file = f'{output_dir_hf}hf_output.json'
        print("JSON文件保存在" + json_file)
        with open(json_file, 'w', encoding='utf-8') as json_out:
            json.dump(json_blocks, json_out, ensure_ascii=False, indent=4)
        json_file = f"{output_dir_hf}/cow_output.json"
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception as e:
        print(f"发生错误: {e}")






# =====================================合服操作开始=====================================================

# 读取 合服列表json 文件
with open(json_file_path1, 'r', encoding='utf-8') as file:
    data_list_1 = json.load(file)

for outer_data in data_list_1:
    # 读取 主服务器 的id
    main_server_value = outer_data.get('主服务器', None)
    # print(main_server_value)
    # 读取 所有区服 的json文件
    with open(json_file_path2, 'r', encoding='utf-8') as file:
        data_list_2 = json.load(file)
        # 合服准备
        for inner_data in data_list_2:
            shili_name = inner_data.get('大区id(必填)', None)
            # print(shili_name)
            if shili_name == main_server_value:  # 判断主服务器所在的json块
                # 修改开服状态和合服属性的值
                inner_data['开服状态(必填)'] = 1
                inner_data['合服属性'] = "3"

                # 存储外网 IP 和内网 IP 的值为变量
                external_ip = inner_data.get('外网ip(必填)', None)
                internal_ip = inner_data.get('内网ip', None)
                # 将主服ip写入文件
                with open(zhufu_ip_path, 'a', encoding='utf-8') as file:
                    file.write(f"{internal_ip} {external_ip}\n")

                # # 打印结果
                # print("外网 IP:", external_ip)
                # print("内网 IP:", internal_ip)
                for data_dict in data_list_1:
                    if data_dict.get("主服务器") == main_server_value:
                        data_values = data_dict.get("data", [])
                        for item in data_values:
                            for key, value in item.items():
                                # print(f"{key} 的值:", value)
                                for inner_data_2 in data_list_2:
                                    if inner_data_2.get("大区id(必填)") == value:
                                        external_ip_2 = inner_data_2.get('外网ip(必填)', None)
                                        internal_ip_2 = inner_data_2.get('内网ip', None)
                                        if external_ip_2:
                                            with open(beihefu_ip_tmp_path, 'a', encoding='utf-8') as file:
                                                file.write(f"{internal_ip_2} {external_ip_2}\n")
                                for inner_data_1 in data_list_2:
                                    if inner_data_1.get("大区id(必填)") == value:
                                        inner_data_1['外网ip(必填)'] = external_ip
                                        inner_data_1['内网ip'] = internal_ip
                                        inner_data_1['开服状态(必填)'] = 1
                                        inner_data_1['合服属性'] = "1"
                # 存储修改后的json文件
                with open(json_file_path2, 'w', encoding='utf-8') as file:
                    json.dump(data_list_2, file, ensure_ascii=False, indent=4)

# 读取json文件 生成 xlsx文件
if json_file_path2:
    with open(json_file_path2, 'r', encoding='utf-8') as file:
        data_list = json.load(file)
    df = pd.json_normalize(data_list)
    df.to_excel(excel_output_path, index=False)
    print(f"转换完成，Excel 文件保存在: {excel_output_path}")

# 去重处理被合服IP
seen_values = set()
# 读取文件，去重数据，写回文件
with open(beihefu_ip_tmp_path, 'r', encoding='utf-8') as input_file, open(beihefu_ip_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        value = line.strip()
        if value not in seen_values:
            seen_values.add(value)
            output_file.write(f"{value}\n")

print(f"去重完成，去重后的数据保存在: {beihefu_ip_path}")
