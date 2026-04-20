import pandas as pd
import os
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# 1. Caminhos
path_atual = Path(__file__).resolve()
raiz_do_projeto = path_atual.parent.parent.parent
caminho_csv = raiz_do_projeto / "data" / "raw_reports.csv"
caminho_saida = raiz_do_projeto / "data" / "relatorio_auditoria_ia.csv"

# 2. CHAVE QUE FUNCIONOU (Verifique se não há espaços extras)
api_key = "SUA_CHAVE_AQUI"  # Usei variáveis de ambiente (.env) para produção

def avaliar_riscos_com_ia():
    if not caminho_csv.exists():
        print("❌ Arquivo raw_reports.csv não encontrado!")
        return

    df = pd.read_csv(caminho_csv).head(10) # Processando 10 registros
    
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=api_key
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um Engenheiro de Segurança do Trabalho Sênior. Responda apenas com uma palavra: Baixo, Médio, Alto ou Crítico."),
        ("human", "Descrição do Incidente: {descricao}")
    ])

    chain = prompt | llm
    resultados = []

    print("\n🚀 Iniciando Auditoria...")
    
    for _, row in df.iterrows():
        try:
            resposta = chain.invoke({"descricao": row['descricao_bruta']})
            risco_ia = resposta.content.strip().replace(".", "")
            
            # Adiciona ao dicionário
            resultados.append({
                "id": row['id_relatorio'],
                "setor": row['setor'],
                "risco_humano": row['risco_declarado'],
                "risco_ia": risco_ia,
                "divergencia": "SIM" if str(row['risco_declarado']).strip().lower() != risco_ia.strip().lower() else "NÃO"
            })
            print(f"✅ Processado ID: {row['id_relatorio']} -> IA: {risco_ia}")
            
        except Exception as e:
            print(f"❌ Erro no ID {row['id_relatorio']}: Verifique sua conexão ou Chave API.")

    # 3. Salva e finaliza apenas se houver resultados
    if resultados:
        df_final = pd.DataFrame(resultados)
        df_final.to_csv(caminho_saida, index=False, encoding='utf-8')
        print(f"\n✨ PRONTO! Arquivo salvo em: {caminho_saida}")
        
        # Só tenta contar se a coluna existir
        if 'divergencia' in df_final.columns:
            total_div = len(df_final[df_final['divergencia'] == 'SIM'])
            print(f"📊 Total de divergências encontradas: {total_div}")
    else:
        print("\n⚠️ Nenhum dado foi processado devido a erros na API.")

if __name__ == "__main__":
    avaliar_riscos_com_ia()