FROM python:3.10.5-bullseye

RUN apt-get update && apt-get install

WORKDIR /log_app

COPY data_io.py main.py operations.py requirements.txt ./

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "main.py"]
