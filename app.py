from flask import Flask, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

# --- Configuration & Assets ---

# A modern, clean HTML/CSS template embedded directly
PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Serenity Flask</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');

        :root {
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --bg-gradient: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            --card-bg: rgba(255, 255, 255, 0.95);
            --text-main: #1e293b;
            --text-sub: #64748b;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: 'Outfit', sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: var(--bg-gradient);
            color: var(--text-main);
        }

        .container {
            text-align: center;
            background: var(--card-bg);
            padding: 3rem;
            border-radius: 24px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            max-width: 400px;
            width: 90%;
            transition: transform 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .container:hover {
            transform: translateY(-5px);
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
            background: -webkit-linear-gradient(45deg, #6366f1, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        p.subtitle {
            color: var(--text-sub);
            font-size: 1.1rem;
            margin-bottom: 2rem;
            line-height: 1.6;
        }

        .quote-box {
            background: #f1f5f9;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            border-left: 4px solid var(--primary);
            text-align: left;
        }

        .quote-text {
            font-style: italic;
            color: #334155;
            font-size: 0.95rem;
        }

        .btn {
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 12px 32px;
            font-size: 1rem;
            font-weight: 500;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            box-shadow: 0 4px 6px -1px rgba(99, 102, 241, 0.4);
        }

        .btn:hover {
            background-color: var(--primary-hover);
            box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.5);
            transform: scale(1.05);
        }
        
        footer {
            margin-top: 2rem;
            font-size: 0.8rem;
            color: #94a3b8;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ greeting }}</h1>
        <p class="subtitle">Welcome to your minimal Flask space. Everything you see here is contained in a single file.</p>
        
        <div class="quote-box">
            <p class="quote-text">"{{ quote }}"</p>
        </div>

        <a href="/" class="btn">New Inspiration</a>
        
        <footer>Server Time: {{ time }}</footer>
    </div>
</body>
</html>
"""

# --- Data ---

quotes = [
    "Simplicity is the ultimate sophistication.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Make it work, make it right, make it fast.",
    "The best way to predict the future is to invent it.",
    "Beauty varies, but simplicity is constant."
]

# --- Routes ---

@app.route('/')
def home():
    # Determine greeting based on time of day
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    return render_template_string(
        PAGE_TEMPLATE, 
        greeting=greeting, 
        quote=random.choice(quotes),
        time=datetime.now().strftime("%H:%M")
    )

if __name__ == '__main__':
    app.run(debug=True)
