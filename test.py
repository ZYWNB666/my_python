# import json
#
# import requests
#
# apikey = "EXPBZ-X5DHM-YMO6C-6YBL5-AGA3S-ALBOL"
#
# # response = requests.get("https://opendata.baidu.com/api.php?query=192.6.66.6&co=&resource_id=6006&oe=utf8")
# response = requests.get(f"https://apis.map.qq.com/ws/location/v1/ip?ip=111.206.145.41&key={apikey}")
# data = json.loads(response.text)
# # print(data)
# # 提取所需字段
# ip = data['result']['ip']
# nation = data['result']['ad_info']['nation']
# province = data['result']['ad_info']['province']
# city = data['result']['ad_info']['city']
# district = data['result']['ad_info']['district']
# lat = data['result']['location']['lat']
# lng = data['result']['location']['lng']
# print("IP:", ip)
# print("国家:", nation)
# print("地址:", province,city,district)
# print("经纬度:", lat, lng)


from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def check_browser_and_os():
    user_agent = request.user_agent.string

    # 判断是否是浏览器和操作系统
    if "Mozilla" in user_agent:
        return "这是一个 Windows 操作系统的浏览器访问"


if __name__ == '__main__':
    app.run()
