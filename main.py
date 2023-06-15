import asyncio
import tornado
import sqlite3

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("test.html", title="My title", items=items)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def database():
    con = sqlite3.connect("thingsdone.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE test(x, y, z)")
    res = cur.execute("SELECT name FROM ")
    res.fetchone
async def main():
    
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())