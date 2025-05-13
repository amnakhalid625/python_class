from flask import Flask ,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def About():
    return  render_template('about.html')

@app.route("/products")
def products():
    return  render_template('product-shop.html')

if __name__ == "__main__":
    app.run(debug=True)


