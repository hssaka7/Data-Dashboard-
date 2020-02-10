from flask import Flask,render_template
import random

app = Flask(__name__)
print("Hello")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/datatable")
def getRandomData():
   context = {"title": "Data table test"}
   data = [{ 'id': i,
             'name': "test_name_{0}".format(random.randint(0,1000)),
             'phone': random.randint(2308,903234),
             'status': random.choice([1,2,3]),
             'href': "work in progress"
           } for i in range(0,500)]

   context['data'] = data
   return render_template('datatable/test_datatable.html', **context)

@app.route("/plot")
def testplot():
    return render_template("plots/test_plot.html")
app.run()