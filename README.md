# Agente Autônomo para Análise de Notas Fiscais

Este projeto consiste em um agente de IA capaz de responder a perguntas em linguagem natural sobre dados de notas fiscais contidos em arquivos CSV.

O agente utiliza a biblioteca LangChain e o modelo de linguagem Gemini do Google para interpretar as perguntas e a biblioteca Pandas para analisar os dados e encontrar as respostas.

---

## Manual de Instalação e Execução

Para garantir uma instalação sem erros, siga os passos abaixo **exatamente na ordem apresentada**.

### Pré-requisitos

- Python 3.9 ou superior instalado.
- Git instalado.
- Uma chave de API válida do Google AI Studio (para o modelo Gemini).

### Passo a Passo da Instalação

**Passo 1: Baixar o Projeto e Entrar no Diretório**

Abra seu terminal (Prompt de Comando, PowerShell, ou Terminal) e execute os comandos abaixo para baixar os arquivos do projeto e entrar na pasta correta.

```bash
git clone https://github.com/4uguzt0/agenteCSV.git
```
***Importante: Todos os passos seguintes devem ser executados de dentro da pasta `agenteCSV`.***

**Passo 2: Criar e Ativar o Ambiente Virtual**

Vamos criar um ambiente isolado para instalar as bibliotecas do projeto. Isso evita conflitos com outros projetos Python.

```bash
# Comando para criar a pasta do ambiente virtual chamada "venv"
python -m venv venv

# Comando para ATIVAR o ambiente (escolha o do seu sistema operacional)

# No Windows (Prompt de Comando ou PowerShell):
venv\Scripts\activate

# No macOS ou Linux:
source venv/bin/activate
```
***Verificação de Sucesso:*** *Você saberá que funcionou quando o nome `(venv)` aparecer no início da linha do seu terminal.*

**Passo 3: Instalar as Dependências do Projeto**

Com o ambiente `(venv)` ativo dentro da pasta do agente execute o comando abaixo para instalar todas as bibliotecas necessárias, listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```
***Este comando só funcionará se o Passo 2 foi bem-sucedido e o `(venv)` estiver visível no seu terminal.***

**Passo 4: Configurar a Chave de API**

O agente precisa da chave para se comunicar com o Gemini. Configure-a como uma **variável de ambiente** para a sessão atual do seu terminal.

**Aviso:** **NÃO** coloque sua chave diretamente no código. Este método é temporário e seguro para a sessão atual do terminal.

```bash
# No Windows (Prompt de Comando):
set GOOGLE_API_KEY=COLE_SUA_CHAVE_API_AQUI

# No macOS/Linux ou Windows (PowerShell):
export GOOGLE_API_KEY='COLE_SUA_CHAVE_API_AQUI'
```

**Passo 5: Executar o Agente**

Se todos os passos anteriores foram concluídos com sucesso, o agente está pronto para ser executado.

```bash
python meu_agente.py
```
O script será iniciado, as mensagens de boas-vindas aparecerão, e você poderá começar a fazer suas perguntas.

---

## Exemplos de Perguntas
- Qual é o fornecedor que teve maior montante recebido?
- Qual item teve maior volume entregue (em quantidade)?
- Liste os 3 itens mais caros (por valor unitário).
- Qual o valor total de todas as notas?

## Tecnologias Utilizadas
- **Python**
- **LangChain** - Framework para desenvolvimento de aplicações com LLMs.
- **Google Gemini** - Modelo de Linguagem utilizado como cérebro do agente.
- **Pandas** - Biblioteca para manipulação e análise dos dados CSV.
- **Tabulate** - Dependência opcional do Pandas para formatação de tabelas.
- 
