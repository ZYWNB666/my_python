import json
import tkinter as tk
from tkinter import filedialog

import pandas as pd

# 创建主窗口
root = tk.Tk()
root.title("XLSX转JSON工具")


# 定义选择文件按钮的回调函数
def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)


# 定义选择保存目录按钮的回调函数
def choose_output_dir():
    output_dir = filedialog.askdirectory()
    entry_output.delete(0, tk.END)
    entry_output.insert(0, output_dir)


# 定义转换按钮的回调函数
def convert_to_json():
    input_file = entry_file.get()
    output_dir = entry_output.get()

    if input_file and output_dir:
        try:
            df = pd.read_excel(input_file)
            json_file = f'{output_dir}/output.json'

            # 将DataFrame转换为字典
            data_dict = df.to_dict(orient='records')

            # 将字典写入JSON文件并设置缩进格式
            with open(json_file, 'w', encoding='utf-8') as json_out:
                json.dump(data_dict, json_out, ensure_ascii=False, indent=4)

            json_file = f"{output_dir}/output.json"  # 替换为你的JSON文件路径
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)

            result_label.config(text=f'转换完成，JSON文件已保存到 {json_file}', fg='green')
        except Exception as e:
            result_label.config(text=f'转换失败: {str(e)}', fg='red')
    else:
        result_label.config(text='请选择输入文件和输出目录', fg='red')


# 创建和布置GUI元素
label_file = tk.Label(root, text="选择输入文件:")
label_output = tk.Label(root, text="选择输出目录:")
entry_file = tk.Entry(root, width=40)
entry_output = tk.Entry(root, width=40)
btn_choose_file = tk.Button(root, text="选择文件", command=choose_file)
btn_choose_output = tk.Button(root, text="选择输出目录", command=choose_output_dir)
btn_convert = tk.Button(root, text="转换为JSON", command=convert_to_json)
result_label = tk.Label(root, text="", fg='black')

label_file.grid(row=0, column=0, padx=10, pady=10, sticky='w')
entry_file.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
btn_choose_file.grid(row=0, column=3, padx=10, pady=10)
label_output.grid(row=1, column=0, padx=10, pady=10, sticky='w')
entry_output.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
btn_choose_output.grid(row=1, column=3, padx=10, pady=10)
btn_convert.grid(row=2, column=1, padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# 运行GUI主循环
root.mainloop()

ip_list = []
while True:
    ip = input("请输入 IP 地址 (不输入直接回车即为开始检索): ")

    # 检查用户是否输入 '结束'，如果是则退出循环
    if ip == '':
        break
    # 将输入的 IP 地址添加到列表中
    ip_list.append(ip)
# print(ip_list)
for slm in ip_list:
    # print(slm)

    # 读取 JSON 文件
    json_file = 'C:\\Users\\user\\Desktop\\fsdownload\\output.json'  # 替换为你的 JSON 文件路径
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

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
        open_date = item.get("大区开启时间")

        # 如果内网 IP 和外网 IP 都存在并且不为空
        if inner_ip and public_ip and short_character and slm == inner_ip or slm == public_ip:
            # if inner_ip and public_ip and short_character:
            # 创建一个唯一标识，结合内网 IP 和外网 IP
            unique_key = f"{inner_ip}_{public_ip}"

            # 如果唯一标识已经在字典中，将记录添加到对应的列表中
            if unique_key in ip_to_info:
                ip_to_info[unique_key].append((short_character, instance_name, region_id, kaifu_zt,open_date))
            else:
                # 否则，创建一个新的列表并添加记录
                ip_to_info[unique_key] = [(short_character, instance_name, region_id, kaifu_zt,open_date)]

    # 输出具有相同内网 IP 和外网 IP 的所有记录的 "合服属性"、"实例名(必填)" 和 "大区id(必填)"
    for unique_key, info_list in ip_to_info.items():
        if len(info_list) > 1:  # 只输出具有多个记录的唯一标识
            inner_ip, public_ip = unique_key.split('_')
            print(f"相同  内网IP: {inner_ip}, 外网IP: {public_ip}")
            for info in info_list:
                short_character, instance_name, region_id, kaifu_zt, open_date = info
                print(f"实例名: {instance_name}, 大区id: {region_id}, 大区开启时间: {open_date}, 合服属性: {short_character}, 开服状态：{kaifu_zt}")