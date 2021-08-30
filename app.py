from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///login.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class log(db.Model):
    sno = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(50) )
    password = db.Column(db.String(50) )

    def __repr__(self) -> str:
        return f"{self.sno} - {self.username}"


class assign(db.Model):
    a_sno = db.Column(db.Integer , primary_key=True)
    a_link = db.Column(db.String(50) )
    a_subject = db.Column(db.String(50) )
    a_date=db.Column(db.String(50))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.a_link}"


class test(db.Model):
    t_sno = db.Column(db.Integer , primary_key=True)
    t_link = db.Column(db.String(50) )
    t_subject = db.Column(db.String(50) )
    t_date=db.Column(db.String(50))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.t_link}"




@app.route("/")
def hello_world():
    return render_template("login.html")

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/assignment")
def home_assign():
    dets=assign.query.all()
    return render_template("assignments.html",dets=dets)

@app.route("/test")
def home_test():
    dets=test.query.all()
    return render_template("test.html",dets=dets)

@app.route("/calender")
def calenders():
    return render_template("calender.html")
    

@app.route("/adda" ,methods=['GET','POST'])
def add_assignment():
    if request.method=='POST':
        a_link=request.form.get('a_link')
        a_subject=request.form.get('a_subject')
        a_date=request.form.get('a_date')
        entry=assign(a_link=a_link,a_subject=a_subject,a_date=a_date)
        db.session.add(entry)
        db.session.commit()
        return redirect("/assignment")
    return render_template("addassign.html")

@app.route("/addt",methods=['GET','POST'])
def add_test():
    if request.method=='POST':
        t_link=request.form.get('t_link')
        t_subject=request.form.get('t_subject')
        t_date=request.form.get('t_date')
        entry=test(t_link=t_link,t_subject=t_subject,t_date=t_date)
        db.session.add(entry)
        db.session.commit()
        return redirect("/test")
    return render_template("addtest.html")

@app.route("/login" ,  methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username=="rupinvijan@gmail.com" and password=="password":
            return redirect("/info")
        
        else :
            dets=log.query.filter_by(username=username).first()
            if dets.password==password:
                return redirect("/index") 
            elif not dets.password==password :
                redirect("/signup") 
            
            

    return render_template("login.html")

@app.route("/signup" ,  methods=['GET','POST'])
def signup():
        
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        entry=log(username=username,password=password)
        db.session.add(entry)
        db.session.commit()
        return render_template("sign-up.html")         

    return render_template("sign-up.html")

@app.route("/logout")
def logout():
    
    return redirect("/login")

@app.route("/delete/<string:sno>" , methods=['GET','POST'])
def delete(sno):
    dets=log.query.filter_by(sno=sno).first()
    db.session.delete(dets)
    db.session.commit()
    return redirect("/login")



@app.route("/info",methods=['GET','POST'])
def info():
    dets=log.query.all()
    return render_template("info.html",dets=dets)

@app.route("/biotest",methods=['GET','POST'])
def bio_test():
    dets=test.query.filter_by(t_subject="biology")
    return render_template("biotest.html",dets=dets)


@app.route("/bioass",methods=['GET','POST'])
def bio_assignment():
    dets=assign.query.filter_by(a_subject="biology")
    return render_template("bioass.html",dets=dets)


@app.route("/phyass",methods=['GET','POST'])
def phy_assignment():
    dets=assign.query.filter_by(a_subject="physics")
    return render_template("phyass.html",dets=dets)


@app.route("/polass",methods=['GET','POST'])
def pol_assignment():
    dets=assign.query.filter_by(a_subject="political science")
    return render_template("polass.html",dets=dets)


@app.route("/compass",methods=['GET','POST'])
def comp_assignment():
    dets=assign.query.filter_by(a_subject="computer science")
    return render_template("compass.html",dets=dets)


@app.route("/phytest",methods=['GET','POST'])
def phy_test():
    dets=test.query.filter_by(t_subject="physics")
    return render_template("phytest.html",dets=dets)


@app.route("/poltest",methods=['GET','POST'])
def pol_test():
    dets=test.query.filter_by(t_subject="political science")
    return render_template("poltest.html",dets=dets)

@app.route("/comptest",methods=['GET','POST'])
def comp_test():
    dets=test.query.filter_by(t_subject="computer science")
    return render_template("comptest.html",dets=dets)


if __name__=="__main__":
    app.run(debug=True)