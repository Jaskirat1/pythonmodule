import cv2
import pytesseract


image = cv2.imread(r"C:\Users\lenovo pc\Desktop\data.png",1)
print(image)

print("***********")

text = pytesseract.image_to_string(image)
print(text)