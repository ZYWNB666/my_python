import requests
from flask import Flask, request, render_template

app = Flask(__name__)


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
                    # 使用JavaScript在新标签页中打开URL
                    js_code = f'window.open("{url_720p}", "_blank");'
                    return f'<script>{js_code}</script>'
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
                # 使用JavaScript在新标签页中打开URL
                js_code = f'window.open("{url_720p}", "_blank");'
                return f'<script>{js_code}</script>'
            else:
                return "URL not found"
        else:
            return f"Failed to download URL. Status code: {response.status_code}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
