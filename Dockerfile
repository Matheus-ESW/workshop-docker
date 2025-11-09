FROM python:3.12
RUN pip install poetry
COPY  . /src
WORKDIR /src
RUN poetry install
RUN poetry add streamlit pandas numpy plotly
EXPOSE 8501
ENTRYPOINT [ "poetry", "run", "streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0" ]