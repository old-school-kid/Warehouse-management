from  flask import Flask ,render_template,url_for,redirect,request,flash
import numpy as np
import pyrebase
import joblib
import sys

config ={
    "apiKey": "AIzaSyAy_-B05G2AYFrOi0FUQAMHrbew7zThnc8",
    "authDomain": "food-chain1.firebaseapp.com",
    "databaseURL": "https://food-chain1-default-rtdb.firebaseio.com",
    "projectId": "food-chain1",
    "storageBucket": "food-chain1.appspot.com",
    "messagingSenderId": "465892674183",
    "appId": "1:465892674183:web:9340d2c92f2b8d50f08622",
    "measurementId": "G-HSSJE3JW49"
}

firebase= pyrebase.initialize_app(config)

db=firebase.database()
##db.child("message to r from wh").push({"msg":"have u recived??"})
##for x in ok:
##    print(ok[x]["msg"])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route("/login",methods=['POST'])
def login():
    data=request.form
    if(data['username'].upper() == 'SUPPLIER' and data['password'] == '12345'):
        return redirect(url_for('Supplier'))
    elif(data['username'].upper() == 'RESTAURANT' and data['password'] == '12345'):
        return redirect(url_for('Restaurant'))
    elif(data['username'].upper() == 'WAREHOUSE' and data['password'] == '12345'):
        return redirect(url_for('Warehouse'))
    else:
        return redirect(url_for('home'))

@app.route("/Supplier")
def Supplier():
    ok1=db.child("message to wh from s").get()
    ok1=ok1.val()
    ok2=db.child("message to s from wh").get()
    ok2=ok2.val()
    return render_template('Supplier.html',info1=ok1, info2=ok2)


@app.route("/Warehouse")
def Warehouse():
    ok1=db.child("message to s from wh").get()
    ok1=ok1.val()
    ok2=db.child("message to r from wh").get()
    ok2=ok2.val()
    ok3=db.child("message to wh from r").get()
    ok3=ok3.val()
    ok4=db.child("message to wh from s").get()
    ok4=ok4.val()
    return render_template('Warehouse.html', info1=ok1, info2=ok2, info3=ok3, info4=ok4)


@app.route("/Restaurant")
def Restaurant():
    ok1=db.child("message to wh from r").get()
    ok1=ok1.val()
    ok2=db.child("message to r from wh").get()
    ok2=ok2.val()
    return render_template('Restaurant.html',info1=ok1, info2=ok2)


##message to warehouse from supplier
@app.route("/msgtowhfs",methods=['POST'])
def msgtowhfs():
    data=request.form
    db.child("message to wh from s").push({"msg":data["mtwfs"]})
    return redirect(url_for('Supplier'))


##message to supplier from warehouse
@app.route("/msgtosfwh",methods=['POST'])
def msgtosfwh():
    data=request.form
    db.child("message to s from wh").push({"msg":data["mtsfw"]})
    return redirect(url_for('Warehouse'))


##message to restaurant from warehouse
@app.route("/msgtorfwh",methods=['POST'])
def msgtorfwh():
    data=request.form
    db.child("message to r from wh").push({"msg":data["mtrfw"]})
    return redirect(url_for('Warehouse'))


##message to warehouse fron restaurant
@app.route("/msgtowhfr",methods=['POST'])
def msgtowhfr():
    data=request.form
    db.child("message to wh from r").push({"msg":data["mtwfr"]})
    return redirect(url_for('Restaurant'))




##Warehouse model form and display page

@app.route("/pp")
def wpp():
    return render_template('pp.html')


@app.route("/predict",methods=['POST'])
def predict():


    direct_input=[x for x in request.form.values()]

    model1 = joblib.load(open(direct_input[0]+'_'+direct_input[1]+'.sav', 'rb'))
    model2 = joblib.load(open(direct_input[0]+'_'+direct_input[1]+'2.sav', 'rb'))


    flt_features = [float(x) for x in request.form.values()]
    flt_features.append(flt_features[3]-flt_features[2])
    final_features1 = [np.array(flt_features[2:])]
    print(flt_features)
    print(final_features1)

    prediction1 = model1.predict(final_features1)
    output1 = round(prediction1[0])
    print(output1)

    flt_features.append(output1)
    final_features2 = [np.array(flt_features[2:])]
    prediction2 = model2.predict(final_features2)
    output2 = round(prediction2[0])
    print(output2)
    return redirect(url_for('wpp'))




if __name__ == "__main__":
    app.run(debug=True)