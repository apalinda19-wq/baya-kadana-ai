from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "ඔයාට පුළුවන්!",
    "අද දවස සුබයි", 
    "හිනාවෙන් ඉන්න",
    "කඩන බය අයින් කරපන්",
    "උත්සාහය ජය උදා කරයි"
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run()
