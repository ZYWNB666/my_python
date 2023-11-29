from flask import Flask, render_template

app = Flask(__name__)

# 指定要展示的文件路径
file_path = '/data/1.log'

@app.route('/')
def show_file():
    # 读取文件内容
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        file_content = "文件不存在"

    return render_template('file_viewer.html', file_content=file_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)

