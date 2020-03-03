from flask import Flask,request

app = Flask (__name__)

@app.route ("/")
def ali ():
    name = request.args.get ("name")
    return ("Hello " + ame)
app.run (debug=True)
