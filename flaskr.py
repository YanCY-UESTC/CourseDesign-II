from flask import *
from werkzeug.utils import secure_filename
import sqlite3
import os
import time



app = Flask('__name__')

def user_identity(user, password):
	if (user=='') or (password==''):
		return 2
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
		return -1
	else:
		if password==pwd:
			return 1
		else:
			return 0

def user_create(user,password):
	timer=int(time.time())
	rv=sqlite3.connect('test.db')
	c=rv.cursor()
	ss='''insert into user values ('%d','%s','%s');'''%(timer,user,password)
	c.execute(ss)
	rv.commit()
	rv.close()

def login_cookies_check():
	try:
		name=request.cookies.get('name')
		#pwd=request.cookies.get('password')
	except KeyError:
		print("KeyError")
		return False
	else:
		if name == None:
			return False
		else:
			return True

@app.route('/',methods=["GET","POST"])
@app.route('/index',methods=["GET","POST"])
def index():
	return render_template("index.html")


@app.route('/login',methods=["GET","POST"])
def login():
	if request.method=='GET':
		failed='用户登录'
		return render_template('login.html',failed=failed)
	else:
		print(request.form)
		username = request.form.get('username')
		userpwd = request.form.get('password')
		if(user_identity(username,userpwd)==1):
			newresponce=make_response(redirect(url_for('input')))
			newresponce.set_cookie('name',username)
			#newresponce.set_cookie('password',userpwd)
			return newresponce
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
		identity=user_identity(username,userpwd)
		if(identity==-1):
			user_create(username,userpwd)
			return redirect(url_for('index'))
		elif(identity==2):
			failed="账户和密码不能为空！请重新设置"
			return render_template('login.html',failed=failed)
		else:
			failed='账户已存在，请采用其他用户名'
			return render_template('login.html',failed=failed)

@app.route('/logout',methods=['GET','POST'])
def logout():
	newresponce=make_response(redirect(url_for('index')))
	newresponce.set_cookie('name','',expires=0)
	return newresponce



@app.route('/input',methods=["GET","POST"])
def input():
	step=1
	if request.method == "POST":
		step=2
		f = request.files['filename']
		basepath = os.path.dirname(__file__)
		uploadpath=os.path.join(basepath,'userfile',f.filename)
		f.save(uploadpath)
		return redirect(url_for('var'))#redirect(url_for('input'))
	else:
		if login_cookies_check():
			print(request.cookies.get('name'))
			return render_template('input.html',step=step)
		else:
			return redirect(url_for('login'))

@app.route('/var',methods=["GET","POST"])
def var():
	if request.method == "POST":
		newresponce=make_response(redirect(url_for('input')))
		return newresponce
	else:
		if login_cookies_check():
			print(request.cookies.get('name'))
			return render_template('var.html')
		else:
			return redirect(url_for('login'))

@app.route('/result',methods=["POST","GET"])
def result_show():
	step=3
	if request.method == "POST":
		k=request.form.get('K')
		newresponce=make_response(url_for('result'))
	return url_for('result')

if __name__ == '__main__':
	#app.debug=True
	app.run(host='0.0.0.0',port='80')
