from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'XXXX'
@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    print(data)
    text = data['text']
    # summary = text
    summary = generate_summary(text)
    return jsonify({'summary': summary})


def generate_summary(text):
    # 要約を3点で出力するように調整
    prompt ='''
    Tl;dr
    以下の形式になるように文章を要約してください
    ポイントは以下の3点です。
    '''
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= prompt + text,
        max_tokens=500,
        temperature=0.7,
        frequency_penalty=1.0,
    )
    summary = response.choices[0].text.strip()
    return summary

if __name__ == '__main__':
    app.run(debug=True)
