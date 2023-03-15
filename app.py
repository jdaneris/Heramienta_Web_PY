from flask import Flask,render_template,url_for,redirect,request


app = Flask(__name__)

@app.route('/')
def index():
    print('index')
    return render_template('index.html')


@app.route('/K_Means')
def k_means():
    return render_template('K_Means.html')

@app.route('/Power_BI')
def power_BI():
    return render_template('Power_BI.html')




if __name__ == '__main__':
    app.run(debug=True)