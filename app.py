from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask inside Streamlit!"

if __name__ == "__main__":
    # Flask serverni Streamlitda ishga tushirmang!
    pass

