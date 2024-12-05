from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

# Ensure Flask doesn't run within Streamlit
if __name__ == "__main__":
    app.run(debug=True)
