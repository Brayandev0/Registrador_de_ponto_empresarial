# Criador         : Brayan vieira 
# função          : Um sistema de gerenciamento de Ponto eletronico
# versão          : 1.0
# data da criação : 08/03/2024
import datetime
import os 
import platform
#--------------------------------------------------------------------------------
#                               variaveis padrões
cargos = ["mecanico","medico","atendente","logista"]
padrao = "\n Insira qualquer tecla para continuar "
arquivo = "Pontos_batidos.txt"
horario_definido = 9
barras = 35 * "_"
#--------------------------------------------------------------------------------
#                   Definindo varíaveis de tempo 
hora = datetime.datetime.now().hour
minuto = datetime.datetime.now().minute
tempo_atual = datetime.datetime.now().time
data = datetime.datetime.now().date()
#--------------------------------------------------------------------------------
#                       verificando cargos
def verificar_cargo(cargo):
    for total in cargos:
        if cargo == total:
            return True
    else:
        return False
#--------------------------------------------------------------------------------
#                       Mostrando Cargos
def mostrar_cargos():
    for total in cargos:
        print(barras,"\n")
        print(total)
#--------------------------------------------------------------------------------
#                       detectando o os para o clear 
def limpador():
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        limpador = "cls"
    elif sistema_operacional == "Linux" or sistema_operacional == "Mac":
        limpador = "clear"
    return os.system(limpador)
#--------------------------------------------------------------------------------
#                       verificando existencia de arquivos
def verificar_existencia_do_arquivo():
    try:
        with open(arquivo,"r") as arquivo_:
            testando = arquivo_.readline()
    except FileNotFoundError:
        with open(arquivo,"x") as arquivo_:
            teste = arquivo_.readline()
#--------------------------------------------------------------------------------
#                       verificando atrasos
def verificar_atraso():
    if hora >= horario_definido:
        return True
    else:
        return False
#--------------------------------------------------------------------------------
#                           registrando pontos batidos 
def registrar_ponto():
        nome_do_funcionario = input(" \n Insira seu nome completo para continuar : ")
        if len(nome_do_funcionario) <= 3:
            print(" \n ERRO \n\n O nome inserido é invalido \n ")
            exit()
        limpador()
        print("Cargos disponiveis : ")
        mostrar_cargos()
        Insira_seu_cargo = input(" \n \n Insira seu cargo na empresa para continuar : ")
        if verificar_cargo(Insira_seu_cargo):
            if len(Insira_seu_cargo) <= 3:
                print(" \n ERRO \n\n O cargo inserido é invalido \n ")
                exit()
            with open(arquivo, "a", encoding="utf-8") as arquivo_de_pontos:
                arquivo_de_pontos.write("\n")
                arquivo_de_pontos.write(f" Nome do funcionario  : {nome_do_funcionario} \n ")
                arquivo_de_pontos.write(f"Cargo do Funcionario : {Insira_seu_cargo} \n ",)
                arquivo_de_pontos.write(f"Hora do ponto batido : {hora}:{minuto} \n ")
                arquivo_de_pontos.write(f"Data do ponto batido : {data} \n ")
                if verificar_atraso():
                    atraso_total = hora - horario_definido
                    arquivo_de_pontos.write(f"Atraso de : {atraso_total} Horas e {minuto} Minutos \n ")
                    arquivo_de_pontos.write(barras)
            limpador()
            print("Horário Adicionado com sucesso...")
        else:
            print("\n ERRO \n \n Cargo inserido inexistente \n ")
            exit()
#--------------------------------------------------------------------------------
#                           ver pontos batidos 
def ver_pontos():
    with open(arquivo,"r",encoding="utf-8") as arquivos_pontos:
        for total in arquivos_pontos:
            print(total)
menu = '''
        ┌─────────────────────────────────┐
        │ Bem vindo ao sistema de bater   │
        │             ponto               │
        ├─────────────────────────────────┤
        │ [ B ] Bater ponto de horário    |
        |                                 │
        │ [ V ] Ver Pontos Batidos        │
        │                                 |                  
        | [ E ]  Sair                     │
        └─────────────────────────────────┘


    Selecione alguma alternativa : '''
#--------------------------------------------------------------------------------
#                       Menu do programa 
while True:
    verificar_existencia_do_arquivo()
    limpador()
    decisao_menu = input(menu).lower()
    limpador()
    match decisao_menu:
        case "b":
            registrar_ponto()
            input(padrao)
        case "v":
            ver_pontos()
            input(padrao)
        case "e":
            limpador()
            print("Saindo......")
            exit()
        case _:
            print("\n ERRO \n\n Caracter inválido detectado \n ")
            input(padrao)
