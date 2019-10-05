import cv2
import numpy as np
import pytesseract as ocr
from gtts import gTTS
from playsound import playsound

###############################################################
### Imagery
###############################################################
def initialize_images():
  p_img = 'hj.jpeg'
  img_temp = cv2.imread(p_img, 1)
  img = img_temp.copy()
  return img, img_temp, None

def define_rectangle(iy, ix, y, x):
  x_sorted = sorted([ix, x])
  y_sorted = sorted([iy, y])
  return (x_sorted[0], y_sorted[0]), (x_sorted[1], y_sorted[1])


def cria_audio(audio):

    tts = gTTS(audio,lang='pt-br')

    #Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('hello.mp3')


if __name__ == '__main__':

    img_temp, img, roi = initialize_images()

    #kernel = np.ones((2, 2), np.uint8)
    roi = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY)
    roi = cv2.threshold(img_temp, 100, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('ROI', roi)
    cv2.waitKey(0)

    # Blue color in BGR
    color = (255, 0, 0)

    thickness = 0

    crop_img = roi[277:277 + 55, 400:400 + 105]
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)
    # Blending the images with 0.3 and 0.7
    height, width = (508, 720)

    blank_image = np.zeros((height, width, 3), np.uint8)
    blank_image[:, 0:width] = (255, 255, 255)  # (B, G, R)

    x_offset = int((width - crop_img.shape[1]) / 2)
    y_offset = int((height - crop_img.shape[0]) / 2)

    blank_image[y_offset:y_offset + crop_img.shape[0], x_offset:x_offset + crop_img.shape[1]] = crop_img

    kernel = np.ones((2, 2), np.uint8)
    teste = cv2.erode(crop_img, kernel, iterations=1)

    cv2.imshow("white", teste)

    # chamada ao tesseract OCR por meio de seu wrapper
    frase = ocr.image_to_string(teste, config="-psm 100 -c tessedit_char_whitelist=.0123456789")

    # impressão do resultado
    print(frase)

    cria_audio(frase)

    cv2.waitKey(0)