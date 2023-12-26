# 設計詳細

## ユーザーゴール
論文の内容を要約し、パワーポイントにしてダウンロードできる。

## 機能要件
- 論文の内容を入力できる。
- 論文の要約をパワーポイントでダウンロードできる。


## シーケンス図の詳細
1. ブラウザに論文を入力(pdf)
2. ブラウザからサーバーに論文の内容が渡される
3. サーバーがpdfから文字を起こす。
4. サーバーからOpenAIサーバーでChatGPTに要約させる
5. OpenAIサーバーからの返り値をServerで受け取り、パワーポイントを作成
6. 作成したパワーポイントを出力


###　追加
パワーポイントで出力した内容を修正したい。
履歴を取る。
Firebaseで認証を簡単にやってくれる. Flask*Firebase
Flask: https://qiita.com/usaitoen/items/0184973e9de0ea9011ed


## シーケンス

```mermaid
sequenceDiagram
    participant User as Client
    participant Browser as Browser
    participant Server as Server
    participant OpenAI as OpenAIsever

    User ->> Browser: 論文情報入力
    Browser ->> Server: 論文情報を取得
    Server ->> OpenAI: 論文の文章を送信
    OpenAI ->> Server: 論文を要約した内容を取得
    Server ->> Browser: 要約内容をpptx化
    Browser ->> User: pptxファイルを取得
```

## 状態遷移図
