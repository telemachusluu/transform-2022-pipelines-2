FROM python:3.10.4-slim-buster
RUN apt update && apt upgrade -y && rm -rf /var/lib/apt/lists
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --requirement requirements.txt && rm requirements.txt
EXPOSE 5000
RUN mkdir /app
COPY project /app
ENV FLASK_ENV=development
ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0
