# Calendário de Visitas - FCJA (Backend)

Este repositório contém o código do "backend" (a parte de trás, o cérebro) do sistema de agendamento de visitas da Fundação Casa José Américo (FCJA).

## O que é isso?

Imagine um restaurante. Você (o cliente) vê o cardápio e faz um pedido a um garçom (o "frontend", ou aplicativo). Esse garçom leva o pedido para a cozinha (o "backend", este projeto), que prepara a comida e acessa o estoque (o "banco de dados").

Este projeto é a **cozinha**. É uma API (Interface de Programação de Aplicações) que:

- Recebe pedidos (como "agendar uma visita" ou "ver datas disponíveis").
- Conecta-se ao banco de dados (MongoDB) para guardar e buscar informações.
- Envia respostas de volta para o "garçom" (frontend) para que o usuário veja.

## Tecnologias Principais

- **Python:** A linguagem de programação usada.
- **FastAPI:** A "receita" (framework) que usamos para construir a API de forma rápida e eficiente.
- **MongoDB:** O "estoque" (banco de dados) onde guardamos todas as informações.
- **Docker:** Uma ferramenta que usamos para "empacotar" o banco de dados MongoDB, facilitando a instalação em qualquer computador.

## Estrutura do Projeto

- `/backend`: Contém todo o código-fonte da API (a cozinha em si). **É aqui que a maior parte do trabalho acontece.**
- `docker-compose.dev.yml`: Um arquivo de "receita" para o Docker, que diz a ele como configurar e iniciar o banco de dados MongoDB.
- `LICENSE`: A licença de uso do projeto (MIT).

## Como Começar

Para entender como instalar e rodar o projeto, vá para a pasta principal do código:

- **[backend/README.md](backend/README.md)** (Clique aqui ou abra o arquivo na pasta `backend`)

Esse arquivo tem o passo a passo detalhado.
