from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app=Flask(__name__)

model=pickle.load(open('sleep_disorderprediction1.pickle','rb'))

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        int_features=[x for x in request.form.values()]
        print(int_features)
        final = [np.array(int_features)]
        prediction = model.predict(final)
        if(prediction[0] == 0): return "No disorder"
        elif(prediction[0] == 1): return "Sleep apne error"
        else: return "Insomnia"
    else:
        return render_template('sleep.html')
if __name__ == '__main__':
    app.run(debug=True)