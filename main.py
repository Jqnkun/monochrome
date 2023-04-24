#!/usr/bin/env python3.9.16
# 必要なモジュールをインポート
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from image_processing import convert_to_grayscale

# ウィンドウを作成
window = Tk()
window.title("Image Converter")
window.geometry("600x400")

# 変換ボタンの処理
def convert_image():
    # ファイルを選択
    file_path = filedialog.askopenfilename()
    
    # 画像をモノクロに変換
    img = Image.open(file_path)
    grayscale_img = convert_to_grayscale(img)
    
    # 画像を表示
    tk_img = ImageTk.PhotoImage(grayscale_img)
    image_label.configure(image=tk_img)
    image_label.image = tk_img

# ラベルを作成してウィンドウに配置
label = Label(window, text="Click the button to select an image to convert")
label.pack(pady=10)

# ボタンを作成してウィンドウに配置
button = Button(window, text="Select Image", command=convert_image)
button.pack(pady=10)

# 画像を表示するためのラベルを作成してウィンドウに配置
image_label = Label(window)
image_label.pack(pady=10)

# イベントループを開始
window.mainloop()
