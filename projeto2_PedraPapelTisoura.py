import os
import random
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear')

cpu = vitCpu = vitJogador = jogador = rodadaVitCpu = rodadaVitJogador = 0
print('=' * 35)
print('       PEDRA, PAPEL E TESOURA')
print('=' * 35)
resp = input('Você quer jogar? [S / N]:  ').strip().upper()[0]

if resp == 'S':
    while resp == 'S':
        temp_Cpu = temp_Jogador = 0 
        jogos = int(input('Quantas rodadas você quer jogar?  ').strip())
        for i in range(jogos):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('=' * 22)
            print(' '*6, f'{(i+1)}º JOGO: ')
            print('-' * 22)
            cpu = random.randint(0,2)
            if cpu == 0:
                cpu = 'pedra'
            elif cpu == 1:
                cpu = 'papel'
            else:
                cpu = 'tesoura'                
            
            print('Escolha um número:')
            print(' [0] - Pedra\n [1] - Papel\n [2] - Tesoura')
            jogador = int(input('\nFaça a sua jogada: ').strip()[0])
            print('-' * 22)
            while jogador not in (0,1,2):
                jogador = int(input(f'\n\nErro.  Você digitou o número {jogador}.  Este valor não é uma opção válida para este jogo.\nEscolha uma das opções abaixo: \n  [0] para Pedra  |  [1] para Papel  |  [2] para Tesoura.\nTente outro número:  ').strip()[0])
            
            if jogador == 0:
                jogador = 'pedra'
            elif jogador == 1:
                jogador = 'papel'
            else:
                jogador = 'tesoura'
            
            print(f'A CPU jogou:   {cpu}')
            print(f'Você jogou:  {jogador}')

            print('-' * 22)
            if jogador == cpu:
                print('   O JOGO EMPATOU! ')
            elif jogador == 'pedra' and cpu == 'tesoura':
                print('     VOCÊ GANHOU! ')
                temp_Jogador += 1
            elif jogador == 'papel' and cpu == 'pedra':
                print('     VOCÊ GANHOU! ')
                temp_Jogador += 1
            elif jogador == 'tesoura' and cpu == 'papel':
                print('      VOCÊ GANHOU! ')
                temp_Jogador += 1
            else:
                print('     A CPU GANHOU! ') 
                temp_Cpu += 1               
            print('-' * 22)
            print('\n\nAguarde...')
            sleep(4)            
        vitCpu += temp_Cpu
        vitJogador += temp_Jogador
        os.system('cls' if os.name == 'nt' else 'clear')
        if temp_Cpu > temp_Jogador:
            rodadaVitCpu += 1
            print(f'\nA CPU venceu a rodada com {temp_Cpu} vitória(s). ')
        elif temp_Jogador > temp_Cpu:
            rodadaVitJogador += 1
            print(f'\nO jogador venceu a rodada com {temp_Jogador} vitória(s). ') 
        else:
            print(f'\nA rodada terminou empatada com {temp_Jogador} vitória(s) para cada lado. ')
        
        resp = input('\nQuer jogar outra vez? [S / N]?  ').strip().upper()[0]

os.system('cls' if os.name == 'nt' else 'clear')
if vitCpu > vitJogador:
    campeao = 'CPU'
elif vitCpu < vitJogador:
    campeao = 'JOGADOR'
else:
    campeao = ' EMPATE '
print('=' * 45)
print(' '*14, 'JOGO FINALIZADO')
print('-' * 45)
print(f'\nNúmero de Rodadas vencidas pelo Jogador:  {rodadaVitJogador}')
print(f'Número de Rodadas vencidas pela CPU:  {rodadaVitCpu}\n')
print('*' * 45)
print('\n', ' '*5, f'O Grande Campeão foi:   {campeao}\n')
print('*' * 45)
sleep(8)