import pandas as pd
# Importamos o modelo do Google em vez do da OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Função principal para executar o agente
def rodar_agente():
    print("🤖 Agente de Análise de CSV iniciado com cérebro Gemini!")

    # Passo 1: Carregar os arquivos CSV em DataFrames do pandas
    try:
        df_cabecalho = pd.read_csv("202401_NFs_Cabecalho.csv")
        df_itens = pd.read_csv("202401_NFs_Itens.csv")
        print("✅ Arquivos CSV carregados com sucesso.")
    except FileNotFoundError:
        print("🚨 Erro: Arquivos CSV não encontrados. Verifique se eles estão na mesma pasta que o script.")
        return

    # Passo 2: Inicializar o modelo de linguagem (LLM) - AGORA COM GEMINI
    # ALTERADO: Usamos o modelo "gemini-1.5-flash-latest" que é mais moderno.
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)
    print("🧠 Cérebro do agente (Gemini) inicializado.")

    # Passo 3: Criar um agente para cada DataFrame (esta parte não muda!)
    agente_cabecalho = create_pandas_dataframe_agent(
        llm,
        df_cabecalho,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        allow_dangerous_code=True
    )

    agente_itens = create_pandas_dataframe_agent(
        llm,
        df_itens,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        allow_dangerous_code=True
    )

    print("🛠️ Agentes criados e prontos para uso.")
    print("--------------------------------------------------")
    print("📄 Dica: O arquivo 'Cabecalho' tem dados do fornecedor e valores totais.")
    print("📦 Dica: O arquivo 'Itens' tem detalhes sobre os produtos, quantidade e valor unitário.")
    print("--------------------------------------------------")


    # Loop para o usuário fazer perguntas
    while True:
        pergunta = input("\n🤔 Faça sua pergunta (ou digite 'sair' para encerrar): ")
        if pergunta.lower() == 'sair':
            print("👋 Até mais!")
            break

        try:
            # Heurística simples para direcionar a pergunta ao agente certo
            if "fornecedor" in pergunta.lower() or "montante" in pergunta.lower() or "valor total" in pergunta.lower():
                print("\n🔄 Consultando o agente de Cabeçalho...")
                resposta = agente_cabecalho.invoke(pergunta)
            else:
                print("\n🔄 Consultando o agente de Itens...")
                resposta = agente_itens.invoke(pergunta)

            print("\n💡 Resposta do Agente:")
            print(resposta['output'])

        except Exception as e:
            print(f"🚨 Ocorreu um erro: {e}")

# Executa a função principal quando o script é rodado
if __name__ == "__main__":
    rodar_agente()