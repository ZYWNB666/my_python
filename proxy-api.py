import requests
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def proxy_root():
    target_url = 'https://api.openai.com'
    url = f'{target_url}{request.full_path}'

    if request.method == 'OPTIONS':
        # Handle preflight CORS requests
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        }
        return Response('', status=200, headers=headers)

    response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False
    )

    headers = {
        key: value for (key, value) in response.headers.items()
    }

    if 'Access-Control-Allow-Origin' not in headers:
        headers['Access-Control-Allow-Origin'] = '*'
    return Response(response.content, response.status_code, headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
