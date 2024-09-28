from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def fun():
    return render_template('Portfoilio.html')

@app.route('/a')
def fc():
    return render_template('Aboutp.html')

@app.route('/b')
def dun():
    return render_template('Skills.html')

@app.route('/c')
def sin():
    return render_template('Projectsp.html')

@app.route('/d')
def suv():
    return render_template('Resume.html')

@app.route('/e')
def ain():
    return render_template('Contactp.html')

app.run(debug=True,port=48943)