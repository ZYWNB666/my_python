import json

import pandas as pd

input_excel_hf = "C:\\Users\\user\\Desktop\\合服\\2023年10月16日\\越南第七次合服合服方案23年10月16日_150人.xlsx"
sheet_name = "运维用分组"
output_dir_hf = "C:\\Users\\user\\Desktop\\合服\\json\\"

if input_excel_hf and output_dir_hf:
    try:
        # 添加 sheet_name 参数以指定要读取的工作表
        df = pd.read_excel(input_excel_hf, sheet_name=sheet_name)

        # 创建一个空列表来存储每个JSON块
        json_blocks = []

        # 使用 groupby 分组，A列可能有多个单元格合并的情况
        grouped = df.groupby('A列')

        # 遍历每个分组
        for name, group in grouped:
            # 创建一个字典来存储当前分组的数据
            group_data = {'主服务器': int(name), 'data': []}

            # 遍历每行数据
            for _, row in group.iterrows():
                # 创建一个字典来存储非空值的数据，将浮点数转换为整数
                non_empty_data = {str(col): int(row[col]) for col in group.columns[1:] if pd.notna(row[col])}

                # 如果非空值的数据字典不为空，则添加到data列表中
                if non_empty_data:
                    group_data['data'].append(non_empty_data)

            # 如果data列表不为空，则将当前分组的数据字典添加到JSON块列表中
            if group_data['data']:
                json_blocks.append(group_data)

        # 以下是你原来的代码
        json_file = f'{output_dir_hf}hf_output.json'
        print("JSON文件保存在" + json_file)

        # 将JSON块列表写入JSON文件并设置缩进格式
        with open(json_file, 'w', encoding='utf-8') as json_out:
            json.dump(json_blocks, json_out, ensure_ascii=False, indent=4)

        json_file = f"{output_dir_hf}/output.json"
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception as e:
        print(f"发生错误: {e}")


