from flask import Flask, jsonify, request
import csv

all_article = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_article = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_article[0],
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_movie():
    article = all_article[0]
    all_article = all_article[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_article[0]
    all_article = all_article[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201


if __name__ == "__main__":
  app.run()

