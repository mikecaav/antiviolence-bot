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


def get_scores(output):
    scores = output[0][0].detach().numpy()
    return softmax(scores)


class EmotionAnalysisModel:
    def __init__(self):
        self.MODEL = "twitter-roberta-base-emotion"
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL)
        self.labels = get_labels()
        self.model = self.init_model()

    def init_model(self):
        return AutoModelForSequenceClassification.from_pretrained(self.MODEL)

    def predict(self, text):
        text = preprocess(text)
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = get_scores(output)
        ranking = self.get_ranking(scores)
        return ranking[0]

    def show_results(self, text):
        prediction = self.predict(text)
        print(f"This text expresses {self.labels[prediction]}")

    def get_ranking(self, scores):
        ranking = np.argsort(scores)
        return ranking[::-1]

    def text_express_anger(self, text):
        prediction = self.predict(text)
        return prediction == 0


if __name__ == "__main__":
    model = EmotionAnalysisModel()
    print(model.text_express_anger("I'm not sure if I asked your opinion"))
