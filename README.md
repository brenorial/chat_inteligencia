# FAQ Interativo - Descrição do Projeto

Este projeto consiste em um sistema de perguntas e respostas interativo, dividido em duas partes principais:

## 1. **Backend (Flask - Python)**

- **Objetivo**: O backend é responsável por gerenciar os dados do FAQ e fornecer os tópicos e perguntas para o frontend, a partir de uma API simples.
- **Tecnologia usada**: Flask
- **Como funciona**:
  - Um servidor local é criado utilizando o Flask, que expõe uma rota principal (`/`) para carregar a interface frontend (HTML).
  - Existe uma rota `/get_sub_questions/<topic>`, que recebe um tópico como parâmetro (ex.: "PAINEL") e retorna um conjunto de perguntas associadas a ele no formato JSON. 
  - A lista de tópicos e perguntas está armazenada em um dicionário chamado `faq`, onde as chaves representam os tópicos e os valores são as perguntas associadas.

## 2. **Frontend (HTML, CSS, JavaScript)**

- **Objetivo**: O frontend oferece a interface de interação para o usuário, permitindo que ele selecione tópicos e perguntas.
- **Tecnologia usada**: HTML, CSS, JavaScript
- **Como funciona**:
  - O HTML define a estrutura básica da interface, com um seletor de tópicos e um botão para o usuário interagir.
  - Quando o usuário escolhe um tópico, a aplicação faz uma requisição para o backend via JavaScript (AJAX) para buscar as perguntas relacionadas.
  - As perguntas são então exibidas dinamicamente em outro seletor (ou uma área de lista), permitindo que o usuário escolha uma pergunta.
  - Além disso, uma vez que o usuário seleciona a pergunta, um botão é mostrado para submeter a escolha.

## **Principais Funcionalidades**

1. **Seleção de Tópicos**: O usuário pode escolher um tópico a partir de um menu suspenso.
2. **Carregamento Dinâmico**: Com base na escolha do tópico, as perguntas são carregadas dinamicamente (sem recarregar a página), utilizando uma requisição ao backend.
3. **Interação**: Após o carregamento das perguntas, o usuário seleciona uma pergunta específica. Em seguida, um botão é exibido para finalizar a interação.

---

**Estrutura do Sistema**:
- **Backend**: Flask serve como servidor web que manipula as requisições e dados do FAQ.
- **Frontend**: HTML apresenta a interface com seleção de tópicos, enquanto JavaScript lida com a interação assíncrona (AJAX) para atualizar as perguntas sem recarregar a página.

**O que falta**:
- **Melhorias de Interface**: Podemos adicionar mais estilo e animações para melhorar a experiência do usuário.
- **Autenticação**: Se necessário, poderíamos adicionar uma camada de autenticação de usuário para personalizar as perguntas e respostas.

--- 

Esse é o resumo de como o sistema interativo está estruturado até o momento.
