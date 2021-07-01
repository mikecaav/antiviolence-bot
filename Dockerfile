FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime
RUN apt-get update
RUN apt-get -y install git git-lfs
RUN git clone https://github.com/mikecaav/antiviolence-bot.git
WORKDIR antiviolence-bot
RUN pip3 install -r requirements-docker.txt
RUN git lfs install
RUN git clone https://huggingface.co/cardiffnlp/twitter-roberta-base-emotion
CMD ["python3", "bot.py"]