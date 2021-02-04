from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def hello_world():
    name='wu'
    return f'Hello World!{name}'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/source')
def source():
    dataList=[]
    con=sqlite3.connect("test.db")
    cur=con.cursor()
    sql="select * from movie250"

    data=cur.execute(sql)
    for row in data:
        dataList.append(data)
    cur.close()
    con.close()
    print(dataList[0])
    return render_template('source.html',movies=dataList)


@app.route('/ec')
def echarts():


    return render_template('echarts.html')

if __name__ == '__main__':
    app.run()
