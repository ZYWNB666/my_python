import json

# 读取 合服列表json 文件
json_file_path1 = "C:\\Users\\user\\Desktop\\合服\\json\\hf_output.json"
with open(json_file_path1, 'r', encoding='utf-8') as file:
    data_list_1 = json.load(file)

for outer_data in data_list_1:
    # 读取 主服务器 的值
    #print("--------------------")
    main_server_value = outer_data.get('主服务器', None)
    #print(main_server_value)
    # 读取 所有区服 的json文件
    json_file_path2 = "C:\\Users\\user\\Desktop\\合服\\json\\cow_output.json"
    with open(json_file_path2, 'r', encoding='utf-8') as file:
        data_list_2 = json.load(file)
        # 合服准备
        for inner_data in data_list_2:
            shili_name = inner_data.get('大区id(必填)', None)
            # print(shili_name)
            if shili_name == main_server_value: # 判断主服务器所在的json块
                # 修改开服状态和合服属性的值
                inner_data['开服状态(必填)'] = 1
                inner_data['合服属性'] = "3"

                # 存储外网 IP 和内网 IP 的值为变量
                external_ip = inner_data.get('外网ip(必填)', None)
                internal_ip = inner_data.get('内网ip', None)

                # # 打印结果
                # print("外网 IP:", external_ip)
                # print("内网 IP:", internal_ip)
                for data_dict in data_list_1:
                    if data_dict.get("主服务器") == main_server_value:
                        data_values = data_dict.get("data", [])
                        for item in data_values:
                            for key, value in item.items():
                                # print(f"{key} 的值:", value)
                                for inner_data_1 in data_list_2:
                                    if inner_data_1.get("大区id(必填)") == value:
                                        inner_data_1['外网ip(必填)'] = external_ip
                                        inner_data_1['内网ip'] = internal_ip
                                # with open(json_file_path2, 'w', encoding='utf-8') as file:
                                #     json.dump(data_list_2, file, ensure_ascii=False, indent=4)
                # 存储修改后的json文件
                with open(json_file_path2, 'w', encoding='utf-8') as file:
                    json.dump(data_list_2, file, ensure_ascii=False, indent=4)

