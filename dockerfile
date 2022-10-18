FROM python:3.10.5-bullseye

RUN apt-get update && apt-get install

COPY /logs_app/data_io.py /logs_app/main.py /logs_app/operations.py requirements.txt ./

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "main.py"]
