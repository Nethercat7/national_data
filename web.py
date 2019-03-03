from flask import Flask, render_template, request, jsonify
from py import query, get_data

app=Flask(__name__,template_folder='web',static_folder='static')

@app.route('/')
def index():
    try:
        if not query.data2017().count()&query.data2016().count()&query.data2015().count()&query.data2014().count()\
                &query.data2013().count()&query.enrollment_rate().count()&query.students_rate().count()\
                &query.graduate_rate().count()&query.gae2017().count()&query.gae2016().count()\
                &query.gae2015().count()&query.gae2014().count()&query.gae2013().count()\
                &query.population().count()&query.sip2017().count()&query.sip2016().count() \
                & query.sip2015().count()&query.sip2014().count()&query.sip2013().count():
            get_data.insert()
        else:
            pass
    finally:
        return render_template('index.html')

#各年份的学生数据
@app.route('/data2017',methods=['GET','POST'])
def data2017():
    if request.method=='POST':
        data= query.data2017()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/data2016',methods=['GET','POST'])
def data2016():
    if request.method=='POST':
        data= query.data2016()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/data2015',methods=['GET','POST'])
def data2015():
    if request.method=='POST':
        data= query.data2015()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/data2014',methods=['GET','POST'])
def data2014():
    if request.method=='POST':
        data= query.data2014()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/data2013',methods=['GET','POST'])
def data2013():
    if request.method=='POST':
        data= query.data2013()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'

#招生、在校、毕业人数增长率
@app.route('/enrollmentRate',methods=['GET','POST'])
def enrollment_rate():
    if request.method=='POST':
        data=query.enrollment_rate()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/studentsRate',methods=['GET','POST'])
def sutdents_rate():
    if request.method=='POST':
        data=query.students_rate()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/graduateRate',methods=['GET','POST'])
def graduate_rate():
    if request.method=='POST':
        data=query.graduate_rate()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'

#各年份的高中职毕业生数和专本科招生数
@app.route('/gae2017',methods=['GET','POST'])
def gae2017():
    if request.method=='POST':
        data= query.gae2017()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/gae2016',methods=['GET','POST'])
def gae2016():
    if request.method=='POST':
        data= query.gae2016()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/gae2015',methods=['GET','POST'])
def gae2015():
    if request.method=='POST':
        data= query.gae2015()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/gae2014',methods=['GET','POST'])
def gae2014():
    if request.method=='POST':
        data= query.gae2014()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/gae2013',methods=['GET','POST'])
def gae2013():
    if request.method=='POST':
        data= query.gae2013()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'

#各年份的总人口中的在校生占比
@app.route('/sip2017',methods=['GET','POST'])
def sip2017():
    if request.method=='POST':
        data= query.sip2017()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/sip2016',methods=['GET','POST'])
def sip2016():
    if request.method=='POST':
        data= query.sip2016()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/sip2015',methods=['GET','POST'])
def sip2015():
    if request.method=='POST':
        data= query.sip2015()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/sip2014',methods=['GET','POST'])
def sip2014():
    if request.method=='POST':
        data= query.sip2014()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'
@app.route('/sip2013',methods=['GET','POST'])
def sip2013():
    if request.method=='POST':
        data= query.sip2013()
        results=[]
        for i in data:
            results.append(i)
        return jsonify(results)
    else:
        return 'request error'

if __name__=='__main__':
    app.run()