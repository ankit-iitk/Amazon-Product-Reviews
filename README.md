# 🛒 Amazon Product Reviews – Sentiment Analysis  

**Amazon Product Reviews Sentiment Analyzer** is a **Machine Learning-powered web application** that provides **real-time sentiment analysis** of Amazon product reviews. The application enables users to quickly gauge customer feedback and make informed decisions by predicting review ratings and displaying them as visual star ratings.

The project demonstrates **end-to-end deployment** of a machine learning model—from data preprocessing and model training in Python to integration with a Flask web application and deployment on Render.

🔗 **Live Demo**: [Amazon Product Reviews Web App](https://amazon-product-reviews-2.onrender.com/)  

---

## 📌 Features
- Enter or paste an Amazon product review
- Predicts sentiment using a trained ML model
- Flask backend with HTML templates
- Deployed on Render

---

## 📂 Project Structure

   ```bash
   ├── app.py # Flask application
   ├── amazon_product_reviews.ipynb # Jupyter notebook for training & exploration
   ├── requirements.txt # Dependencies
   │
   ├── model/ # Trained model files
   │ ├── model.pkl
   │ └── vectorizer.pkl
   │
   └── templates/ # HTML templates
   └── index.html
   ```
---

## ⚙️ Installation & Setup

1. **Clone the repository:**
     ```bash
     git clone https://github.com/ankit-iitk/Amazon-Product-Reviews.git
     cd Amazon-Product-Reviews
     ```
2. **Create & activate a virtual environment:**
      ```bash
      python -m venv venv
      source venv/bin/activate   # Mac/Linux
      venv\Scripts\activate      # Windows
      ```
3. **Install dependencies:**
      ```bash
      pip install -r requirements.txt
      ```
4. **Run the app locally:**
      ```bash
      python app.py
      ```
5. **Open in browser:**
      ```bash
      http://127.0.0.1:5000/
      ```
   
   

