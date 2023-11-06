import json
import re
import subprocess

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/serverip')
def serverip():
    command = "curl -s checkip.amazonaws.com | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}'"
    try:
        ip = subprocess.check_output(command, shell=True).decode('utf-8').strip()
        return f"服务端IP地址是: {ip}"
    except subprocess.CalledProcessError:
        return "Failed to fetch your public IP address."


@app.route('/')
def get_client_ip():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.remote_addr
    return f"{client_ip}\n"


def get_client_ip_info():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.remote_addr
    return f"{client_ip}"


@app.route('/ipinfo')
def get_ip_info():
    user_agent = request.user_agent.string
    apikey = "EXPBZ-X5DHM-YMO6C-6YBL5-AGA3S-ALBOL"
    ipv4_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    client_ip = request.args.get('ip')
    if not client_ip or (not ipv4_pattern.match(client_ip)):
        client_ip = get_client_ip_info()
    try:
        response = requests.get(f"https://apis.map.qq.com/ws/location/v1/ip?ip={client_ip}&key={apikey}")
        print(response.url)  # 打印请求的URL
        print(response.status_code)  # 打印状态码

        if response.status_code != 200:
            print(response.text)  # 打印响应内容
            return "您输入的IP不存在，请核查后再查询!"

        data = json.loads(response.text)

        # 提取所需字段，如果数据中没有'result'，则返回IP信息不可用
        result = ""
        if 'result' in data:
            ip = data['result']['ip']
            nation = data['result']['ad_info']['nation']
            province = data['result']['ad_info']['province']
            city = data['result']['ad_info']['city']
            district = data['result']['ad_info']['district']
            lat = data['result']['location']['lat']
            lng = data['result']['location']['lng']

            result = f"IP: {ip}\n国家: {nation}\n地址: {province}, {city}, {district}\n经纬度: {lat}, {lng}"

        if "Mozilla" in user_agent:
            result = result.replace('\n', '<br>')
        return result if result else "IP信息不可用"
    except subprocess.CalledProcessError:
        return "Failed to fetch IP information."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

