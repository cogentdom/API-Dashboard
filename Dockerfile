FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .

# Install production dependencies.
RUN pip3 install -r requirements.txt

RUN mkdir .streamlit
COPY .streamlit/config.toml .streamlit/

COPY main.py .

EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]