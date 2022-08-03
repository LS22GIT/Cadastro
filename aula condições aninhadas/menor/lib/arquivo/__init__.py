def existe(txt):
    try:
        a=open(txt,"rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criar(txt):
    try:
        a = open(txt,"wt+")
        a.close()
    except:
        print(f"Houve um erro na criação do arquivo {txt}")
    else:
        print("arquivo criado com sucesso")
def ler(txt):
    try:
        a=open(txt,"rt")
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except:
        print("Houve um erro ao ler o arquivo")
        print('\033[1;93m1', '-', '\033[1;36mver pessoas cadastradas')
        print('\033[1;93m2', '-', '\033[1;36mlistar nova pessoa')
        print('\033[1;93m3', '-', '\033[1;36msair do menor\033[m')
    else:
        print('-' * 20)
        print('\033[1;93m PESSOAS CADATRADAS\033[m')
        print('-' * 20)
        print('N°|Ano    |Nome')
        c=0
        for linha in a:
                dado=linha.split(";")
                print(f'{c} {dado[0]}     {dado[1]}',end="")
                c+=1
    finally:
        a.close()
def cadastrar(arq,nome="desconhecido", idade=0):
    try:
        a=open(arq,'at')
    except:
        print("Houve um erro na abertura do arquivo")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um erro na hora de escrever os dados!")
        else:
            print(f"!Novo registro de {nome} adicionado")

        print(f"Novo registro de {nome} adicionado")

