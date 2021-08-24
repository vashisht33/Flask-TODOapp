import sqlite3 as lit
import datetime
def main():
    try:
            db=lit.connect("Crud.db")
            cur = db.cursor()
            tablequery=("Create table logs(ID INT,created_on text,updated_on text)")
            #cur.execute(tablequery)

            cur.execute("create trigger creation AFTER INSERT ON emp1 "
                        "begin" 
                        "insert into logs (ID,created_on,updated_on) values(new.ID,datetime('now'))"                      
                        "end")
            cur.execute('Select * from logs')
            #cur.execute("update emp1")
            print("table created successfully")
            return 'main'

    except:
            print("Error")