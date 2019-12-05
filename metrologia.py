import pytesseract as ocr
import numpy as np
import cv2
from gtts import gTTS
from playsound import playsound

choice = 0

def menu():
    print(30 * '-')
    print("   M E N U")
    print(30 * '-')
    print("1. ler imagem")
    print("2. finalizar programa")
    print(30 * '-')

    ## Get input ###
    choice = input('Enter your choice [1-2] : ')

    ### Convert string to int type ##
    choice = int(choice)

    return choice


#Funcao responsavel por falar
def cria_audio(audio):

    tts = gTTS(audio,lang='pt-br')

    #Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('hello.mp3')

    #cv2.waitKey(0)



while (choice != 2):
    choice = menu()
    if choice == 1:
        image = input('Digite o nome da imagem: ')
        img_temp = cv2.imread(image, 1)
        cv2.imshow("lari", img_temp)

        im = cv2.cvtColor(img_temp, cv2.COLOR_RGB2GRAY)
        cv2.imshow('im', im)

        roi = cv2.threshold(im, 165, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow('roi', roi)

        kernel = np.ones((3, 3), np.uint8)

        teste = cv2.erode(roi, kernel, iterations=1)
        cv2.imshow('teste', teste)

        # chamada ao tesseract OCR por meio de seu wrapper
        phrase = ocr.image_to_string(roi, config="-psm 100 -c tessedit_char_whitelist=0123456789.m")

        cria_audio(phrase)

        cv2.destroyAllWindows()







