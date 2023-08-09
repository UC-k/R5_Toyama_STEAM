
```python
# import文でtkinterをtkとして扱うと宣言
import tkinter as tk
# ------------------------------------------------------------------------------
def deleteA():
    cvs.delete("A")
def deleteB():
    cvs.delete("B")
def deleteAll():
    cvs.delete("all")
def revival():
    cvs.create_text(10, 10, text="テキストテキストテキスト\n改行してテキスト", fill="blue",
                font=("System", 20), anchor="nw", tag="A")
    cvs.create_line(10, 100, 300, 150, fill="blue", width=2, tag="A")
    cvs.create_line(30, 200, 300, 250, 30, 400, 30, 200,
                fill="blue", width=5, tag="A")
    cvs.create_rectangle(500, 10, 700, 100, fill="grey",
                    outline="red", width=2, tag="B")
    cvs.create_oval(500, 200, 700, 400, fill="grey", outline="red",
                    width=4, tag="B")
# ------------------------------------------------------------------------------
root = tk.Tk()
cvs = tk.Canvas(root, width=800, height=600, bg="white")
cvs.pack()
# ------------------------------------------------------------------------------
btnA = tk.Button(root, text='「A」のみ削除', fg="blue",
                highlightbackground="white", command=deleteA)
btnB = tk.Button(root, text='「B」のみ削除', fg="red",
                highlightbackground="white", command=deleteB)
btnC = tk.Button(root, text='すべて削除',
                highlightbackground="white", command=deleteAll)
btnD = tk.Button(root, text="すべて復活",
                highlightbackground="white", command=revival)
btnA.place(x=100, y=550, anchor="c")
btnB.place(x=300, y=550, anchor="c")
btnC.place(x=500, y=550, anchor="c")
btnD.place(x=700, y=550, anchor="c")
# ------------------------------------------------------------------------------
# テキスト（x, y, text, color, font, anchor, tag）
cvs.create_text(10, 10, text="テキストテキストテキスト\n改行してテキスト", fill="blue",
                font=("System", 20), anchor="nw", tag="A")
# 線（x1, y1, x2, y2, color, 線幅, tag）
cvs.create_line(10, 100, 300, 150, fill="blue", width=2, tag="A")
# 三角形（x1, y1, x2, y2, x3, y3, x1, y1, color, 線幅, tag）
cvs.create_line(30, 200, 300, 250, 30, 400, 30, 200,
                fill="blue", width=5, tag="A")
# 矩形（x, y, x+width, y+height, 内側の色, 外線の色, 線幅, tag）
cvs.create_rectangle(500, 10, 700, 100, fill="grey",
                    outline="red", width=2, tag="B")
# 楕円（中心(x)-半径(r), 中心(y)-半径(r), x+r, y+r, 内側の色, 外側の色, 線幅, tag）
cvs.create_oval(500, 200, 700, 400, fill="grey", outline="red",
                    width=4, tag="B")
# ------------------------------------------------------------------------------
root.mainloop()
```

```python
import tkinter as tk
import math
# ------------------------------------------------------------------------------
bar1 = 0
bar2 = 0
load = 0
# ------------------------------------------------------------------------------
def start():
    global bar1, bar2, load
    # ロード中のサークル描画
    cvs.create_arc(100, 100, 500, 500, width=8, style=tk.ARC, outline="#01FACA",
            start=90, extent=bar1, tag="load")
    cvs.create_arc(100, 100, 500, 500, width=8, style=tk.ARC, outline="#01FACA",
            start=270, extent=bar2, tag="load")
    cvs.update()
    # 中心にパーセントを表示
    if load < 100:
        load += 1.38
    elif load > 100:
        load = 100
    load_txt.config(text=str(math.floor(load))+"%")
    # 円を徐々に描写
    if bar2 >= -180:
        if bar1 >= -180:
            bar1 -= 5
        elif bar1 < -180:
            bar2 -= 5
        root.after(1, start)
# ------------------------------------------------------------------------------
root = tk.Tk()
root.title("Python習熟度診断アプリ")
root.geometry("600x600+300+100")
root.resizable(False, False)
# ------------------------------------------------------------------------------
cvs = tk.Canvas(root, width=600, height=600, bg="#323232")
cvs.pack()
# ------------------------------------------------------------------------------
load_txt = tk.Label(text="0%", font=("DSEG7 Classic", 30),
                    fg="#01FACA", bg="#323232")
load_txt.place(x=300, y=300, anchor="c")

start()
root.mainloop()
```

