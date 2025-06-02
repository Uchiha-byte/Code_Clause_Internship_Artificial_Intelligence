# 🧠 Sentiment Analysis Tool (Python)

This is a simple Python project that uses **TextBlob** to detect the sentiment of text as **Positive**, **Negative**, or **Neutral**.

---

## 🎓 Internship Info

> ✅ This is my **first project** for **CodeClause** as an **AI Intern**.  
> It demonstrates basic Natural Language Processing (NLP) skills using Python.

---

## 📁 Files Included

- `Sentiment Analysis.py` — Main Python script  
- `sentiment-analysis-python.ipynb` — Jupyter notebook version

---

## 🚀 Features

- Takes a sentence or paragraph as input  
- Analyzes the sentiment polarity  
- Classifies the result as:
  - 😊 Positive  
  - 😠 Negative  
  - 😐 Neutral  
- Shows the sentiment **score**

---

## 🛠 Requirements

Install required libraries:

```bash
pip install textblob
python -m textblob.download_corpora
```

---

## ▶️ How to Run

Run the Python file:
```bash
python "Sentiment Analysis.py"
```

Or open the Jupyter notebook:
```bash
jupyter notebook sentiment-analysis-python.ipynb
```

---

## 🧪 Example Output

```
Sentence: I love this product, it's amazing!
Sentiment: Positive (Score: 0.625)

Sentence: The service was terrible, I'll never go back again.
Sentiment: Negative (Score: -1.0)

Sentence: I feel indifferent about the movie.
Sentiment: Neutral (Score: 0.0)
```

---

## 📚 Library Used

- [TextBlob](https://textblob.readthedocs.io/en/dev/) – simple NLP library for processing textual data.

---

## 📄 License

This project is licensed under the MIT License.
