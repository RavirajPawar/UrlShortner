FROM python:3.8-slim-buster

WORKDIR /url_ashortner_app

copy . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py"]



