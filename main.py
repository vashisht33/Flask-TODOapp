import sqlite3 as lit
from flask import Flask, render_template,request
import datetime
import sqlite



sqlite.main()
app = Flask(__name__)
@app.route('/')
def Index():
    return render_template("home.html")


@app.route('/enternew')
def new():
    return render_template("emp.html")


@app.route('/addrec',methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            id = request.form['id']
            nm = request.form['nm']
            ema = request.form['ema']
            ph = request.form['ph']


            with lit.connect("Crud.db") as con:
                cur = con.cursor()
                msg = "Record added successfully-200"
                cur.execute("Insert into emp1 (ID,Name,email,Phone) values(?,?,?,?)",(id,nm,ema,ph))
                con.commit()

        except:
            con.rollback()
            msg = "Record already exist with associated ID!"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route("/Retrieve")
def ret():
        return render_template("Ret.html")

@app.route("/Retrieve2",methods =['GET','POST'])
def retro():
    try:

        if request.method == 'POST':

            id = request.form['id']
            db = lit.connect("Crud.db")
            db.row_factory = lit.Row
            cur = db.cursor()
            cur.execute("Select * from emp1 where ID = ?",id)
            msg = 'Success - 201'
            rows = cur.fetchall()
            return render_template("Ret2.html", rows=rows, msg=msg)

    except:

        db.rollback()
        msg = "Value can not be NULL or Negative!"
        return render_template("result.html",msg=msg)


@app.route('/list', methods = ['GET','PUT'])
def list():


        db = lit.connect("Crud.db")
        db.row_factory = lit.Row
        cur = db.cursor()
        cur.execute("Select * from emp1")
        msg = "Success - 201"
        rows = cur.fetchall()
        return render_template("list.html", rows=rows,msg=msg)

@app.route('/list2', methods = ['GET','PUT'])
def list2():


        db = lit.connect("Crud.db")
        db.row_factory = lit.Row
        cur = db.cursor()
        cur.execute("Select * from logs")
        msg = "Success - 201"
        rows = cur.fetchall()
        return render_template("list2"
                               ".html", rows=rows,msg=msg)

@app.route('/updatentry')
def updentry():
    return render_template("update.html")

@app.route('/update',methods= ['GET','PUT','POST'])
def update():
    if request.method == 'POST':
        try:
            id = request.form['id']
            nm = request.form['nm']
            ema = request.form['ema']
            ph = request.form['ph']

            with lit.connect("Crud.db") as con:
                cur = con.cursor()
                msg = "Record updated successfully-200"
                cur.execute("Update emp1 set Name = ?,email = ?,Phone =? where ID = ?",(nm,ema,ph,id))
                con.commit()


        except:
            con.rollback()
            if id == "":
                msg = 'Value can not be NULL or negative!'
            else:
                msg = "Record Does Not Exist!"

        finally:
            return render_template("result.html", msg=msg)

@app.route('/deleteentry')
def delentry():
    return render_template("delete.html")

@app.route('/delete', methods=['GET','POST','DELETE'])
def delete():
    if request.method == 'POST':
        try:
            id = request.form['id']
            with lit.connect("Crud.db") as con:
                cur = con.cursor()
                msg = "Record deleted successfully-200"
                cur.execute("Delete from emp1 where ID = ?",id)
                con.commit()

        except:
            con.rollback()
            if id == "":
                msg = 'Value can not be NULL or negative!'
            else:
                msg = "Record Does Not Exist!"

        finally:
            return render_template("result.html", msg = msg)
            con.close()


if __name__ == "__main__":
    app.run(debug=True)