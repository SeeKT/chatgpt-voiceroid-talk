# chatgpt-voiceroid-talk
 
ChatGPTを使ってVoiceRoidと会話したいと思い、作りました。

## 動作環境
- Windows10 21H2
- Python 3.11.2
- AssistantSeika 20230319/c

## Usage
### (1) 依存関係のあるパッケージ等
- [AssistantSeika](https://hgotoh.jp/wiki/doku.php/documents/voiceroid/assistantseika/assistantseika-001a) を使っています。
- OpenAI の API を使っています。
- Pythonの依存関係は `requirements.txt` に書いています。

### (2) 実行環境の準備
#### (2-1) AssistantSeika の準備
[公式サイト](https://hgotoh.jp/wiki/doku.php/documents/voiceroid/assistantseika/assistantseika-001a) からダウンロードします。使い方については公式サイト参照。

#### (2-2) OpenAI の APIキーの取得
OpenAI の Webサイトで、Create new secret keys する。やり方については解説ブログ等参照。

#### (2-3) Python 環境
[公式サイト](https://www.python.org/downloads/) から Python をダウンロード。

[仮想環境](https://www.python.jp/install/windows/venv.html)の使用推奨。以降、PowerShellの場合を想定。

仮想環境の作成：

```
PS C:\> python -m venv [dir] 
```

仮想環境に入る：

(PowerShellの場合) 一度だけ以下コマンドを実行

```
PS C:\> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

```
PS C:\> [path to virtual env]\Scripts\activate.ps1
```

依存関係のインストール：

```
PS C:\> pip install -r requirements.txt
```

### (3) 実行方法

```
PS C:\> python talk_with_voiceroid.py [API key] [Path of SeikaSay2.exe]
```

API key と exe ファイルのパスは、環境変数として追加しておくと楽です。

## References
- [ChatGPTのAPIをPythonから使う](https://fuji-pocketbook.net/chatgpt-api-python/)
- [ChatGPT+Pythonでボイスロイドとリアルタイムで音声会話できるプログラムを作った](https://zenn.dev/akashixi/articles/303dd79264e1ff)
- [AssistantSeika の使用例](https://hgotoh.jp/wiki/doku.php/documents/voiceroid/assistantseika/assistantseika-001)