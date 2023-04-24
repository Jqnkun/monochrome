# from PIL import Image
def convert_to_grayscale(file_path):
    # 画像を開く
    image = Image.open(file_path)
    
    # モノクロに変換する
    grayscale_image = image.convert('L')
    
    # 変換した画像を保存する
    grayscale_image.save(file_path)
