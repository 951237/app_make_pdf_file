'''
파일 업로드 참고 : https://niceman.tistory.com/150
'''

from flask import Flask, request, render_template
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1', port=5000)