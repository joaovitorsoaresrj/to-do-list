# Lista de Tarefas com Desfazer e Refazer (To-Do List)

Este é um aplicativo de linha de comando (CLI) desenvolvido em Python para o gerenciamento prático de tarefas diárias. O projeto foi estruturado com foco em modularidade, legibilidade de código e manipulação eficiente de estruturas de dados.

Além do sistema de **Desfazer (Undo)** e **Refazer (Redo)**, a aplicação conta com **persistência de dados em arquivo JSON**, permitindo que as tarefas sejam armazenadas permanentemente e recuperadas automaticamente ao reiniciar o programa.

## 🚀 Funcionalidades

* **Adicionar Tarefas:** Permite inserir novas tarefas mantendo a formatação original digitada pelo usuário.
* **Listar Tarefas:** Exibe todas as tarefas cadastradas com índices numéricos sequenciais.
* **Desfazer (Undo):** Remove a última tarefa adicionada e a armazena temporariamente em uma pilha de histórico.
* **Refazer (Redo):** Recupera a última tarefa removida por meio do comando de desfazer.
* **Persistência em JSON:** Todas as alterações são salvas automaticamente no arquivo `to_do_list.json`.
* **Carregamento Automático:** As tarefas são recuperadas automaticamente ao iniciar o programa.
* **Interface CLI Fluida:** Limpeza automática do terminal para melhorar a experiência do usuário.
* **Controle de Estado:** O histórico de refazer é limpo automaticamente quando uma nova tarefa é adicionada após um desfazer.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Biblioteca `os`** (limpeza do terminal)
* **Biblioteca `json`** (armazenamento e recuperação permanente das tarefas)

## 🗂️ Estrutura do Código

O projeto foi dividido em funções específicas para facilitar manutenção e reutilização:

* `exibir_lista(lista)`: Exibe as tarefas numeradas utilizando `enumerate()`.
* `limpar_tela()`: Responsável pela limpeza do terminal.
* `listar()`: Exibe as tarefas cadastradas ou informa quando a lista está vazia.
* `desfazer()`: Move a última tarefa da lista principal para a pilha de tarefas removidas.
* `refazer()`: Restaura a última tarefa removida.
* `ler(tarefas, caminho_arquivo)`: Carrega os dados armazenados no arquivo JSON.
* `salvar(tarefas, caminho_arquivo)`: Persiste as alterações realizadas na lista de tarefas.

## 💾 Persistência de Dados

As tarefas são armazenadas no arquivo:

```text
to_do_list.json
```

Sempre que uma tarefa é adicionada, desfeita ou refeita, a lista é atualizada automaticamente no arquivo JSON. Dessa forma, os dados permanecem disponíveis mesmo após o encerramento do programa.

## 📦 Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado.
2. Baixe ou clone este repositório.
3. Abra o terminal no diretório do projeto.
4. Execute o comando:

```bash
python to_do_list.py
```

## 📚 Conceitos Aplicados

* Estruturas de dados (listas e pilhas)
* Manipulação de arquivos
* Serialização de dados com JSON
* Tratamento de exceções (`try` / `except`)
* Modularização de código
* Persistência de dados
* Interface de linha de comando (CLI)
