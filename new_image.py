import pytesseract as ocr
import numpy as np
import cv2
from gtts import gTTS
from playsound import playsound

#p_img = 'medida.png'
p_img = 'cu.png'
img_temp = cv2.imread(p_img, 1)


cv2.imshow("npimagem", img_temp)
cv2.waitKey(0)

im = cv2.cvtColor(img_temp, cv2.COLOR_RGB2GRAY)
cv2.imshow('im', im)
cv2.waitKey(0)

roi = cv2.threshold(im, 165, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('roi', roi)
cv2.waitKey(0)

kernel = np.ones((3, 3), np.uint8)

teste = cv2.erode(roi, kernel, iterations=1)
cv2.imshow('teste', teste)
cv2.waitKey(0)

# chamada ao tesseract OCR por meio de seu wrapper
phrase = ocr.image_to_string(roi,  config="-psm 100 -c tessedit_char_whitelist=0123456789.m")

# impressão do resultado
print(phrase)


#Funcao responsavel por falar
def cria_audio(audio):

    tts = gTTS(audio,lang='pt-br')

    #Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('hello.mp3')


cria_audio(phrase)