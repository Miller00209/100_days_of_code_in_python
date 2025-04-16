from random import randint
from time import sleep

points = 0

while True:
    num = randint(1,10)
    print("\033[2J\033[HEscolhi um número entre 1 e 10, tente descobrir qual é...")
    for i in range(3, 0, -1):
        print(f"Pontuação: {points}pts")
        print(f"Tentativas restantes: {i}")
        res = int(input("Sua resposta: "))
        if res == num:
            print("\033[1;92mParabéns, você acertou o número. +10 pontos\033[m]")
            points += 10
            sleep(2)
            break
    else:
        print("\033[1;91mTentativas esgotadas. -5 pts\033[m")
        points -= 5
        sleep(2)
    
    if points < 0:
        opt = input("Você perdeu, quer jogar novamente? (S/N)")
        if opt.lower() == "n":
            exit(0)
        else:
            points = 0
            continue
    elif points >= 100:
        opt = input("Você venceu, quer jogar novamente? (S/N)")
        if opt.lower() == "n":
            exit(0)
        else:
            points = 0
            continue