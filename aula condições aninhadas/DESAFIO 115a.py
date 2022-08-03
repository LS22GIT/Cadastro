from menor.lib.interface import *
from menor.lib.arquivo import *
cadastro = {}
lis=[]
arq= "arquivo.txt"
if not existe(arq):
    criar (arq)
while True:
        opcao=escolha()
        if opcao == 1:
            ler(arq)
        elif opcao == 2:
            while True:
                try:
                    cadastro[f"Ano"] = int(input("Digite o ano de nascimento:"))
                    cadastro[f"Nome"] = input("Digite o nome:").title()
                except (ValueError, TypeError):
                    print("Houve um problema em relação ao tipo de dado que digitou")
                except:
                    print(" deu errado")
                else:
                    print("salvo com sucesso")
                    cadastrar(arq,cadastro[f"Ano"],cadastro[f"Nome"])
                    lis.append(cadastro.copy())
                    break
        elif opcao==3:
            nome=input("Digite o nome do arquivo:  ")
            criar(nome)
        elif opcao==4:
            arq=input("que arquivo deseja selecionar?" )
        elif opcao==5:
            break
print("Até mais")