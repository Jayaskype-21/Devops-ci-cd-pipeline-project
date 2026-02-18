from flask import Flask, jsonify

app = Flask(__name__)

grocery_items = [
    {"id": 1, "name": "Rice", "price": 50},
    {"id": 2, "name": "Milk", "price": 200},
    {"id": 3, "name": "Sugar", "price": 300}
]

@app.route("/")
def home():
    items_html = ""
    for item in grocery_items:
        items_html += f"""
        <li class="item">
            <span class="name">{item['name']}</span>
            <span class="price">₹{item['price']}</span>
        </li>
        """

    return f"""
    <html>
        <head>
            <title>Online Grocery Store</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f8;
                    margin: 0;
                    padding: 0;
                }}

                .container {{
                    width: 50%;
                    margin: 50px auto;
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                }}

                h1 {{
                    text-align: center;
                    color: #2c3e50;
                }}

                p {{
                    text-align: center;
                    color: #555;
                }}

                ul {{
                    list-style: none;
                    padding: 0;
                }}

                .item {{
                    display: flex;
                    justify-content: space-between;
                    padding: 12px;
                    margin: 10px 0;
                    background: #e8f5e9;
                    border-left: 6px solid #4caf50;
                    border-radius: 5px;
                    font-size: 18px;
                }}

                .name {{
                    font-weight: bold;
                    color: #2e7d32;
                }}

                .price {{
                    color: #1b5e20;
                }}

                a {{
                    display: block;
                    text-align: center;
                    margin-top: 20px;
                    text-decoration: none;
                    color: white;
                    background: #4caf50;
                    padding: 10px;
                    border-radius: 5px;
                }}

                a:hover {{
                    background: #43a047;
                }}
            </style>
        </head>

        <body>
            <div class="container">
                <h1>🛒 Online Grocery Store</h1>
                <p>Fresh items with updated prices</p>

                <ul>
                    {items_html}
                </ul>

                <a href="/items">View Items API</a>
            </div>
        </body>
    </html>
    """

@app.route("/items")
def items():
    return jsonify(grocery_items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
