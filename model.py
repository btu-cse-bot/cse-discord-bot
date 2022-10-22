import sqlite3 
import sys
sys.path.insert(0,".")
class Models:
    def __init__(self):
        self.db = sqlite3.connect('db.sqlite3')
        self.cursor = self.db.cursor()
        
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS main(
                user_id TEXT NOT NULL PRIMARY KEY,
                signDate DATETIME DEFAULT CURRENT_TIMESTAMP,
                takeDate DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS exp(
            user_id INTEGER PRIMARY KEY,
            exp INTEGER DEFAULT 0,
            leetcode_exp INTEGER DEFAULT 0,
            level INTEGER DEFAULT 0,
            amount INTEGER DEFAULT 0
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks(
            task_id INTEGER PRIMARY KEY NOT NULL,
            task_encrpted TEXT NOT NULL,
            completed_user_id INTEGER DEFAULT O,
            task TEXT,
            zorluk INTEGER DEFAULT 0
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS urls(
            user_id INTEGER PRIMARY KEY,
            leetcode TEXT DEFAULT NULL,
            github TEXT DEFAULT NULL
            )
        ''')
        print("Tables created")
    def add_user(self,user_id):
        self.cursor.execute('''
            INSERT INTO main(user_id) VALUES(?)''',(user_id,))
        self.db.commit()

    def add_exp(self,user_id):
        EXP,LEVEL,AMOUNT =100,0,100
        self.cursor.execute('''
            INSERT INTO exp(user_id,exp,level,amount) VALUES(?,?,?,?)''',(user_id,EXP,LEVEL,AMOUNT))
        self.db.commit()

    def add_task(self,task_id,task_encrpted,task,zorluk):
        self.cursor.execute('''
            INSERT INTO tasks(task_id,task_encrpted,task,zorluk) VALUES(?,?,?,?)''',(task_id,task_encrpted,task,zorluk))
        self.db.commit()

    def add_url(self,user_id):
        self.cursor.execute('''
            INSERT INTO urls(user_id) VALUES(?)''',(user_id,))
        self.db.commit()

    def get_user(self,user_id):
        self.cursor.execute('''
            SELECT * FROM main WHERE user_id=?''',(user_id,))
        return self.cursor.fetchone()


    def get_user_info(self,user_id):
        self.cursor.execute('''
            SELECT * FROM exp WHERE user_id=?''',(user_id,))
        return self.cursor.fetchone()
    def get_exp(self,user_id):
        self.cursor.execute('''
            SELECT * FROM exp WHERE user_id=?''',(user_id,))
        return self.cursor.fetchone()