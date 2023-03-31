# chatgpt-voiceroid-talk
 
ChatGPTを使ってVOICEROIDと会話したいと思い、作りました。

機能追加：VOICEVOX version も作成しました。

## 動作確認環境
- Windows10 21H2
- Python (>3.10)
- AssistantSeika 20230319/c
- VOICEVOX
- [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/ja/visual-cpp-build-tools/)

## Usage
### (1) 依存関係のあるパッケージ等
- [AssistantSeika](https://hgotoh.jp/wiki/doku.php/documents/voiceroid/assistantseika/assistantseika-001a) を使っています。
- OpenAI の API を使っています。
- Pythonの依存関係は `requirements.txt` に書いています。
  - `simpleaudio` のインストールに Microsoft C++ Build Tools が必要です。

### (2) 実行環境の準備
#### (2-1) AssistantSeika の準備 (VOICEROID version)
[公式サイト](https://hgotoh.jp/wiki/doku.php/documents/voiceroid/assistantseika/assistantseika-001a) からダウンロードします。使い方については公式サイト参照。

#### (2-1) VOICEVOX の準備 (VOICEVOX version)
[公式サイト](https://voicevox.hiroshiba.jp/) または [GitHubリポジトリ](https://github.com/VOICEVOX/voicevox_engine/releases) からダウンロードします。

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
VOICEROID version と VOICEVOX version があります。

VOICEROID version の実行方法：

```
usage: talk_with_voiceroid.py [-h] [-l HISTORY] [-c CID] api_key exe_path

Talk with VOICEROID

positional arguments:
  api_key               OpenAI API key
  exe_path              the path of exe file

options:
  -h, --help            show this help message and exit
  -l HISTORY, --history HISTORY
                        the path of chat history file
  -c CID, --cid CID     the cid of VOICEROID Software
```

VOICEVOX version の実行方法：

```
usage: talk_with_voicevox.py [-h] [-l HISTORY] [-s SPEAKER] [-r RETRY] api_key

Talk with VOICEROID

positional arguments:
  api_key               OpenAI API key

options:
  -h, --help            show this help message and exit
  -l HISTORY, --history HISTORY
                        the path of chat history file
  -s SPEAKER, --speaker SPEAKER
                        the speaker id of the VOICEVOX character
  -r RETRY, --retry RETRY
                        maximum limit of retry
```

API key や exe ファイルのパスは、環境変数として追加しておくと楽です。

### (4) 終了方法
「終わります」と話したら処理が終了します。

## デモ動画 (VOICEROID version)
[![](https://img.youtube.com/vi/PZ-GPs_KCm0/0.jpg)](https://www.youtube.com/watch?v=PZ-GPs_KCm0)

## References
- [ChatGPTのAPIをPythonから使う](https://fuji-pocketbook.net/chatgpt-api-python/)
- [ChatGPT+Pythonでボイスロイドとリアルタイムで音声会話できるプログラムを作った](https://zenn.dev/akashixi/articles/303dd79264e1ff)
- [AssistantSeika の使用例](https://hgotoh.jp/wiki/doku.php/documents/voiceroid/assistantseika/assistantseika-001)
- [AI Tuberで使えそうなVoiceVox × Pythonコードを貼っておくだけ。](https://note.com/mega_gorilla/n/n8cec1ce5ccaa)