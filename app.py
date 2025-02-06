from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Home():
    return render_template("index.html")


if __name__=="__main__": #this will be used to run the code continusly in the back end#
    app.run()