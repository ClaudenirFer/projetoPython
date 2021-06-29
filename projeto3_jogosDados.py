
import os
from operator import itemgetter
from collections import Counter
from random import randint
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear') # limpa tela
ranking = dict()
vitoria = []
resp = input('Você quer jogar [S/N]?  ').strip().upper()[0]
while resp != 'S' and 'N' != resp:  # Validando a resposta. Obriga S ou N
    print('Essa não é uma opção válida. Digite apenas S ou N.\n')
    resp = input('Você quer jogar [S/N]?  ').strip().upper()[0]    
if resp == 'S':
    while resp == 'S':
        c=0
        quant = int(input('Quantas rodadas?  ').strip())
        for c in range(quant):
            jogo = {"jogador 1": randint(1,6),"jogador 2": randint(1,6),"jogador 3": randint(1,6),"jogador 4": randint(1,6)}   # Dicionários com os jogadores 
            
            # Mostrando o jogo
            print()
            print('-'*35)
            print(f'            RODADA {c+1}')
            print('-'*35)        
            for k, v in jogo.items():            
                print(f'O jogador {k} tirou: {v}')
                sleep(1)
            
            ranking = [list(e) for e in (sorted(jogo.items(), key=itemgetter(1), reverse=True))] # 1º Ordena o dicionário, 2º Converte as tuplas em listas. No final teremos uma "Listagem" de listas.            
            
            # Verifica se há empate nas primeiras posições
            if ranking[0][1] == ranking[1][1]:
                print('\n')
                print('='*50)
                print('\nHouve empate entre os dois primeiros colocados:')
                print(f'{ranking[0][0]} tirou {ranking[0][1]} e o {ranking[1][0]} tirou {ranking[1][1]} também.')
                print('\nDesimpatando o jogo...\n')
                print('='*50)
                sleep(5)
                               
                # Evita o empate nas duas primeiras posições da lista.
                while ranking[0][1] == ranking[1][1]:
                    ranking[0][1] = randint(5,6)
                    ranking[1][1] = randint(5,6)                   
                    ranking = sorted(ranking, key=lambda l:l[1], reverse=True)  # Ordenando a lista depois do desempate entre os dois primeiros          

            # Mostrando o Ranking
            print(f'\n\n###### Ranking da pardida {c+1} ######')
            for i, v in enumerate(ranking):
                print(f'{i+1}º lugar: {v[0]} com o número: {v[1]}')
                
            print('-'*35)
            sleep(1)
            print('\n\n')
            vitoria.append(ranking[0][0]) # Adicona o ganhador na lista vitória
            
        resp = input('Quer continuar [S/N]?  ').strip().upper()[0] 
        while resp != 'S' and 'N' != resp:  # validando a resposta
            print('Essa não é uma opção válida. Digite apenas S ou N.')
            resp = input('Você quer jogar [S/N]?  ').strip().upper()[0]

    k = Counter(vitoria).most_common(1)[0][0] # Para pegar o jogador que mais apareceu na lista vitória
    v = Counter(vitoria).most_common(1)[0][1] # Para pegar a quantidade de vezes que o jogador apareceu na lista vitória.
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print('*'*52,'\n')
    print(f'O Grnade campeão foi o {k} com {v} vitória(s)\n')     
print('**************** JOGO FINALIZADO *******************')