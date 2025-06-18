from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    menu_items = [
        {"name": "Pizza", "price": "R80"},
        {"name": "Burger", "price": "R60"},
        {"name": "Pasta", "price": "R90"}
    ]
    return render_template('menu.html', menu=menu_items)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        guests = request.form['guests']
        date = request.form['date']
        flash(f'Thank you {name}, your booking for {guests} guests on {date} is confirmed!')
        return redirect(url_for('booking'))
    return render_template('booking.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
