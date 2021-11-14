from flask import Flask, render_template
from DB import Database
from flask import request
import time

app = Flask(__name__)
@app.route('/'.methods=['GET','POST'])
def index():
    if request.method == 'GET':
        db=Database()
        sql_all=db.show()
        print(sql_all)
        return render_template('index.html', list =sql_all)
    if __name__ == '__main__':
        app.rum(host='127.0.0.1',port= 5000, debug='True')

