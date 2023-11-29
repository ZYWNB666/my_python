import os
import time

import requests
from flask import Flask, render_template
from flask import request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = 'your_secret_key'  # 设置会话的密钥，用于存储URL

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            api_url = f"https://cdn30.savetube.me/info?url={url}"
            response = requests.get(api_url)
            if response.status_code == 200:
                download_data = response.json()  # 解析JSON响应
                url_720p = None
                for video_format in download_data["data"]["video_formats"]:
                    if video_format["label"] == "720p":
                        url_720p = video_format["url"]
                        break

                if url_720p:
                    # 存储URL在会话中
                    session['download_url'] = url_720p
                    return redirect(url_for('index'))  # 重定向到当前页面
                else:
                    return "URL not found"
            else:
                return f"Failed to download URL. Status code: {response.status_code}"

    return render_template('index.html')



@app.route('/download')
def url_download():
    url = request.args.get('url')
    if url:
        api_url = f"https://cdn30.savetube.me/info?url={url}"
        response = requests.get(api_url)
        if response.status_code == 200:
            download_data = response.json()  # 解析JSON响应
            url_720p = None
            for video_format in download_data["data"]["video_formats"]:
                if video_format["label"] == "720p":
                    url_720p = video_format["url"]
                    break

            if url_720p:
                # 存储URL在会话中
                session['download_url'] = url_720p
                return redirect(url_for('index'))  # 重定向到当前页面
            else:
                return "URL not found"
        else:
            return f"Failed to download URL. Status code: {response.status_code}"
    return render_template('index.html')


@app.route('/cn_download', methods=['GET'])
def cn_download():
    url = request.args.get('url')
    if url:
        api_url = f"https://cdn30.savetube.me/info?url={url}"
        response = requests.get(api_url)
        if response.status_code == 200:
            download_data = response.json()
            url_720p = None

            for video_format in download_data["data"]["video_formats"]:
                if video_format["label"] == "720p":
                    url_720p = video_format["url"]
                    break

            if url_720p:
                download_folder = '/data/download/'

                # 创建下载文件夹，如果不存在
                if not os.path.exists(download_folder):
                    os.makedirs(download_folder)

                # 生成保存文件的路径
                current_time = time.strftime("%Y%m%d%H%M%S")
                file_name = f"{current_time}.mp4"
                file_path = os.path.join(download_folder, file_name)

                # 下载文件
                response = requests.get(url_720p)
                with open(file_path, 'wb') as file:
                    file.write(response.content)

                # 生成超链接
                link = f'http://oss.zywjjj.vip/youtube-download/download/{file_name}'

                return f"视频下载地址: {link}"
            else:
                return "No suitable download link found for 720p."
        else:
            return "Failed to fetch download information from the API."
    else:
        return "URL parameter is missing."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
