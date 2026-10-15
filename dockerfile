# Usa a imagem oficial do Python 3.12 (compatível com o teu requires-python >= 3.12)
FROM python:3.12-slim

# Copia o executável do uv diretamente da imagem oficial da Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Define o diretório de trabalho dentro do contentor
WORKDIR /app

# Copia os ficheiros de dependências primeiro (aproveita o cache do Docker)
COPY pyproject.toml uv.lock ./

# Instala as dependências exatas do uv.lock sem pacotes de desenvolvimento
RUN uv sync --frozen --no-dev --no-install-project

# Copia o ficheiro principal e a pasta src para dentro do contentor
COPY main.py ./
COPY src/ ./src/

# Coloca o ambiente virtual criado pelo uv no PATH do sistema
ENV PATH="/app/.venv/bin:$PATH"

# Expõe a porta padrão
EXPOSE 8000

# O Render injeta a variável de ambiente $PORT automaticamente.
# Se não existir (ex: ao testar localmente), usa a porta 8000 por defeito.
CMD ["sh", "-c", "fastapi run main.py --host 0.0.0.0 --port ${PORT:-8000}"]