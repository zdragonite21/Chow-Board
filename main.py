import asyncio
import tornado
import sqlite3

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = get_tasks()
        self.render("test.html", title="My title", items=items)

con = sqlite3.connect("thingsdone.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS tasks
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                stars INTEGER,
                task TEXT,
                time INTEGER)''')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])
    
def add_task(name, stars, task, time):
    cur.execute("INSERT INTO tasks (name, stars, task, time) VALUES (?, ?, ?, ?)", (name, stars, task, time))
    con.commit()

def get_tasks(n):
    cur.execute("SELECT * FROM tasks ORDER BY id DESC LIMIT " + str(n))
    return cur.fetchall()

def clear_db():
    cur.execute("DELETE FROM tasks")
    cur.execute("DELETE FROM sqlite_sequence WHERE name='tasks'")
    con.commit()

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()
    

if __name__ == "__main__":
    add_task("Rowan", 5, "Abnormal Psychology", 10000)
    print(get_tasks(5))
    asyncio.run(main())
    con.close()