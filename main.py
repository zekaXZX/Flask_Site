from flask import Flask, render_template

app = Flask(__name__)


@app.route('/project-1')
def index():
    return render_template('index.html')


@app.route('/project-2')
def speed_test():
    return render_template('project-2.html')


@app.route('/project-3')
def project_3():
    return render_template('project-3.html')


@app.route('/home')
def home_page():
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
