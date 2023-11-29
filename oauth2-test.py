import requests
from urllib.parse import urlencode

# Google OAuth2 配置信息
client_id = "316247377788-5uvdlq9525345k5ssb5dkra6btjn5r2m.apps.googleusercontent.com"
client_secret = "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"
redirect_uri = "https://grafana.netwebs.top:3000/login/google"
scope = "openid profile email"

# Google OAuth2 站点 URL
authorization_base_url = "https://accounts.google.com/o/oauth2/auth"
token_url = "https://accounts.google.com/o/oauth2/token"

# 用户需要访问的 URL，用于获取授权码
authorization_url = authorization_base_url + '?' + urlencode({
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'scope': scope,
    'response_type': 'code',
})

# 打印授权 URL，用户在浏览器中打开此 URL 来进行授权
print("请访问以下链接进行授权:")
print(authorization_url)

# 用户在浏览器中输入授权码
authorization_code = input("请输入授权码: ")

# 使用授权码获取访问令牌
token_data = {
    'code': authorization_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'grant_type': 'authorization_code',
}

response = requests.post(token_url, data=token_data)

# 打印获取的访问令牌信息
print("获取的访问令牌信息:")
print(response.json())
