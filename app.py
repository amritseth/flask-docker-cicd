from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    team = [
        {'name': 'Alice Johnson', 'role': 'CEO', 'image': 'https://i.pravatar.cc/150?img=1'},
        {'name': 'Bob Smith', 'role': 'Developer', 'image': 'https://i.pravatar.cc/150?img=2'},
        {'name': 'Carol White', 'role': 'Designer', 'image': 'https://i.pravatar.cc/150?img=3'},
    ]
    return render_template('about.html', team=team)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash(f'Thanks {name}! Your message has been sent.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

