from time import sleep
from termcolor import colored
from colorama import init

init()

texto = "Esto es un ejemplo del letrero con colores en verde."

for letra in texto:
    print(colored(letra, 'green', attrs=['blink', 'bold', 'underline']),end=" ")
    sleep(.5)