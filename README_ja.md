# pyfiledb

## ファイルにシンプルな印
毎日の仕事の中で、ファイルを探すことに躍起になっていないですか？
わたしはその1人です。
このpyfiledbは、YouTubeやInstagramの用に
fileのpathに対して、任意のハッシュタグをつけることで、
ハッシュタグ検索することができます。
また、API,CLI、GUIの3つのインターフェースを持っており、
それら全てが完全フリーで配布しております。(MITライセンス)

## APIの使用
pyfiledbをinstallします。
```bash
>python setup.py install
```

appendでファイル情報が追加され、searchでハッシュ検索ができます。
```python
>>> from pyfiledb import pyfiledb
>>> filedb = pyfiledb()
>>> filedb.append('xxx/yyy/zzz.txt', '#hash1#hash2')
>>> filedb.search('#hash2')
{'xxx/yyy/zzz.txt': '#hash1#hash2'}
>>> filedb.close()
```

## CLIの使用
pyfiledbをinstallします。
```bash
>python setup.py install
```

appendでファイル情報を追加します。
```bash
> pyfiledb-cli add
path: xxx/yyy/zzz.txt  
hashs: #hash1#hash2
```

searchでハッシュ検索をします
```bash
> pyfiledb-cli search
hashs: #hash1 
-[0]-------------
path: xxx/yyy/zzz.txt
hashs: #hash1#hash2
```

## GUIの使用
kivyをインストールします。
```bash
>pip install kivy
```

GUIアプリを起動は、次のコードです。
```bash
>python -m pyfiledb.gui
```


## 今後の改善
* 登録したファイルのプロファイルを削除する機能
* CLIとGUIのAhead-Of-Timeコンパイル
* 探索アルゴリズムの最適化
* with文のサポート
