
# CivicEval: AI-Driven Risk Audit System

## Project Overview
This project features the development of a data and artificial intelligence pipeline designed for the automated auditing of safety reports within large-scale civil engineering sites. The solution integrates Large Language Models (LLMs), statistical analysis, and data visualization to enhance the technical accuracy of risk classifications.

## Technical Description 

### Situation
Risk management in high-complexity engineering projects often relies on subjective classifications provided by field operators. It was identified that this subjectivity created data inconsistencies, potentially masking critical risks and hindering evidence-based strategic decision-making.

### Task
The objective was to develop an independent auditing system capable of validating raw incident descriptions against established technical standards in real-time. The goal was to utilize Artificial Intelligence to eliminate human bias and centralize compliance indicators.

### Action
To achieve this objective, the following technical stages were implemented:
* **AI Engine Development**: Implementation of a Python script utilizing LangChain and the Groq API to process textual descriptions through the Llama 3.3 70B model.
* **User Interface Construction**: Development of a web application via Streamlit to allow managers to perform CSV file uploads and obtain instantaneous audit results.
* **Analytics Pipeline**: Creation of a Power BI dashboard integrated with AI results to monitor divergence rates and identify sectors with the highest indices of classification errors.
* **Security and Governance**: Application of security best practices through secret management using environment variables and GitHub push protection protocols.

### Result
* **Identification of Divergences**: The audit revealed that 72.73% of manual risk classifications contained inconsistencies compared to the AI’s technical analysis.
* **Sectoral Insights**: Mapping indicated that the Hydraulics and Civil Safety sectors hold the highest volumes of critical errors, enabling targeted training interventions.
* **Operational Efficiency**: Replacing manual auditing with an automated solution significantly reduced report review time and increased the reliability of compliance data.

## Technologies Used
* **Languages**: Python (Pandas, LangChain)
* **AI/ML**: Groq Cloud (Llama 3.3), LLMs
* **BI Tools**: Power BI
* **Web Frameworks**: Streamlit
* **Version Control**: Git and GitHub





# CivicEval: Auditoria de Riscos com Inteligência Artificial

## Resumo do Projeto
Este projeto apresenta o desenvolvimento de um pipeline de dados e inteligência artificial para a auditoria automatizada de relatórios de segurança em canteiros de obras de engenharia civil. A solução integra modelos de linguagem de grande escala (LLMs), análise estatística e visualização de dados para otimizar a precisão técnica das classificações de risco.

## Descrição Técnica 

### Situação
O gerenciamento de riscos em projetos de grande escala frequentemente depende de classificações subjetivas fornecidas por operadores em campo. Identificou-se que essa subjetividade gerava inconsistências nos dados de segurança, mascarando riscos críticos e dificultando a tomada de decisão estratégica baseada em evidências técnicas.

### Tarefa
O objetivo foi desenvolver um sistema de auditoria independente capaz de validar, em tempo real, as descrições brutas de incidentes de obra contra normas técnicas pré-estabelecidas, utilizando Inteligência Artificial para eliminar o viés humano e centralizar os indicadores de conformidade.

### Ação
Para atingir o objetivo, foram executadas as seguintes etapas técnicas:
* **Desenvolvimento do Motor de IA**: Implementação de um script Python utilizando LangChain e a API Groq para processar descrições textuais através do modelo Llama 3.3 70B.
* **Construção de Interface de Usuário**: Desenvolvimento de uma aplicação web via Streamlit para permitir que gestores realizem o upload de arquivos CSV e obtenham auditorias instantâneas.
* **Pipeline de Analytics**: Criação de um dashboard no Power BI integrado aos resultados da IA para monitorar a taxa de divergência e identificar os setores com maiores índices de erro classificatório.
* **Segurança e Governança**: Aplicação de boas práticas de segurança através do gerenciamento de segredos com variáveis de ambiente e proteção de push no GitHub.

### Resultado
* **Identificação de Divergências**: A auditoria revelou que 72,73% das classificações de risco feitas manualmente apresentavam inconsistências em relação à análise técnica da IA.
* **Insights Setoriais**: O mapeamento indicou que os setores de Hidráulica e Segurança Civil detêm os maiores volumes de erros críticos, permitindo intervenções de treinamento direcionadas.
* **Eficiência Operacional**: A substituição da auditoria manual por uma solução automatizada reduziu drasticamente o tempo de revisão dos relatórios e aumentou a confiabilidade dos dados de conformidade.

## Tecnologias Utilizadas
* **Linguagens**: Python (Pandas, LangChain)
* **IA/ML**: Groq Cloud (Llama 3.3), LLMs
* **Ferramentas de BI**: Power BI
* **Web Frameworks**: Streamlit
* **Controle de Versão**: Git e GitHub
