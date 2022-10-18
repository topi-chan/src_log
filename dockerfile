FROM python:3.10.5-bullseye

RUN apt-get update && apt-get install

COPY data_io.py main.py operations.py requirements.txt ./

WORKDIR /log_app

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "main.py"]
