import pytesseract as ocr
import numpy as np
import cv2

from PIL import Image

# tipando a leitura para os canais de ordem RGB
#imagem = Image.open('saoluis.jpeg').convert('RGB')
imagem = Image.open('a.png').convert('RGB')

# convertendo em um array editável de numpy[x, y, CANALS]
npimagem = np.asarray(imagem).astype(np.uint8)

# diminuição dos ruidos antes da binarização
npimagem[:, :, 0] = 0 # zerando o canal R (RED)
npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)

# atribuição em escala de cinza
im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)

kernel = np.ones((10, 10), np.uint8)
#roi = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
roi = cv2.threshold(im, 60, 255, cv2.THRESH_BINARY)[1]
roi = cv2.erode(roi, kernel, iterations=0)
cv2.imshow('ROI',roi)


# chamada ao tesseract OCR por meio de seu wrapper
phrase = ocr.image_to_string(roi, lang='por')


# aplicação da truncagem binária para a intensidade
# pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
# pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
# A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem

#ret, thresh = cv2.threshold(im, 0, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)

#ret, thresh = cv2.threshold(im, 100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#cv2.imshow("bin", thresh)
cv2.waitKey(0)


#kernel = np.ones((5, 5), np.uint8)
#roi = cv2.erode(thresh, kernel, iterations=0)


#th3 = cv2.adaptiveThreshold(thresh,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

# reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
#binimagem = Image.fromarray(thresh)
#binimagem = Image.fromarray(th3)

cv2.imwrite("graytest.jpg",roi)
#binimagem.show()


# impressão do resultado
print("antes de ler")
print(phrase)
print("cheguei aqui")