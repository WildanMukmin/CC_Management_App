import mysql.connector as con
from customtkinter import *

# Database management class
class Management_CC:
    def __init__(self):
        self.mydb = con.connect(
            host="localhost",
            user="root",
            passwd="",
            database="capcut"
        )
        self.myCursor = self.mydb.cursor()
        self.create_table()
    
    def create_table(self):
        try:
            self.myCursor.execute("""
                CREATE TABLE IF NOT EXISTS record (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nama VARCHAR(50),
                    link VARCHAR(100),
                    tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    status VARCHAR(11)
                )
            """)
            print("Table created successfully")
        except con.Error as err:
            print(f"Error: {err}")

    def add_record(self, nama, link, status):
        sql = "INSERT INTO record (nama, link, status) VALUES (%s, %s, %s)"
        val = (nama, link, status)
        try:
            self.myCursor.execute(sql, val)
            self.mydb.commit()
            print("Record added successfully")
        except con.Error as err:
            print(f"Error: {err}")
    
    def update_record(self, record_id, nama=None, link=None, tanggal=None, status=None):
        sql = "UPDATE record SET "
        val = []
        if nama:
            sql += "nama = %s, "
            val.append(nama)
        if link:
            sql += "link = %s, "
            val.append(link)
        if tanggal:
            sql += "tanggal = %s, "
            val.append(tanggal)
        if status:
            sql += "status = %s, "
            val.append(status)
        sql = sql.rstrip(', ')
        sql += " WHERE id = %s"
        val.append(record_id)
        try:
            self.myCursor.execute(sql, tuple(val))
            self.mydb.commit()
            print("Record updated successfully")
        except con.Error as err:
            print(f"Error: {err}")

    def delete_record(self, record_id):
        sql = "DELETE FROM record WHERE id = %s"
        val = (record_id,)
        try:
            self.myCursor.execute(sql, val)
            self.mydb.commit()
            print("Record deleted successfully")
        except con.Error as err:
            print(f"Error: {err}")
    
    def fetch_records(self):
        sql = "SELECT * FROM record"
        try:
            self.myCursor.execute(sql)
            result = self.myCursor.fetchall()
            return result
        except con.Error as err:
            print(f"Error: {err}")
            return []

# GUI class
class CapCutGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CapCut Management")
        self.root.geometry("1000x600")
        self.db_manager = Management_CC()
        
        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # <----------------- FRAME SIDE BAR ----------------->
        self.side_bar = CTkFrame(self.root, corner_radius=0, fg_color="red")
        self.side_bar.place(relwidth = 0.25, relheight = 1, relx = 0, rely = 0, anchor = NW)
        
        # <----------------- FRAME MAIN ----------------->
        self.side_bar = CTkFrame(self.root, corner_radius=0, fg_color="blue")
        self.side_bar.place(relwidth = 0.75, relheight = 1, relx = 0.25, rely = 0, anchor = NW)

        
        
        

root = CTk()
app = CapCutGUI(root)
root.mainloop()
