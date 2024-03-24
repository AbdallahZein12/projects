from flask import Flask, render_template, request, session, redirect, url_for #Needed to render different HTML code 
from flask_socketio import  join_room, leave_room, send, SocketIO 
import random #to generate random room codes
from string import ascii_uppercase #all the available characters to choose from when I generate a code for a room
import os 

app = Flask(__name__) #initialized flask application
app.config["SECRET_KEY"] = os.getenv("FLASK_CHAT_WEBSITE") #configs for flask app
socketio = SocketIO(app) #socketio integration 

rooms = {
    
}

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        
        if code not in rooms:
            break
        
    return code
    

@app.route("/", methods=["POST", "GET"]) #route to home page with methods post and get to retieve what the home page returns or post data to that route 
def home(): #home page / where you go to connect to or create a new chat room
    session.clear()
    if request.method == "POST": #if it receives post data from home form
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False) #attempts to get input out of form dictionary
        create = request.form.get("create", False)
        
        if not name:
            return render_template("home.html", error="Please enter a name!", code=code, name=name)
        
        if join != False and not code:
            return render_template("home.html", error="Please enter a room code!", code=code, name=name)
        
        room = code 
        if create != False:
            room = generate_unique_code(4) #generates unique code for room
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("home.html", error="Room does not exist!", code=code, name=name)
        
        session["room"] = room #storing data in a sesion - semipermanent user info - expires at some point and yet secure way to store user data
        session["name"] = name 
        return redirect(url_for("room"))

    return render_template("home.html")

@app.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms: #to ensure user has to complete registration on home page before entering a room
        return redirect(url_for("home"))
    
    return render_template("room.html", code=room, messages = rooms[room]["messages"])

@socketio.on("message") #handles server listening and communication to different rooms for messages
def message(data):
    room = session.get("room")
    if room not in rooms:
        return
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")
    

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name: #ensures user has valid room and valid name 
        return
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room) #joins socket room 
    send({"name": name, "message": "has entered the room"}, to=room) #default message for joining
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")
    
@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)
    
    if room in rooms:
        rooms[room]["members"] -= 1 #decreases members everytime a member leaves
        if rooms[room]["members"] <= 0: #removes room if no members are in session
            del rooms[room]
    
    send({"name": name, "message": "has left the room"}, to=room) #default message for leaving
    print(f"{name} has left the room {room}")
            
            

if __name__ == "__main__":
    socketio.run(app, debug=True) #enabling debug so any change to the web server that does not break any of the code will automatically refresh

