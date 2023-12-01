import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
root_path = 'C:/Users/dell/PycharmProjects/pythonProject6/uploads'
folder_path = os.path.abspath(root_path)
@app.route('/')
def welcome1():
    return render_template('2222.html')
@app.route('/1')
def welcome2():
    return render_template('1.html')
@app.route('/a')
def a():
    return render_template('1.html')
@app.route('/b')
def b():
    return render_template('2222.html')
@app.route('/Answer_home_page')
def welcome3():
    return render_template('Answer_home_page.html')
@app.route('/c')
def c():
    return render_template('Answer_home_page.html')
@app.route('/Answer')
def welcome4():
    return render_template('Answer.html')
@app.route('/d')
def d():
    return render_template('Answer.html')
@app.route('/QAQ')
def welcome5():
    return render_template('QAQ.html')
@app.route('/e')
def e():
    return render_template('QAQ.html')
@app.route('/show_file_list')
def show_file_list():
    file_list = os.listdir(folder_path)
    return render_template('file_list.html', files=file_list)

@app.route('/delete_files', methods=['POST'])
def delete_files():
    # 解析请求数据
    data = request.get_json()
    folder_path = data.get('folderPath', '')
    if folder_path:
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        response = {'message': '文件删除成功'}
    else:
        response = {'message': '未提供文件夹路径'}

    return jsonify(response)
@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('show_file_list'))
@app.route('/download/<path:filename>')
def download_file(filename):
    file_path = os.path.join(folder_path, filename)
    return send_file(file_path, as_attachment=True)
if __name__ == '__main__':
    app.run()