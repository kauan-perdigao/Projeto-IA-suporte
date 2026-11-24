# Chatbot de Atendimento SafeBank

Projeto de atendimento automatizado com RAG (Retrieval-Augmented Generation), desenvolvido em Python e Streamlit. O assistente consulta o manual em PDF da SafeBank e utiliza o modelo hospedado pela Groq para responder em português.

## Tecnologias

- Python
- Streamlit
- LangChain
- Groq
- FAISS
- Hugging Face Embeddings
- PyMuPDF

## Estrutura do projeto

- `app02.py` - aplicação web do chatbot.
- `manual-safebank.pdf` - documento utilizado como base de conhecimento.
- `index_faiss/` - índice vetorial gerado pelo FAISS.
- `proj02 - LLMs para empresas e negócios - Atendimento e Suporte.ipynb` - notebook com o desenvolvimento e testes do projeto.
- `.env.example` - exemplo de configuração da chave da Groq.
- `.venv/` - ambiente virtual local do projeto.

## Pré-requisitos

- Python 3.10 ou superior
- Conta e chave de API da Groq
- Aproximadamente 2 GB de espaço livre para o ambiente Python e os modelos de embedding

## Instalação

Clone o repositório e acesse a pasta do projeto:

```bash
git clone <url-do-repositorio>
cd proj02-suporte
```

Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install --upgrade pip
python -m pip install streamlit python-dotenv langchain==0.3.1 langchain-community==0.3.1 langchain-core langchain-classic langchain-text-splitters langchain-huggingface==0.1.1 langchain-groq PyMuPDF faiss-cpu sentence-transformers
```

## Configuração

Crie o arquivo `.env` a partir do arquivo de exemplo:

```powershell
Copy-Item .env.example .env
```

No arquivo `.env`, substitua o valor de exemplo pela chave obtida no console da Groq:

```env
GROQ_API_KEY=sua_chave_aqui
```

Não compartilhe a chave nem envie o arquivo `.env` para um repositório público.

## Executando a aplicação

Com o ambiente virtual ativado, execute:

```bash
streamlit run app02.py
```

A aplicação será aberta em `http://localhost:8501`.

Ao enviar a primeira pergunta, o projeto lê os PDFs da pasta do projeto, gera os fragmentos de texto, cria os embeddings com `BAAI/bge-m3` e inicia a recuperação de contexto com FAISS.

## Como funciona

1. O conteúdo do manual é extraído com PyMuPDF.
2. O texto é dividido em partes menores.
3. As partes são transformadas em embeddings.
4. Os fragmentos mais relevantes são recuperados pelo FAISS.
5. O histórico da conversa é considerado para reformular perguntas.
6. A Groq gera a resposta com base no contexto recuperado.

## Modelo

O modelo configurado em `app02.py` é:

```python
id_model = "openai/gpt-oss-20b"
```

Se o modelo não estiver disponível para sua conta, altere `id_model` para um modelo disponível no console da Groq.
