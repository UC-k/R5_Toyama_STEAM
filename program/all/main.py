import tkinter as tk

# --------------------------------------------------

root = tk.Tk()
root.title("診断アプリ")
root.geometry("900x700+100+20")
root.resizable(False, False)

# --------------------------------------------------

cvs = tk.Canvas(root, width=900, height=700)
cvs.pack()

# --------------------------------------------------

bool_var  = [None]*8
check_btn = [None]*8
question_list = []

ITEM = [
    "1つ目の質問",
    "2つ目の質問",
    "3つ目の質問",
    "4つ目の質問",
    "5つ目の質問",
    "6つ目の質問",
    "7つ目の質問",
    "8つ目の質問"
]

RESULT = [
    "チェックの数が0個のときの\n結果を表示する",
    "チェックの数が1個のときの\n結果を表示する",
    "チェックの数が2個のときの\n結果を表示する",
    "チェックの数が3個のときの\n結果を表示する",
    "チェックの数が4個のときの\n結果を表示する",
    "チェックの数が5個のときの\n結果を表示する",
    "チェックの数が6個のときの\n結果を表示する",
    "チェックの数が7個のときの\n結果を表示する",
    "チェックの数が8個のときの\n結果を表示する"
]

# --------------------------------------------------

def result_scene():
    cnt = 0
    for i in range(8):
        if bool_var[i].get():
            cnt += 1

    for i in range(8):
        check_btn[i].place_forget()
        question_list[i].place_forget()
    result_btn.place_forget()

    result_label = tk.Label(text=RESULT[cnt],
                            fg="white", bg="#323232",
                            font=("游ゴシック体", 20)
                            )
    result_label.place(x=900/2, y=700/2, anchor="c")

# --------------------------------------------------

for i in range(8):
    # チェックボタン
    bool_var[i] = tk.BooleanVar()
    bool_var[i].set(False)
    check_btn[i] = tk.Checkbutton(fg="white", bg="#323232",
                                  variable=bool_var[i]
                                )
    check_btn[i].place(x=200, y=80+60*i, anchor="nw")
    # チェックボタン横に配置するテキスト（ITEM）
    question_label = tk.Label(text=ITEM[i], 
                     fg="white", bg="#323232",
                     font=("游ゴシック体", 20)
                     )
    question_list.append(question_label)
    question_label.place(x=230, y=68+60*i, anchor="nw")

# 結果画面に移行するための画面
result_btn = tk.Button(text="結果へ", cursor="pointinghand",
                        command=result_scene
                       )
result_btn.place(x=600, y=400, anchor="nw")


# --------------------------------------------------

root.mainloop()


# - リスト（配列）
# - 関数
# - for文（繰り返し文）
# - if文（条件分岐）
# - tkinter（ウィンドウ、キャンバス、ボタン、チェックボタン、ラベル）
# - 画像