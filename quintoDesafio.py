'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''
def inversor(texto):
  return texto[::-1]

usrInput = input("Escreva: ")

invertido = inversor(usrInput)

print(invertido)