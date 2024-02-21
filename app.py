from flask import Flask, request, render_template, jsonify, send_file
import requests
import PyPDF2
from pptx import Presentation
import io

app = Flask(__name__, static_url_path='/static')

# ルートURLへのリクエストに対する処理
@app.route('/')
def home():
    return render_template('index.html')

# アップロードされたPDFファイルのテキスト抽出とサマリーの取得
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['pdf']
    text = extract_text_from_pdf(file)
    # PDFファイルから抽出したテキストを別のサーバーに送信し、その結果を取得
    summary = send_text_to_server(text)
    print(summary)
    return render_template('index.html', summary=summary)


# PDFファイルからテキストを抽出する関数
def extract_text_from_pdf(file, num_lines=100):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ''
    line_count = 0
    for page in range(pdf_reader.numPages):
        if line_count >= num_lines:
            break
        page_text = pdf_reader.getPage(page).extractText()
        lines = page_text.split('\n')
        for line in lines:
            if line.strip():
                text += line + '\n'
                line_count += 1
                if line_count >= num_lines:
                    break
    return text.strip()

# テキストを別のサーバーに送信してサマリーを取得する関数
def send_text_to_server(text):
    url = 'http://127.0.0.1:5000/summarize'
    data = {'text': text}
    response = requests.post(url, json=data)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True, port=8080)
