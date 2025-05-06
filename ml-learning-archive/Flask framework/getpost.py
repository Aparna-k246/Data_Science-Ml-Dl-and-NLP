#http scope




from flask import Flask,render_template,request

'''Web server gateway interface-WSGI(creates an instance of Flask class)'''
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return '<html><H1>Welcome to this screen</H1></html'

@app.route("/index",methods=['GET'])
def function():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

'''creating entry point'''
if __name__=="__main__":
    app.run(debug=True)