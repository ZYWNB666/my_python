import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, request, jsonify

app = Flask(__name__)

def send_email(to_email, subject, html_content):
    # SMTP 服务器和认证信息
    mail_server = "smtp.qq.com"
    port = 587  # 根据您的邮件服务器要求进行更改
    from_email = "ops-alarm@qq.com"
    password = "eaikqbptkxjsdjdi"

    # 创建邮件
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    # 创建 MIMEText 对象，并指定内容类型和字符集
    html_body = MIMEText(html_content, 'html', 'utf-8')
    message.attach(html_body)

    # 连接到 SMTP 服务器并发送邮件
    with smtplib.SMTP(mail_server, port) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())

@app.route('/', methods=['POST'])
def send_email_from_url():
    to_email = request.form.get('mail')
    subject = request.form.get('subject')
    html_content = request.form.get('html_content')

    if to_email and subject and html_content:
        send_email(to_email, subject, html_content)
        return jsonify({"message": "Email sent successfully"})
    else:
        return jsonify({"error": "Missing required parameters"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
