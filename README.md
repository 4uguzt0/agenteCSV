# Agente Autônomo para Análise de Notas Fiscais

Este projeto consiste em um agente de IA capaz de responder a perguntas em linguagem natural sobre dados de notas fiscais contidos em arquivos CSV.

O agente utiliza a biblioteca LangChain e o modelo de linguagem Gemini do Google para interpretar as perguntas e a biblioteca Pandas para analisar os dados e encontrar as respostas.

---

## Como Executar o Projeto

Siga os passos abaixo para rodar o agente em sua máquina local.

### Pré-requisitos

- Python 3.9 ou superior
- Uma chave de API do Google AI Studio (Gemini)

### 1. Clonar o Repositório

```bash
git clone https://github.com/4uguzt0/agenteCSV.git
```

### 2. Instalar as Dependências

É altamente recomendado criar um ambiente virtual para isolar as dependências do projeto.

```bash
# Criar um ambiente virtual (opcional, mas recomendado)
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instalar as bibliotecas necessárias
pip install -r requirements.txt
```

### 3. Configurar a Chave de API

Este projeto requer uma chave de API do Google para funcionar. A forma mais segura de configurá-la é através de uma **variável de ambiente**.

**O script NÃO funcionará se a chave não for configurada.**

Crie uma variável de ambiente chamada `GOOGLE_API_KEY` com o valor da sua chave.

**Importante:** **NÃO** coloque sua chave de API diretamente no código ou em qualquer arquivo que será enviado para o GitHub.

### 4. Executar o Agente

Com o ambiente virtual ativado e a chave de API configurada, execute o script:

```bash
python meu_agente.py
```

O programa irá iniciar e você poderá fazer suas perguntas diretamente no terminal.

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