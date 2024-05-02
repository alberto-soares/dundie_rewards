# Outra forma importando so os objetos desejados

"""Modulo xyz"""

from modulo1 import say_hi, NOME # Procura modulo1.py no mesmo diretorio

def say_hello(n):
    print(f"Hello {n}")

say_hi(NOME) # Hi Alberto

say_hello(NOME) # Hello Alberto

