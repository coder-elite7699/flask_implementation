from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/passed')
def passed():
    return render_template('passed.html')

@app.route('/failed')
def failed():
    return render_template('failed.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        sub1 = int(request.form['pyt'])
        sub2 = int(request.form['php'])
        sub3 = int(request.form['cpp'])
        sub4 = int(request.form['java'])
        sub5 = int(request.form['assem'])
        total_score = sub1+sub2+sub3+sub4+sub5
    res=""
    if total_score>=250:
        res="passed"
    else:
        res="failed"
    return redirect(url_for(res))

if __name__=="__main__":
    app.run(debug=True)