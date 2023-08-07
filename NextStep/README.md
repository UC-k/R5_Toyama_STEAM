# テキストの入力
tkinterにおいて、ユーザがテキスト入力を行うことができるテキスト入力欄のオブジェクトを作成する際、「Entry」という1行の入力欄、または「Text」という複数行の入力欄がある。

# １行のテキスト入力欄について（Entry）
tkinter.Entryを使用して、１行のテキスト入力欄を作成してみましょう。
```python
import tkinter as tk
```
`プログラムの説明`<br>
1. <br>
2. <br>


# 複数行のテキスト入力欄について（Text）
tkinter.Textを使用して、複数行のテキスト入力欄を作成してみましょう。
```python
import tkinter as tk
```
`プログラムの説明`<br>
1. <br>
2. <br>


# テキストの一部の色を変更する
0-0. ではtkinterにおいて、tkinter.Labelを用いてテキストを配置しました。<br>
しかし、Labelでは、テキストの一部のみ色を変更することはできません。（テキスト全体はできる。）<br>
そこで、テキストの一部のみ色を変更したい場合は、EntryまたはTextを使用します。<br>
.tag_configure()を使用して、自分の好きな色に指定してみましょう。
```python
import tkinter as tk
```
`プログラムの説明`<br>
1. <br>
2. <br>

`解説`<br>
1. .insert("1.0","〇〇〇〇")テキスト<br>
2. <br>
