from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def fun():
    return render_template('Landing.html')

@app.route('/a')
def fuc():
    return render_template('Homel.html')

@app.route('/b')
def ao():
    return render_template('Servicel.html')

@app.route('/c')
def sub():
    return render_template('Testimonials.html')

@app.route('/d')
def cd():
    return render_template('Contactl.html')

@app.route('/e')
def ki():
    return render_template('Aboutl.html')

app.run(debug=True,port=39482)