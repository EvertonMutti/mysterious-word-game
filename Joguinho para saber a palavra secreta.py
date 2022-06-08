# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 21:51:37 2022

@author: Everton SSD
"""
sPalavraSuperSecreta = 'bebaágua'
sLetrasDigitadas = []
chances = 3
Letra = ''
print('Joguinho da palavra mistériosa, para sair, digite: sair \nVamos começar!')

while True:
    sPalavraSecTemp = ''
    Letra = input('Digite uma letra ')
    
    if Letra.lower() == 'sair':
        break
    elif len(Letra) > 1:
        print('Eu só aceito letras')
        continue
    elif len(Letra) == 0:
        print('Digite alguma coisa pelo amor de deus ')
        continue
    elif Letra.isnumeric():
        print('Eu acredito que um número não seja exatamente uma letra')
        continue

    elif Letra in sLetrasDigitadas:
        print('Você já digitou essa letra, tente outra')
        continue
    else:
        #Essa váriavel acumula as letras digitadas
        sLetrasDigitadas.append(Letra)
        
        if Letra in sPalavraSuperSecreta:
            print('Uau, você acertou uma letra =)')
            
        else:
            chances -= 1
            if chances == 0:
                print('Você perdeu =(')
                break
            print(f'Você errou, você tem: {chances} restantes')
            sLetrasDigitadas.pop()
        
        
        for sletra_secreta in sPalavraSuperSecreta:
            if sletra_secreta in sLetrasDigitadas:
                sPalavraSecTemp = sPalavraSecTemp + sletra_secreta
            else:
                sPalavraSecTemp += '*'
        
        if sPalavraSecTemp == sPalavraSuperSecreta:
            print('Nunca desacreditei de você haha!!!.')
            sPalavraSecTempCort = sPalavraSecTemp[:4] + ' ' + sPalavraSecTemp[4:8]
            print(sPalavraSecTempCort)
            break
        
        
        sPalavraSecTempCort = sPalavraSecTemp[:4] + ' ' + sPalavraSecTemp[4:8]
        print(sPalavraSecTempCort)
            
     
     
