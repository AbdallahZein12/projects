FROM python:3.10 

ARG LYRICA_BOT
ARG LYRICA_YT

ENV LYRICA_BOT=${LYRICA_BOT}
ENV LYRICA_YT=${LYRICA_YT}


WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y ffmpeg 

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && apt-get update -y && apt-get install google-cloud-cli -y

COPY service-account-key.json /root/.config/gcloud/service-account-key.json

RUN gcloud auth activate-service-account --key-file=/root/.config/gcloud/service-account-key.json

COPY . /app

CMD ["python3","main.py"] 
