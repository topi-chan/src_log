FROM python:3.10.5-bullseye

RUN apt-get update && apt-get install

COPY logs_app ./logs_app

COPY requirements.txt .

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "/logs_app/main.py"]
