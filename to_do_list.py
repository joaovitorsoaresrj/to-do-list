import os
import json

def exibir_lista(lista):
    print("Os itens listados são:")
    for indice, item in enumerate(lista, start = 1):
        print(f"{indice}. {item}")

def limpar_tela():
    os.system("cls")

def listar():
    limpar_tela()
    if lista_de_comandos == []:
        print("A lista de tarefas está vazia.")
    else:
        exibir_lista(lista_de_comandos)

def desfazer():
    if lista_de_comandos == []:
        limpar_tela()
        print("Nenhuma tarefa disponível para desfazer.")
    else:
        limpar_tela()
        lista_de_apagados.append(lista_de_comandos[-1])
        lista_de_comandos.pop()
        salvar(lista_de_comandos, CAMINHO_ARQUIVO)
        exibir_lista(lista_de_comandos)

def refazer():
    if lista_de_apagados == []:
        limpar_tela()
        print("Nenhuma tarefa disponível para refazer.")
    else:
        limpar_tela()
        lista_de_comandos.append(lista_de_apagados[-1])
        lista_de_apagados.pop()
        salvar(lista_de_comandos, CAMINHO_ARQUIVO)
        exibir_lista(lista_de_comandos) 

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, "r", encoding="utf8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, "w", encoding="utf8") as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO  = "to_do_list.json"

lista_de_comandos = ler([], CAMINHO_ARQUIVO)
lista_de_apagados = []

limpar_tela()
print("=" * 70)
print("LISTA DE TAREFAS COM DESFAZER E REFAZER")
print("=" * 70)

while True:

    print("\nComandos: \n" \
    "Listar: Para listar tarefas.\n" \
    "Desfazer: Para desfazer a última alteração.\n" \
    "Refazer: Para refazer a última alteração.\n" \
    "Sair: Para fechar o programa.\n")

    comando_tarefa = input("Digite uma tarefa ou comando: ")
    comando_formatado = comando_tarefa.lower()

    if comando_formatado == "listar":
        listar()

    elif comando_formatado == "desfazer":
        desfazer()


    elif comando_formatado == "refazer":
        refazer()

    elif comando_formatado == "sair":
        break

    else:
        if lista_de_apagados:
            lista_de_apagados.clear()

        limpar_tela()
        lista_de_comandos.append(comando_tarefa)
        salvar(lista_de_comandos, CAMINHO_ARQUIVO)
        print(f"A tarefa {comando_tarefa} foi adicionada.")

