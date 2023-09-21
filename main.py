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

