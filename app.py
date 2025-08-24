from flask import Flask, request, jsonify, render_template
import pickle
import traceback

# Initialize Flask
app = Flask(__name__, template_folder="website")

# Load Vectorizer
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load Model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # If JSON request
        if request.is_json:
            data = request.get_json()
            review_text = data.get("review", "")
        else:
            # If form request
            review_text = request.form.get("review", "")

        # Validate
        if not review_text.strip():
            return jsonify({"error": "No review provided"}), 400

        # Transform text
        X = vectorizer.transform([review_text])

        # Predict
        prediction = model.predict(X)
        score = int(prediction[0]) if len(prediction) > 0 else None

        return jsonify({"score": score})

    except Exception as e:
        print("❌ Backend error:", traceback.format_exc())
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
