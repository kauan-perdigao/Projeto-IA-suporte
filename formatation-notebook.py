caminho_arquivo = r"C:\Users\kauan\Documents\proj02-suporte\proj02 - LLMs para empresas e negócios - Atendimento e Suporte.ipynb"

# Lê com a codificação padrão do Windows (latin-1) e salva em UTF-8
with open(caminho_arquivo, "r", encoding="latin-1") as f:
    conteudo = f.read()

with open(caminho_arquivo, "w", encoding="utf-8") as f:
    f.write(conteudo)
