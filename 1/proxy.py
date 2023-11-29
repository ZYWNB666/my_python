import socketserver
import urllib.request
from http.server import SimpleHTTPRequestHandler

class ThreadedProxyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        target_url = "https://ai.netwebs.top" + self.path

        try:
            # 发送 GET 请求到目标 URL
            response = urllib.request.urlopen(target_url)

            # 获取目标服务器的响应
            content = response.read()

            # 设置响应头
            self.send_response(response.status)
            self.send_header("Content-type", response.headers.get("Content-type"))
            self.end_headers()

            # 将目标服务器的响应发送给客户端
            self.wfile.write(content)
        except Exception as e:
            # 处理异常，例如网络错误
            self.send_error(500, f"Proxy error: {str(e)}")

# 选择一个端口（例如 8080）
port = 8080

# 创建支持多线程的代理服务器
with socketserver.ThreadingTCPServer(("0.0.0.0", port), ThreadedProxyHandler) as httpd:
    print(f"Threaded proxy server is running on port {port}")
    httpd.serve_forever()
