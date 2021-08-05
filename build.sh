FILE=twitter-roberta-base-emotion/pytorch_model.bin

apt-get -y install git-lfs
git lfs install

if test -f "$FILE"; then
  echo "$FILE exists."
else
  echo "$FILE doesn't exists, downloading files..."
  git clone https://huggingface.co/cardiffnlp/twitter-roberta-base-emotion
  echo "$FILE is now downloaded"
fi

docker build -t mikex40/antiviolence-bot -f Dockerfile .
