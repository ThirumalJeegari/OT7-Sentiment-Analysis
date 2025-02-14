from flask import Flask,render_template,request,jsonify
from test import TextToNum
import pickle

app = Flask(__name__)
@app.route("/")
def Home():
    return render_template("index.html")
@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")
        print(msg)

        cl = TextToNum(msg)
        cl.cleaner()
        cl.token()
        cl.removeStop()
        st = cl.stemme()
        stvc = " ".join(st)
        with open("vectorizer.pickle","rb") as vc_file:
            vectorizer =pickle.load(vc_file)
        dt = vectorizer.transform([stvc]).toarray()
        with open("model.pickle","rb") as mb_file:
            model = pickle.load(mb_file)
        pred = model.predict(dt)
        
        #return render_template("result.html")
        
        if pred[0]==1:
            pred = "Positive"
        elif pred[0]==0:
            pred = "Neutral"
        else:
            pred = "Negative"
            
        # prediction = str(pred[0])  # Convert prediction to string
        
        return render_template("result.html", prediction=pred)



    else:
        return render_template("predict.html")
    
    
if __name__ =="__main__":
    app.run(host="0.0.0.0",port=5050)





