from PIL import Image
import pytesseract

def convert_img(img,threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img

captcha = Image.open("11.jpg")
r = convert_img(captcha,150)
result = pytesseract.image_to_string(r)
print(result)
