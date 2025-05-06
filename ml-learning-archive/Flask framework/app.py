#Basic skeleton of Flask framework


from flask import Flask

'''Web server gateway interface-WSGI(creates an instance of Flask class)'''
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return 'Hi, How are you?'

@app.route("/index")
def function():
    return 'Welcome to this screen'

'''creating entry point'''
if __name__=="__main__":
    app.run(debug=True)