import pandas as pd

def analisar_estatisticas_iniciais():
    path = 'data/raw_reports.csv'
    
    try:
        df = pd.read_csv(path)
        print("🔍 Analisando Integridade dos Dados...")
        
        # 1. Estatística 
        total_relatorios = len(df)
        contagem_setores = df['setor'].value_counts()
        contagem_riscos = df['risco_declarado'].value_counts()
        
        print(f"\n✅ Total de registros: {total_relatorios}")
        print("\n🏢 Relatórios por Setor:")
        print(contagem_setores)
        
        print("\n⚠️ Distribuição de Riscos Declarados (Humanos):")
        print(contagem_riscos)
        
        # 2. Identificando 'Unstructured Data' longo (análise de texto básica)
        df['tamanho_descricao'] = df['descricao_bruta'].str.len()
        media_texto = df['tamanho_descricao'].mean()
        print(f"\n📝 Comprimento médio das descrições textuais: {media_texto:.2f} caracteres")

        return df

    except FileNotFoundError:
        print("❌ Erro: O arquivo de dados ainda não existe. Rode o data_generator.py primeiro.")

if __name__ == "__main__":
    analisar_estatisticas_iniciais()