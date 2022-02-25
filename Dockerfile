FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY requirements.txt .

# Install production dependencies.
RUN pip install -r requirements.txt

RUN mkdir .streamlit
COPY .streamlit/config.toml .streamlit/

COPY main.py .

EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]