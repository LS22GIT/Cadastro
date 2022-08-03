from time import sleep
cadastro={}
lis=[]
def cab():
    print('-' * 20)
    print('\033[1;93m   MENU PRINCIPAL\033[m')
    print('-' * 20)
    print('\033[1;93m1', '-', '\033[1;36mver pessoas cadastradas\033[m')
    print('\033[1;93m2', '-', '\033[1;36mlistar nova pessoa\033[m')
    print('\033[1;93m3', '-', '\033[1;36mnovo arquivo\033[m')
    print('\033[1;93m4', '-', '\033[1;36mselecionar arquivo\033[m')
    print('\033[1;93m5', '-', '\033[1;36msair do menu\033[m')
def escolha():
        while True:
            try:
                global opcao
                cab()
                opcao=int(input("O que deseja? "))
                sleep(0.5)
            except (ValueError, TypeError):
                print("Houve um problema em relação ao tipo de dado que digitou")
            except:
                print("!opção invalida!digite 1, 2 ou 3")
            else:
                if opcao >=1 and opcao<=4:
                   return opcao
                   break
                else:
                   print("opção invalida! digite 1, 2 ou 3")