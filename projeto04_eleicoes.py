# Procurei seguir ao máximo o enunciado inclusive na lógica pedida para a função autorização() e a votar().
# Procurei ao máximo dar prints dentro das funções de lógicas.

from collections import Counter
import os
from time import sleep
import pygame

# Recebe o ano de nascimento e verifica, pela idade, se a pessoa tem o voto negado, opcional ou obrigatório. Recebe a autorização


def authorize_vote(year):
    from datetime import date
    current_year = date.today().year
    age = current_year - year
    if 16 <= age < 18 or age >= 70:
        authorize = True
    elif 18 <= age < 70:
        authorize = True
    else:
        authorize = False

    # O retorno da fun Menu (Nº escolhido) é passado como parâmetro p/ a função que computa o voto, juntamente com a autorização obtida "Vl Literal".
    return polling(authorize, menu())

# recebe o nº do candidato e a autorização para votar, (seguindo literalmente o enunciado). Faz a verificação da autorização p/ computar o voto ou não. ### Vale lembrar q já poderíamos ter encerrado o programa na função anterior, mas como enunciado pede, foi feito assim.


def polling(situation, vote):
    if situation == False:  # se for falso, a pessoa não pode votar.
        return False
    elif vote not in range(1, 6):
        print('Não existe candidatos nesse número!!!!!!!!!!!')
        sleep(1)
    else:
        if vote in candidatos:
            votos.update([vote])  # O voto é adicionado.


def show_result():  # Mostra o resultado da votação.
    print()
    for n, qtd in votos.most_common():  # Método da Counter() que conta o mais comum, ou seja, o que mais aparece na lista
        print(
            f'\033[32m{candidatos[n]}:\033[m  recebeu \033[32m{qtd}\033[m votos')

    # Inclui apenas o ou os candidatos, ou as opções, que não receberam nenhum voto em uma outra listagem, caso isso aconteça.
    for i in range(1, 6):
        if i in candidatos and i not in votos:
            not_voted.update([i])

    for n, qtd in not_voted.most_common():  # Printa os q não receberam votos
        print(
            f'\033[32m{candidatos[n]}:\033[m  recebeu \033[32m{(qtd-1)}\033[m votos')  # printando a (-1), que vai revelar a quantidade de votos.

# Função p/ limpar a tela


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# função q inicia um som da biblioteca pygame e vai ser invocada a cada início e no final limpa a tela


def start():

    pygame.mixer.music.load('aud.mp3')
    pygame.mixer.music.play()
    print('''
    
           ####    ##   ##   ####      ####    ####      ##     ##   ##  #####     #####
            ##     ###  ##    ##      ##  ##    ##      ####    ###  ##   ## ##   ##   ##
            ##     #### ##    ##     ##         ##     ##  ##   #### ##   ##  ##  ##   ##
            ##     ## ####    ##     ##         ##     ##  ##   ## ####   ##  ##  ##   ##
            ##     ##  ###    ##     ##         ##     ######   ##  ###   ##  ##  ##   ##
            ##     ##   ##    ##      ##  ##    ##     ##  ##   ##   ##   ## ##   ##   ##    ##       ##       ##
           ####    ##   ##   ####      ####    ####    ##  ##   ##   ##  #####     #####     ##       ##       ##                           
           
           ''')

    sleep(1)
    clean_screen()

# função q finaliza a cada voto. Reproduz um som da biblioteca pygame e vai ser invocada a cada final, mas antes limpa a tela


def end():
    clean_screen()
    pygame.mixer.music.play()
    print('''
                ######    ####    ##   ##
                ##         ##     ### ###
                ##         ##     #######
                ####       ##     ## # ##
                ##         ##     ##   ##
                ##         ##     ##   ##    ##      ##      ##
                ##        ####    ##   ##    ##      ##      ## ''')
    sleep(2)

# Exibe o menu com as opções e retorna a opção escolhida. Chama a função limpa  a tela


def menu():
    clean_screen()
    print('''
CANDIDATOS:

Escolha uma das opções abaixo:
\033[32m[1]\033[m Chapolim
\033[32m[2]\033[m Tio Sam
\033[32m[3]\033[m Seu Creiço
\033[32m[4]\033[m Branco
\033[32m[5]\033[m Nulo
\n''')
    number = int(input(f'Informe o Número do Candidato:  '))
    return number


clean_screen()
# Dicionário dos candidatos
candidatos = {
    1: 'Chapolin',
    2: 'Tio San',
    3: 'Seu Creiço',
    4: 'Branco',
    5: 'Nulo'
}
pygame.init()
# Usada para ser possível fazer o uso do método most_common() e buscar a opção que mais aparece.
votos = Counter()
# Usada para ser possível fazer o uso do método most_common(), dessa vez,  na lógica aplicada, ela irá buscar, somente, os que não foram votados.
not_voted = Counter()

# O programa inicia aqui.
while True:
    while True:
        start()
        print('JUSTIÇA ELEITORAL DO BRASIL\nURNA LIBERADA.')
        year = int(input('\nInsira o ano do seu nascimento (AAAA):  '))
        situation = authorize_vote(year)
        if situation == False:
            print('Você não pode votar!')
            sleep(2)
            end()
            break

        end()
        break

    clean_screen()
    reply = input(
        'Pressione [N] para sair e ver o resultado da apuração ou tecle algo para continuar:  ').strip().upper()[0]
    if reply == 'N':
        break

show_result()  # chama o resultado da votação.
