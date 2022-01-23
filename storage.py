import csv
all_articles = []
with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allarticles = data[1:]

liked_articles = []
not_liked_articles = []