from tkinter import *
from image_processing import convert_to_grayscale

def create_gui():
    # ウィンドウを作成する
    root = Tk()
    root.title("Image Converter")
    
    # ラベルを作成する
    label = Label(root, text="Select an image to convert to grayscale:")
    label.pack()
    
    # ボタンを作成する
    button = Button(root, text="Select Image", command=select_image)
    button.pack()
    
    # メインループを開始する
    root.mainloop()

def select_image():
    # ファイルダイアログを表示する
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    
    # 画像を変換する
    convert_to_grayscale(file_path)
    
    # ダイアログを表示する
    messagebox.showinfo("Conversion Complete", "The image has been converted to grayscale.")

if __name__ == "__main__":
    create_gui()
