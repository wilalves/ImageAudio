import pytesseract as ocr
import numpy as np
import cv2
from gtts import gTTS
from playsound import playsound

from PIL import Image

# tipando a leitura para os canais de ordem RGB
#imagem = Image.open('saoluis.jpeg').convert('RGB')
imagem = Image.open('aa.jpeg').convert('RGB')

# convertendo em um array editável de numpy[x, y, CANALS]
npimagem = np.asarray(imagem).astype(np.uint8)  

# diminuição dos ruidos antes da binarização
npimagem[:, :, 0] = 0 # zerando o canal R (RED)
npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)

# atribuição em escala de cinza
im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY) 

# aplicação da truncagem binária para a intensidade
# pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
# pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
# A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem

#ret, thresh = cv2.threshold(im, 0, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)

ret, thresh = cv2.threshold(im, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("bin", thresh)
#cv2.waitKey(0)

th3 = cv2.adaptiveThreshold(thresh,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

# reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
#binimagem = Image.fromarray(thresh) 
binimagem = Image.fromarray(th3)

#cv2.imwrite('graytest.jpg',binimagem)
binimagem.show()

# chamada ao tesseract OCR por meio de seu wrapper
phrase = ocr.image_to_string(binimagem,  config="-psm 100 -c tessedit_char_whitelist=.0123456789")

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