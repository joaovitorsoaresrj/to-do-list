# Lista de Tarefas com Desfazer e Refazer (To-Do List)

Este é um aplicativo de linha de comando (CLI) desenvolvido em Python para o gerenciamento prático de tarefas diárias. O projeto foi estruturado com foco em modularidade, legibilidade de código e manipulação eficiente de estruturas de dados em memória.

O grande diferencial desta aplicação é a implementação de um sistema robusto de **Desfazer (Undo)** e **Refazer (Redo)**, utilizando o conceito clássico de pilhas (*stacks*) para gerenciar o histórico de estados.

## 🚀 Funcionalidades

- **Adicionar Tarefas:** Permite inserir novas tarefas mantendo a formatação original (maiúsculas e minúsculas) digitada pelo usuário.
- **Listar Tarefas:** Exibe de forma organizada todas as tarefas ativas com índices numéricos sequenciais.
- **Desfazer (Undo):** Remove a última tarefa adicionada e a guarda temporariamente em um histórico de exclusão.
- **Refazer (Redo):** Recupera a última tarefa que foi desfeita, reinserindo-a na lista principal de tarefas.
- **Interface CLI Fluida:** Conta com limpeza automática do console a cada comando executado, otimizando a experiência de uso no terminal.
- **Tratamento de Estado:** O histórico de "Refazer" é redefinido automaticamente sempre que uma nova tarefa inédita é inserida, evitando inconsistências no fluxo de dados.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Biblioteca `os`** (nativa do Python, utilizada para gerenciar comandos do sistema de arquivos e console)

## 🗂️ Estrutura do Código

O projeto preza pela separação de responsabilidades, dividindo as operações em funções modulares:

- `exibir_lista(lista)`: Função auxiliar responsável por percorrer e formatar a lista utilizando `enumerate(..., start=1)`.
- `limpar_tela()`: Centraliza o comando de limpeza do console para manter a interface limpa.
- `listar()`: Realiza validações de segurança (verifica se a lista está vazia) antes de renderizar os itens na tela.
- `desfazer()`: Gerencia a lógica de pilhas retirando o último elemento da lista ativa via `.pop()` e inserindo-o no histórico via `.append()`.
- `refazer()`: Executa o caminho inverso, resgatando o último item da pilha de apagados.

## 📦 Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado no seu computador.
2. Baixe ou clone este repositório.
3. Abra o terminal (ou prompt de comando) no diretório onde o arquivo está salvo.
4. Execute o comando:
```bash
   python to_do_list.py