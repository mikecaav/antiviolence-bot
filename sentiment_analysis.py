from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request


def get_labels():
    mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/emotion/mapping.txt"
    with urllib.request.urlopen(mapping_link) as f:
        html = f.read().decode('utf-8').split("\n")
        csvreader = csv.reader(html, delimiter='\t')
    return [row[1] for row in csvreader if len(row) > 1]


def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


class SentimentAnalysisModel:
    def __init__(self):
        self.MODEL = "twitter-roberta-base-emotion"
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL)
        self.labels = get_labels()
        self.model = self.init_model()

    def init_model(self):
        return AutoModelForSequenceClassification.from_pretrained(self.MODEL)

    def get_scores(self, text):
        text = preprocess(text)
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        for i in range(scores.shape[0]):
            label = self.labels[ranking[i]]
            score = scores[ranking[i]]
            probability = np.round(float(score), 4)
            print(f"{i + 1}) {label} {probability}")




if __name__ == "__main__":
    model = SentimentAnalysisModel()
    model.get_scores("Cannot believe that you're saying that 🙄")
