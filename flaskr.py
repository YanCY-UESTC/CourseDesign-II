from flask import *
from werkzeug.utils import secure_filename
import sqlite3
import os
import time


app = Flask('__name__')

def user_identity(user, password):
	rv=sqlite3.connect('test.db')
	c=rv.cursor()
	re=c.execute('''
		select password from user where name =?
		''',(user,))
	pwd=""
	try:
		pwd=c.fetchall()[0][0]
	except IndexError:
		print(pwd)
		rv.close()
		return False
	else:
		if password==pwd:
			return True
		else:
			return False

def user_create(user,password):
	timer=int(time.time())
	rv=sqlite3.connect('test.db')
	c=rv.cursor()
	ss='''insert into user values ('%d','%s','%s');'''%(timer,user,password)
	c.execute(ss)
	rv.commit()
	rv.close()



@app.route('/',methods=["GET","POST"])
@app.route('/login',methods=["GET","POST"])
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		print(request.form)
		username = request.form.get('username')
		userpwd = request.form.get('password')
		if(user_identity(username,userpwd)):
			return redirect(url_for('index'))
		else:
			failed='登录失败，请重新登录'
			return render_template('login.html', failed=failed)

@app.route('/newuser',methods=['GET','POST'])
def newuser():
	if request.method=='GET':
		failed='注册新用户'
		return render_template('login.html',failed=failed)
	else:
		print(request.form)
		username = request.form.get('username')
		userpwd = request.form.get('password')
		user_create(username,userpwd)
		return redirect(url_for('index'))

@app.route('/logout',methods=['GET','POST'])
def logout():
	return redirect(url_for('login'))

@app.route('/index',methods=["GET","POST"])
def index():
	return render_template("index.html")

@app.route('/input',methods=["GET","POST"])
def input():
	step=1
	if request.method == "POST":
		step=2
		f = request.files['filename']
		basepath = os.path.dirname(__file__)
		uploadpath=os.path.join(basepath,'userfile',f.filename)
		f.save(uploadpath)
		return render_template('input.html',step=step)#redirect(url_for('input'))
	return render_template('input.html',step=step)

if __name__ == '__main__':
	#app.debug=True
	app.run(host='0.0.0.0',port=80)
