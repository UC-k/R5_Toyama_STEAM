import tkinter as tk

# ----------------------------------------
# 1.画面の作成
# 1-1.画面の作成
root = tk.Tk()
# 1-2.タイトルを作成
root.title("○○診断")
# 1-3.画面の大きさを指定
root.geometry("900x700")
# 1-4.画面を拡大・縮小できないように設定
root.resizable(False, False)


# 2.キャンバスの作成・配置
# 2-1.キャンバスを定義
cvs = tk.Canvas(root, width=900, height=700)
# 2-2.キャンバスを配置
cvs.pack()


# 3.キャンバスに画像を配置
# 3-1.使用する画像を定義
img = tk.PhotoImage(file="./image.png")
# 3-2.画像をキャンバスに配置
cvs.create_image(0, 0, anchor="nw", image=img, tag="start_image")


# 4.画面にタイトル（テキスト）を作成・配置
# 4-1.ラベル（テキスト）を定義
title_label = tk.Label(text="○○診断",
                       fg="white", bg="#8dcdbe",
                       font=("游ゴシック", 50)
                       )
# 4-2.ラベル（テキスト）を配置
title_label.place(x=450, y=300, anchor="c")


# 5.診断画面へ移行するためのボタンを作成・配置
# 5-1.ボタンを押した際に実行される関数
def toShindan():
    # 5-1-1.キャンバスに配置した画像を取り除く（任意）
    # cvs.delete("start_image")
    # 5-1-2.画面に配置したラベルやボタンを取り除く
    title_label.place_forget()
    toShindan_btn.place_forget()
    # 5-1-3.診断画面を形成する関数へ
    shindan()
# 5-2.ボタンの作成・配置
# 5-2-1.ボタンを定義
toShindan_btn = tk.Button(text="診断へ",
                          cursor="hand2",
                          fg="black", highlightbackground="#8dcdbe",
                          command=toShindan)
# 5-2-2.ボタンを配置
toShindan_btn.place(x=700, y=550, anchor="nw")


# ----------------------------------------
# 6.診断項目の準備
# 6-1.診断項目の数だけチェックボタンを作成するためのリストを作成
check_btn = [None]*8
# 6-2.チェックボタンがチェックされているかどうかを判断するリストを作成
bool_var  = [None]*8
# 6-3.診断項目（ラベル）を入れるための空のリストを用意（7-1-6で利用）
question_list = []
# 6-4.診断項目の内容を入れたリストを作成
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
# 6-5.チェックの数に応じて表示する診断結果を入れたリストを作成
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


# 7.診断画面を形成する関数
def shindan():
    # 7-1.チェックボタンの作成・配置
    for i in range(8):
        # 7-1-1.チェックボタンの判定を「True」「False」に設定
        bool_var[i] = tk.BooleanVar()
        # 7-1-2.はじめは全て「False」（チェックがついていない状態）にセット
        bool_var[i].set(False)
        # 7-1-3.チェックボタンを作成
        check_btn[i] = tk.Checkbutton(fg="red", bg="#8dcdbe",
                                      variable=bool_var[i]
                                      )
        # 7-1-4.チェックボタンを配置
        check_btn[i].place(x=200, y=80+60*i, anchor="nw")
        # 7-1-5.チェックボタンの横に表示する診断項目（ラベル）を定義
        question_label = tk.Label(text=ITEM[i],
                                  fg="white", bg="#8dcdbe",
                                  font=("游ゴシック", 30)
                                  )
        # 7-1-6.診断項目（ラベル）をリストにまとめる（8-1-2で削除する際に利用）
        question_list.append(question_label)
        # 診断項目（ラベル）を配置
        question_label.place(x=230, y=68+60*i, anchor="nw")
    # 7-2.結果画面へ移行するためのボタンを配置(8を参照)
    set_resultBtn()

# 8.結果画面へ移行するためのボタンを作成・配置
# 8-1.ボタンを押した際に実行される関数
def toResult():
    # again_btn,quit_btn,result_lavelは関数外で使用するためグローバル化
    global again_btn, quit_btn, result_label
    # 8-1-1.チェックボタンの「True」（チェックされている）数を調べる
    count = 0
    for i in range(8):
        if bool_var[i].get():
            count += 1
    # 8-1-2.画面に配置したチェックボタン、ラベル、ボタンを取り除く
    for i in range(8):
        check_btn[i].place_forget()
        question_list[i].place_forget()
        result_btn.place_forget()
    # 診断結果を表示するラベルの作成
    result_label = tk.Label(text=RESULT[count],
                            fg="white", bg="#8dcdbe",
                            font=("游ゴシック", 40)
                            )
    # 診断結果を表示するラベルを配置
    result_label.place(x=900/2, y=700/2, anchor="c")
    # 診断結果後、もう一度やるか終了するかのボタンを作成
    again_btn = tk.Button(text="もう一度", cursor="hand2",
                          fg="black", highlightbackground="#8dcdbe",
                          command=again) # 9-1を参照
    quit_btn  = tk.Button(text="終了する", cursor="hand2",
                          fg="black", highlightbackground="#8dcdbe",
                          command=end) # 9-2を参照
    # ↑のボタンを配置
    again_btn.place(x=700, y=550, anchor="nw")
    quit_btn.place(x=800, y=550, anchor="nw")
# 8-2.ボタンの作成・配置
# 8-2-1.ボタンを定義
result_btn = tk.Button(text="結果へ", cursor="hand2",
                       fg="black", highlightbackground="#8dcdbe",
                        command=toResult # 8-1を参照
                       )
# 8-2-2.ボタンを配置
def set_resultBtn():
    result_btn.place(x=600, y=400, anchor="nw")

# 9.もう一度するか終了するかを選択するボタン
# 9-1.「もう一度」ボタンの作成
def again():
    # 9-1-1.画面に配置したボタンやラベルを取り除く
    again_btn.place_forget()
    quit_btn.place_forget()
    result_label.place_forget()
    # 9-1-2.診断項目（リスト）の初期化
    question_list.clear()
    # 9-1-3.診断画面へ
    toShindan()
# 9-2.「終了する」ボタンの作成
def end():
    root.destroy()

# ----------------------------------------
# 10.メインループ
root.mainloop()