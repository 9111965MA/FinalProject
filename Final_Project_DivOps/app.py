from flask import Flask , redirect ,render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class EmployeeModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))
 
    def __init__(self, employee_id,name,age,position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position
 
    def __repr__(self):
        return f"{self.name}:{self.employee_id}"

#from flask import Flask,render_template,request,redirect
#from models import db,EmployeeModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

#@app.route('/')
#def root():
#    return redirect(url_for('/data'))
 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage1.html')
 
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position = position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/')
 
@app.route('/')
def front():
    return render_template('front.html')

@app.route('/data')
def RetrieveList():
    employees = EmployeeModel.query.all()
    return render_template('datalist3.html',employees = employees)
 
 
@app.route('/data/<int:id>')
def RetrieveEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data2.html', employee = employee)
    return f"Employee with id ={id} Doenst exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(employee_id=id, name=name, age=age, position = position)
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Doesn't exist"
 
    return render_template('update2.html', employee = employee)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        #abort(404)
 
    return render_template('delete2.html')
 
#app.run(host='localhost', port=5000)
app.run(debug = True, host = '0.0.0.0', port=5000)
