#Variable Rule
#building url's dynamically
#Jinja2 template engine
'''
 {{ }} expressions to print output in html
 {%...%} condtions,for loops
 {#...#} single line comments'''





from flask import Flask,render_template,request,redirect,url_for

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


'''@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
    '''

#Variable rule
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=45:
        res="PASSED"
    else:
        res="FAILED"

    #return "The marks you got is, "+str(score)
    return render_template('result.html',results=res)

#Variable rule
@app.route("/successres/<int:score>")
def successRes(score):
    res=""
    if score>=45: 
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score, "res":res}

    #return "The marks you got is, "+str(score)
    return render_template('newresult.html',results=exp)

#if condition
@app.route("/successif/<int:score>")
def successif(score):
    res=""
    

    #return "The marks you got is, "+str(score)
    return render_template('result.html',results=score)


@app.route("/fail/<int:score>")
def fail(score):
    res=""
    

    #return "The marks you got is, "+str(score)
    return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successRes',score=total_score))


'''creating entry point'''
if __name__=="__main__":
    app.run(debug=True)