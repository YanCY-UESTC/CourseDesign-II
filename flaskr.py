from flask import *
from werkzeug.utils import secure_filename
import sqlite3
import os
import time
import xlrd ###
import zipfile
import kmeans_modules as km  ##

static_filetail=['.xls','.xlsx']

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


def createZip(filePath, savePath):
	'''
    将文件夹下的文件保存到zip文件中。
    :param filePath: 待备份文件
    :param savePath: 备份路径
    :param note: 备份文件说明
    :return:
    '''
	fileList = []
	target = 'download.zip'
	newZip = zipfile.ZipFile(savePath + os.sep + target, 'w')
	for dirpath, dirnames, filenames in os.walk(filePath):
		for filename in filenames:
			fileList.append(os.path.join(dirpath, filename))
	for tar in fileList:
		newZip.write(tar, tar[len(filePath):])  # tar为写入的文件，tar[len(filePath)]为保存的文件名
	newZip.close()
	print('backup to', target)

#获取当前时间
def time_output():
	 return "%d/%d/%d_%d/%d/%d"%(time.localtime(time.time())[0:6])#年.月.日_时:分:秒

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
	if request.method == "POST":
		try:
			f = request.files['filename']###
			if (f != ""):
				basepath = os.path.dirname(__file__)
				name_tail = os.path.splitext(f.filename)[1]#获取文件后缀名
				print(name_tail)
				'''
				检查上传文件是否为可以处理的.xls或.xlsx文件
				'''
				if name_tail in static_filetail:
					this_time=time_output()
					file_name="%s_%s%s"%(this_time,request.cookies.get('name'),name_tail)
					uploadpath = os.path.join(basepath, 'static/userfile', file_name)
					f.save(uploadpath)
					k = request.form.get("radioValue")
					newresponce=make_response(redirect(url_for('result')))
					newresponce.set_cookie('k',str(k))
					newresponce.set_cookie('filename',file_name)
					return newresponce  # redirect(url_for('input'))
				else:
					file = "请上传类型正确的文件(.xls/.xlsx)"
					return render_template('input.html', file = file)
		except:#抓到keyerror
			file = "处理文件不得为空"
			print(file)
			print(request.cookies.get('name'))
			return render_template('input.html',file = file)#显示选择正确文件
	else:
		if login_cookies_check():
			print(request.cookies.get('name'))
			file = "分析准备"
			return render_template('input.html', file = file)
		else:
			return redirect(url_for('login'))

# @app.route('/var',methods=["GET","POST"])
# def var():
# 	if request.method == "POST":
# 		newresponce=make_response(redirect(url_for('input')))
# 		return newresponce
# 	else:
# 		if login_cookies_check():
# 			print(request.cookies.get('name'))
# 			return render_template('var.html')
# 		else:
# 			return redirect(url_for('login'))

@app.route('/result',methods=["GET","POST"])
def result():
	#登录检测
	if login_cookies_check():
		pass
	else:
		return redirect(url_for('login'))
	# step=3
	# if request.method == "POST":
	# 	newresponce=make_response(url_for('result'))
	# return url_for('result')
	#success = "false"
	###kmeans'程序运行成功，
	success = "true"
	data = xlrd.open_workbook("static/userfile/download/kmeans_result.xlsx")
	table = data.sheet_by_index(0)
	nrows = table.nrows
	ncols = table.ncols
	tList = [([0] * ncols) for i in range(nrows)]
	for i in range(1,nrows):
		for j in range(ncols):
			if isinstance(table.cell(i, j).value,float):
				tList[i][j] = round(table.cell(i, j).value,4)
			else:
				tList[i][j] = table.cell(i, j).value
	for i in range(1,nrows):
		for j in range(1,nrows - i):
			if tList[j][0] > tList[j+1][0]:
				tList[j],tList[j+1] = tList[j+1],tList[j]
	for i in range(1,nrows):
		for j in range(ncols):
			temp = str(tList[i][j])
			tList[i][j] = temp.rstrip('0').strip('.') if '.' in temp else temp
	createZip("static/userfile/download", "static/userfile")
	return render_template("result.html",ncols = ncols, nrows = nrows, tList = tList, success = success)

if __name__ == '__main__':
	print(time_output())
	#app.debug=True
	app.run(host='127.0.0.1',port='5000', debug=True, threaded=True)
