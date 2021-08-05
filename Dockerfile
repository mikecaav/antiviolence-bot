FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime
RUN apt-get update
RUN apt-get -y install git
RUN git clone https://github.com/mikecaav/antiviolence-bot.git
WORKDIR antiviolence-bot
COPY . ./twitter-roberta-base-emotion
RUN pip3 install -r requirements-docker.txt
CMD ["python3", "bot.py"]