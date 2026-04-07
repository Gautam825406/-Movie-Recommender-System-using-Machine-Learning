# 🎬 Movie Recommender System using Machine Learning

---

## 🚀 Live Demo

👉 **Streamlit App:**  
https://movierecomandersystem.streamlit.app/

👉 **Google Colab Notebook:**  
https://colab.research.google.com/drive/1JXBTEviqKzYgRQqmqSKHgrtuOaSYRbKW

---

## 📌 Overview

This project is a **content-based movie recommendation system** built using machine learning and NLP techniques.

It recommends movies based on similarity in:

- 🎭 Cast  
- 🎬 Director  
- 🎯 Keywords  
- 🎥 Genres  
- 📝 Overview  

The system uses **CountVectorizer + Cosine Similarity** to find similar movies.

---

## ⚙️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- NLTK  
- Streamlit  
- TMDB API  

---

## 🧠 How It Works

1. Load and merge movie datasets  
2. Extract important features (genres, keywords, cast, director)  
3. Clean and combine into a single column (`tags`)  
4. Convert text to vectors using CountVectorizer  
5. Compute similarity using cosine similarity  
6. Recommend top 5 similar movies  

---

## 🎯 Features

- 🔍 Content-based movie recommendation  
- 🎬 Movie posters using TMDB API  
- ⚡ Fast similarity search  
- 🎨 Interactive UI with Streamlit  
- 📊 Clean ML pipeline  

---

## 📂 Project Structure
# 🎬 Movie Recommender System using Machine Learning

---

## 🚀 Live Demo

👉 **Streamlit App:**  
https://movierecomandersystem.streamlit.app/

👉 **Google Colab Notebook:**  
https://colab.research.google.com/drive/1JXBTEviqKzYgRQqmqSKHgrtuOaSYRbKW

---

## 📌 Overview

This project is a **content-based movie recommendation system** built using machine learning and NLP techniques.

It recommends movies based on similarity in:

- 🎭 Cast  
- 🎬 Director  
- 🎯 Keywords  
- 🎥 Genres  
- 📝 Overview  

The system uses **CountVectorizer + Cosine Similarity** to find similar movies.

---

## ⚙️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- NLTK  
- Streamlit  
- TMDB API  

---

## 🧠 How It Works

1. Load and merge movie datasets  
2. Extract important features (genres, keywords, cast, director)  
3. Clean and combine into a single column (`tags`)  
4. Convert text to vectors using CountVectorizer  
5. Compute similarity using cosine similarity  
6. Recommend top 5 similar movies  

---

## 🎯 Features

- 🔍 Content-based movie recommendation  
- 🎬 Movie posters using TMDB API  
- ⚡ Fast similarity search  
- 🎨 Interactive UI with Streamlit  
- 📊 Clean ML pipeline  

---

## 📂 Project Structure
movie-recommender/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
└── README.md


---

## 🖥️ Installation & Run Locally


git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py

