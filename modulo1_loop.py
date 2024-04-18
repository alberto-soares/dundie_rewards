# Python e uma linguagem interpretada

import modulo2 # modulo1 chama modulo2   LOOP

NOME = "Alberto"

def say_hi(n):
    print(f"Hi {n}") # Hi Alberto


modulo2.say_hello(NOME)

#############
# RESULTADO #
#############
#Traceback (most recent call last):
# File "/Users/albertosoares/Projetos/dundie_rewards/modulo1.py", 
# line 3, in <module> import modulo2
# File "/Users/albertosoares/Projetos/dundie_rewards/modulo2.py", 
# line 1, in <module> import modulo1 # Procura modulo1.py no 
# mesmo diretorio
# File "/Users/albertosoares/Projetos/dundie_rewards/modulo1.py", 
# line 11, in <module> modulo2.say_hello(NOME)
# AttributeError: partially initialized module 'modulo2' has no 
# attribute 'say_hello' (most likely due to a circular import)
#
