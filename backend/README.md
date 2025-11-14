# Backend - API do Calendário de Visitas

Bem-vindo à pasta principal do código da API! Este é o "cérebro" do sistema de agendamento.

Ele é construído com **FastAPI** e se conecta a um banco de dados **MongoDB**.

## O que você precisa ter instalado?

Antes de começar, garanta que você tem essas ferramentas no seu computador:

1.  **Python 3.10** (ou mais recente).
2.  **Docker** e **Docker Compose**: Usaremos isso para rodar o banco de dados MongoDB facilmente, sem precisar instalá-lo "na mão".
3.  **Um editor de código**: Como o VS Code.

---

## Passo a Passo para Rodar (Desenvolvimento)

Siga estas etapas para fazer a API funcionar na sua máquina.

### 1. Inicie o Banco de Dados (MongoDB)

Vamos usar o Docker para criar um "container" (uma caixa) com o MongoDB já pronto para nós.

1.  Verifique se o aplicativo Docker Desktop está aberto e rodando.
    
2.  Abra seu terminal ou prompt de comando.

3.  **Importante:** Navegue de volta para a pasta **raiz** do projeto (a pasta `back_calendario_visitacao`, _não_ esta pasta `backend`).

4.  Digite o comando abaixo e pressione Enter:

        ```bash
        docker-compose -f docker-compose.dev.yml up -d
        ```

5.  **O que isso faz?** Ele lê o arquivo `docker-compose.dev.yml` e inicia o MongoDB. O `-d` faz ele rodar em segundo plano. O banco de dados estará acessível na porta `27017`, que é exatamente onde a API espera encontrá-lo.

### 2. Configure a API (Esta pasta, `/backend`)

Agora, vamos preparar a API em si.

1.  **Crie um "Ambiente Virtual"**: Isso cria uma "bolha" para nosso projeto, para que as "peças" (pacotes) que ele usa não se misturem com outros projetos Python.

        - _No terminal, dentro desta pasta `/backend`:_

        ```bash
        python -m venv venv
        ```

2.  **Ative o Ambiente Virtual**:

        - _No Windows (CMD/PowerShell):_
          ```bash
          .\venv\Scripts\activate
          ```
        - _No macOS/Linux:_
          ```bash
          source venv/bin/activate
          ```
        - (Você deve ver `(venv)` aparecer no início da linha do seu terminal).

3.  **Instale os Pacotes (as "peças")**: Vamos instalar tudo o que está listado no arquivo `requirements.txt`.
        ```bash
        pip install -r requirements.txt
        ```

### 3. Rode a API

Tudo está pronto. Para iniciar o servidor da API, execute:

    ```bash
    python run.py
    ```

- Este comando usa o arquivo run.py, que por sua vez inicia o uvicorn (um servidor) com o nosso aplicativo app.main:app.

- O reload=True é ótimo para desenvolvimento: qualquer alteração que você salvar no código fará o servidor reiniciar automaticamente.

- Você verá mensagens no terminal indicando que o servidor está rodando em <http://0.0.0.0:8000> este comando usa o arquivo run.py, que por sua vez inicia o uvicorn (um servidor) com o nosso aplicativo app.main:app.

- O reload=True é ótimo para desenvolvimento: qualquer alteração que você salvar no código fará o servidor reiniciar automaticamente.

- Você verá mensagens no terminal indicando que o servidor está rodando em <http://0.0.0.0:8000>.

### 4. Verifique se Funcionou

Com o servidor rodando, abra seu navegador de internet:

    1. Teste 1: A API está viva?

    Acesse: <http://localhost:8000/>

    Você deve ver: {"status": "ok"}

    2. Teste 2: A API está falando com o Banco de Dados?

    Acesse: <http://localhost:8000/api/v1/db-check>

    Você deve ver: {"status": "ok", "message": "Conexão com o banco de dados bem-sucedida"}

    3. Teste 3: Veja a Documentação (O "Manual" da API)

    Acesse: <http://localhost:8000/docs>

O FastAPI gera automaticamente uma página interativa com todos os "caminhos" (endpoints) da API. Você pode até testá-los por aqui!

## Estrutura da Pasta /backend (Onde mexer)

Se você precisa adicionar ou alterar algo, aqui está o mapa:

`run.py`: Arquivo que você usa para iniciar o servidor.

`requitiments.txt`: Lista de todos os pacotes Python que o projeto precisa.

`app/main.py`: O coração da API. Ele cria o aplicativo FastAPI, define configurações gerais (como CORS, para permitir que o "frontend" converse com ele) e carrega as rotas.
`app/api/`: Pasta que guarda os "caminhos" (endpoints) da API.

`main_routes.py`: Junta todas as diferentes versões das rotas.

`v1/routes_v1.py`: Este é um arquivo importante! Ele define as rotas da "versão 1" da API, como /status e /db-check. Quando você for criar novas funções (como "agendar visita"), você provavelmente adicionará as rotas aqui.

`app/database/`: Pasta para os códigos que falam com o banco de dados.

`mongo_db.py`: Configura a conexão com o MongoDB e define o nome do banco como calendario_fcja.
