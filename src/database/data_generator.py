import pandas as pd
import random

def gerar_dados_industriais(n=1000):
    """
    Simula uma base de dados em larga escala de relatórios de obra
    com textos não estruturados (Unstructured Data).
    """
    setores = ['Civil', 'Elétrica', 'Hidráulica', 'Segurança']
    riscos = ['Baixo', 'Médio', 'Alto', 'Crítico']
    
    descricoes_base = [
        "Fiação exposta próxima à área úmida no setor norte.",
        "Ausência de uso de EPI (capacete) por três operários na laje.",
        "Rachadura identificada no pilar B4 após concretagem.",
        "Vazamento de óleo no guindaste durante operação de carga.",
        "Escada de acesso sem corrimão instalado corretamente.",
        "Tudo em conformidade com as normas de segurança.",
        "Material acumulado bloqueando a saída de emergência."
    ]

    dados = []
    for i in range(n):
        dados.append({
            'id_relatorio': f"REL-{i+1000}",
            'setor': random.choice(setores),
            'descricao_bruta': random.choice(descricoes_base) + f" (Ref: {random.randint(1, 999)})",
            'risco_declarado': random.choice(riscos),
            'temperatura_local': random.uniform(25, 40)
        })
    
    df = pd.DataFrame(dados)
    df.to_csv('data/raw_reports.csv', index=False)
    print(f"✅ Gerados {n} relatórios de obra para processamento em larga escala.")

if __name__ == "__main__":
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
    gerar_dados_industriais()