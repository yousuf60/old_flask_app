from flask import Flask ,redirect,flash,render_template ,request ,make_response , jsonify
import socket
import time
import json
import multiprocessing
import random

path='/home/yousuf123/mysite/data/data.js'
path2="/home/yousuf123/mysite/topics.js"
path3="/home/yousuf123/mysite/messages.js"
server=socket.socket()
server.bind(("",1414))
server.listen(1)
class crt:
	data=json.loads(open(path).read())


	def search(self,n,n2,p):
		try:
			x=self.data['data'][n]
			if x[0]==n2:
				if x[1]==p:
					print(n)
					return x[2]
				else:
					return 1
			else:return 1
		except:
			return 1
DB=crt()

def thr():
	while True:
	    time.sleep(40000)
	    x=str(random.randint(1,100))
	    x1=str(random.randint(1,100))
	    x2=str(random.randint(1,200))
	    c=random.randint(1,2)
	    if c==1:sing=["$_$","@_@","!_!"]
	    elif c==2:sing=["^---^","^_^","+!@"]
	    else:sing=["^---^","^_^","+!@"]
	    x3=f"{sing[0]}{x}{x1}_A_{x2}{sing[1]}{sing[2]}"
	    open(path,"w").write('{"data":{"yousuf":["yoyo_YOYO_yoyo","pP1P","%s"]},"ids_data":{"%s":["",""]}}'%(x3,x3))
	    open(path2,'w').write("{}")
	    open(path3,"w").write("""{"messages":[]}""")





first_pr=multiprocessing.Process(target=thr)
first_pr.start()
#####
########
app=Flask(__name__)
app.config['SECRET_KEY']=';saj;'
@app.route('/',methods=['GET','POST'])
def main():
	x=json.loads(open(path2).read())
	flash('hello and welcome',category='yes')

	if request.cookies.get("usr") in DB.data["ids_data"]:

		allow="yes"
	else:
		allow="no"
	if request.method=='POST':

		Any=request.form['ANY']

		if Any and len(Any)>1000:
			flash('too much',category='no')

		elif Any and len(Any)<=20:
			flash('type more',category='no')
		elif Any:
			if Any not in x.values():
			    ln=len(x.keys())
			    x[str(ln+random.randint(2,100)+random.random())+'main']=Any
			    json.dump(x,open(path2,'w'))





	return render_template('main.html',k=x,a=allow)
@app.route('/admin_page_for_admins',methods=['GET','POST'])
def admin():
	if request.method=="POST":
		name=request.form['name']
		email=request.form['email']
		password=request.form['password']
		z=DB.search(name,email,password)
		print(z)
		if z !=1:


			x=make_response(redirect("/"))
			x.set_cookie("usr",z)
			return x



	return render_template("admin.html")
@app.route("/delete/<name>",methods=["POST"])
def delete(name):
    if request.cookies.get("usr") in DB.data["ids_data"] or request.form['usr']in DB.data["ids_data"]:
    	x=json.loads(open(path2).read())

    	if name in x.keys():
    		del x[name]
    		json.dump(x,open(path2,'w'))
    		print(x)
    	return redirect('/')
@app.route("/api/admin_app",methods=["POST","GET"])
def admin_app():
	x=json.loads(open(path2).read())
	ok=False
	if request.form['usr']in DB.data["ids_data"]:ok=True
	elif request.cookies.get("usr") in DB.data["ids_data"]:ok=True
	else:ok=False

	if ok:

		if "ANY" in request.form :
			Any=request.form['ANY']

			if len(Any)>1000:
					x="its too much"
			elif len(Any)<20:
					x="its too small"
			elif Any not in x.values():
				ln=len(x.keys())

				x[str(ln+random.randint(2,100)+random.random())+'admin_app']=Any
				json.dump(x,open(path2,'w'))
			print(request.form)
			return jsonify(dict(x))
		if "del" in request.form :
			dl=request.form["del"]
			if dl =="all" :
				x.clear()
				open(path2,'w').write("{}")

			else:
				try:
					del x[dl]
					json.dump(x,open(path2,'w'))
				except:pass

			return jsonify(dict(x))
		else:return jsonify(dict(x))
	elif request.method=="GET":return jsonify(dict(x))
	return "empty"
@app.route("/api/user",methods=['POST','GET'])
def usr():
    x=json.loads(open(path2).read())
    ln=len(x.keys())
    if request.method=="POST":
        an=request.form["ANY"]


        print(an)
        if an not in x.values():
            x[str(ln+random.randint(2,100)+random.random())+'user_app']=an

            json.dump(x,open(path2,'w'))
            print(x)
        return jsonify(dict(x))
    return jsonify(x)
@app.route("/api/admin_app_login",methods=['POST','GET'])
def ad_log():
	if request.method=="POST":
		name=request.form['name']
		email=request.form['email']
		password=request.form['password']
		z=DB.search(name,email,password)
		print(z)
		if z !=1:


			x=make_response(z)
			x.set_cookie("usr",z)
			return x
@app.route("/api/messages",methods=["POST","GET"])
def mesaage():
    x=json.loads(open(path3).read())
    if request.method=="POST":
        me=request.form["message"]
        x["messages"].append(me)
        json.dump(x,open(path3,'w'))


if __name__ == '__main__':

    app.run()