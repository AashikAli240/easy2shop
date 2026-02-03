from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "super-secret-key"  # change in production

# Dummy products
PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 199, "img": "https://via.placeholder.com/300"},
    {"id": 2, "name": "Smart Watch", "price": 149, "img": "https://via.placeholder.com/300"},
    {"id": 3, "name": "Gaming Mouse", "price": 59, "img": "https://via.placeholder.com/300"},
    {"id": 4, "name": "Mechanical Keyboard", "price": 129, "img": "https://via.placeholder.com/300"},
]

def get_cart():
    if "cart" not in session:
        session["cart"] = []
    return session["cart"]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    return render_template("products.html", products=PRODUCTS)

@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    cart = get_cart()
    for p in PRODUCTS:
        if p["id"] == product_id:
            cart.append(p)
            break
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    cart = get_cart()
    total = sum(item["price"] for item in cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/clear-cart")
def clear_cart():
    session["cart"] = []
    return redirect(url_for("cart"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
