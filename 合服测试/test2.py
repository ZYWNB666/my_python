import os

json_save = "C:\\Users\\user\\Desktop\\合服\\json\\"
if not os.path.exists(json_save):
    try:
        os.makedirs(json_save, exist_ok=True)
        print(f"目录 {json_save} 创建成功")
    except Exception as e:
        print(f"目录 {json_save} 创建失败，错误信息：{e}")
