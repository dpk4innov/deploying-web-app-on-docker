from flask import Flask, render_template, request, redirect
import pymysql
import os
app = Flask(__name__)


os.system('/etc/init.d/mysql start')
my=pymysql.connect(host="localhost",user='root')
my.cursor().execute("create database if not exists users")
mysql=pymysql.connect(host="localhost",user='root',database="users")
cur = mysql.cursor()
cur.execute("drop table if exists user;")
cur.execute("create table user(ID Int,Name varchar(50),Age Int,Department varchar(50),Subject varchar(100),primary key(ID));")
cur.close()
@app.route('/user', methods=['GET', 'POST'])
def index():
	if request.method == 'POST' and 'submit' in request.form:
		userDetails = request.form
		id1= userDetails['id']
		name= userDetails['name']
		age=userDetails['age']
		dep=userDetails['dep']
		sub=userDetails['sub']
		if id1 and name and age and dep and sub:
			cur = mysql.cursor()
			value=cur.execute("SELECT * FROM user where ID=%s",(id1))
			if value==0:
				cur.execute("INSERT INTO user(ID,Name,Age,Department,Subject) VALUES(%s, %s,%s,%s,%s)",(id1,name,age,dep,sub))
				mysql.commit()
			else:
				return ("user already exists")

			resultValue = cur.execute("SELECT * FROM user")
			if resultValue > 0:
				userDetails = cur.fetchall()
				return render_template('users.html',userDetails=userDetails)
			cur.close()			
			return redirect('/user')
		else:
			return ("error while adding users")
	elif request.method == 'POST' and 'get' in request.form:
		cur = mysql.cursor()
		resultValue = cur.execute("SELECT * FROM user")
		if resultValue > 0:
			userDetails = cur.fetchall()
			return render_template('users.html',userDetails=userDetails)
		else:
			return("No Users")
		cur.close()
		return redirect('/user')	
			
	
	elif request.method == 'POST' and 'update' in request.form:
		userDetails = request.form
		id1= userDetails['id']
		name= userDetails['name']
		age=userDetails['age']
		dep=userDetails['dep']
		sub=userDetails['sub']
		if id1 and name and age and dep and sub:
			cur = mysql.cursor()
			value=cur.execute("SELECT * FROM user where ID=%s",(id1))
			if value>0:
				cur.execute("update user set Name=%s,Age=%s,Department=%s,Subject=%s where ID=%s",(name,age,dep,sub,id1))
				mysql.commit()
			else:
				return ("Wrong Id")			
			resultValue = cur.execute("SELECT * FROM user")
			if resultValue > 0:
				userDetails = cur.fetchall()
				return render_template('users.html',userDetails=userDetails)
			cur.close()
			return redirect('/user')
		else:
			return ("error while updating users")
	elif request.method == 'POST'and 'delete' in request.form:
		userDetails = request.form
		id1= userDetails['id']
		if not id1:
			return ("please provide id")
		cur = mysql.cursor()
		value=cur.execute("SELECT * FROM user where ID=%s",(id1))
		if value>0:
			cur.execute("delete from user where ID=%s",(id1,))
			mysql.commit()
		else:
			return ("user does not exist")
	
		resultValue = cur.execute("SELECT * FROM user")
		if resultValue > 0:
			userDetails = cur.fetchall()
			return render_template('users.html',userDetails=userDetails)
		else:
			return("No Users")
		cur.close()
		return redirect('/user')
		

	return render_template('index.html')

	
if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0",port=8080)
