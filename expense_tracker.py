import sqlite3
db=sqlite3.connect("expenses.db")
db.execute("""CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY,category TEXT,amount REAL,description TEXT,date TEXT DEFAULT CURRENT_DATE)""")
db.commit()

while True:
    print("\n1 Add 2 List 3 Total 4 Category totals 5 Exit")
    c=input("> ")
    if c=="1":
        db.execute("INSERT INTO expenses(category,amount,description) VALUES(?,?,?)",
                   (input("Category: "),float(input("Amount: ")),input("Description: "))); db.commit()
    elif c=="2":
        for x in db.execute("SELECT * FROM expenses"): print(x)
    elif c=="3":
        print("Total:",db.execute("SELECT COALESCE(SUM(amount),0) FROM expenses").fetchone()[0])
    elif c=="4":
        for x in db.execute("SELECT category,SUM(amount) FROM expenses GROUP BY category"): print(x)
    elif c=="5": break
