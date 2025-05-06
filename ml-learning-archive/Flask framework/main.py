#integrate html file with web framework




from flask import Flask,render_template

'''Web server gateway interface-WSGI(creates an instance of Flask class)'''
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return '<html><H1>Welcome to this screen</H1></html'

@app.route("/index")
def function():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

'''creating entry point'''
if __name__=="__main__":
    app.run(debug=True)