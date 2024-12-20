from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def homebutton():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/trustees')
def trustees():
    return render_template('trustees.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/survey')
def survey_reports():
    return render_template('survey_reports.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/publication')
def publication():
    return render_template('publication.html')

@app.route('/contact')
def contact():
    return render_template('contact_us.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)

