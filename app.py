import streamlit as st
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Configuração da Página
st.set_page_config(page_title="Auditoria de Obras IA", layout="wide")

st.title("🏗️ Auditoria Inteligente de Riscos - CivicEval")
st.markdown("Faça o upload do relatório de obra para validar as classificações de risco com IA.")

# Barra lateral para a Chave API
with st.sidebar:
    st.header("Configurações")
    api_key = st.text_input("Insira sua Groq API Key", type="password")
    modelo = "llama-3.3-70b-versatile"

# 1. Upload do Arquivo
arquivo_upload = st.file_uploader("Escolha o arquivo CSV da obra", type="csv")

if arquivo_upload is not None:
    df = pd.read_csv(arquivo_upload)
    st.write("### Dados Brutos do Relatório")
    st.dataframe(df.head()) # Mostra uma prévia da tabela

    if st.button("🚀 Iniciar Auditoria com IA"):
        if not api_key:
            st.error("Por favor, insira a sua API Key na barra lateral!")
        else:
            try:
                llm = ChatGroq(model=modelo, groq_api_key=api_key, temperature=0)
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "Responda apenas: Baixo, Médio, Alto ou Crítico."),
                    ("human", "Analise este incidente de obra: {descricao}")
                ])
                chain = prompt | llm

                resultados = []
                progresso = st.progress(0)
                
                # Vamos processar os primeiros 5 para teste rápido
                total = min(len(df), 5) 
                
                for i, row in df.head(total).iterrows():
                    resp = chain.invoke({"descricao": row['descricao_bruta']})
                    risco_ia = resp.content.strip().replace(".", "")
                    
                    resultados.append({
                        "ID": row['id_relatorio'],
                        "Humano": row['risco_declarado'],
                        "IA": risco_ia,
                        "Divergência": "⚠️ SIM" if str(row['risco_declarado']).lower() != risco_ia.lower() else "✅ NÃO"
                    })
                    progresso.progress((i + 1) / total)

                # Exibição dos Resultados
                df_final = pd.DataFrame(resultados)
                st.write("### 📊 Resultado da Auditoria")
                
                # Estilizando a tabela
                st.table(df_final)
                
                st.success("Auditoria concluída com sucesso!")
                
            except Exception as e:
                st.error(f"Erro ao processar: {e}")

else:
    st.info("Aguardando upload do arquivo CSV para começar...")