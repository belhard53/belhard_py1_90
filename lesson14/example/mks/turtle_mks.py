import turtle as t
import requests, json, os

WORK_DIR = os.path.dirname(__file__)

def mks_move(x,y):
    global mks
    mks.penup()
    mks.goto(x, y)
    mks.showturtle()
    mks.pendown()

def mks_track():
    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url)
    if res.status_code==200:
        res_json = json.loads(res.text)
        y = float(res_json['iss_position']["latitude"])
        x = float(res_json['iss_position']["longitude"])
        print(x,y)
        mks_move(x, y)
    else:
        print("err mks url....")

    widget = t.getcanvas()
    widget.after(2000,mks_track)


screen = t.Screen()
mks = t.Turtle()
mks.hideturtle()
screen.setup(1600, 800)
screen.bgpic(os.path.join(WORK_DIR, "karta1.gif"))
screen.setworldcoordinates(-180, -90, 180, 90)
t.register_shape(os.path.join(WORK_DIR, 'mks3.gif'))
mks.shape(os.path.join(WORK_DIR, 'mks3.gif'))
mks.hideturtle()


mks_track()
t.mainloop()