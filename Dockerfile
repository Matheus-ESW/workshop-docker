# FROM python:3.12.1
# RUN pip install poetry
# COPY  . /src
# WORKDIR /src
# RUN poetry install
# EXPOSE 8501
# ENTRYPOINT [ "poetry", "run", "streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0" ]

FROM python:3.12.1

# Instala Poetry
RUN pip install poetry

# Copia apenas arquivos de dependência primeiro (cache layer)
COPY pyproject.toml poetry.lock* /src/

WORKDIR /src

# Instala dependências sem instalar o pacote local
RUN poetry config virtualenvs.create false && \
    poetry install --no-root

# Copia o resto do projeto
COPY . /src

EXPOSE 8501

ENTRYPOINT [ "poetry", "run", "streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0" ]