from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from tama import Tamagochi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tamagotchi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PetModel(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    hunger = db.Column(db.Integer)
    happiness = db.Column(db.Integer)
    alive = db.Column(db.Integer)

with app.app_context() :
    db.create_all()

def loadpet() :
    savedata = PetModel.query.first()
    if savedata :
        pet = Tamagochi(savedata.name)
        pet.age = savedata.age
        pet.hunger = savedata.hunger
        pet.happiness = savedata.happiness
        pet.alive = savedata.alive
        return pet
    else :
        return Tamagochi("asdasdasd")

def savepet(pet) :
    savedata = PetModel.query.first()
    if savedata :
        savedata.age = pet.age
        savedata.hunger = pet.hunger
        savedata.happiness = pet.happiness
        savedata.alive = pet.alive
    else :
        savedata = PetModel(name=pet.name, age=pet.age, hunger=pet.hunger, happiness=pet.happiness, alive=pet.alive)
        db.session.add(savedata)
    db.session.commit()

with app.app_context():
    pet = loadpet()

@app.route('/')
def index() :
    return render_template('index.html', pet=pet, message="")

@app.route('/feed', methods=['POST'])
def feed() :
    message = pet.feed()
    message2 = pet.timepassed()
    savepet(pet)
    if message == message2 :
        message2 = ""
    return render_template('index.html', pet=pet, message=message, message2= message2)

@app.route('/play', methods=['POST'])
def play() :
    message = pet.play()
    message2 = pet.timepassed()
    savepet(pet)
    if message == message2 :
        message2 = ""
    return render_template('index.html', pet=pet, message=message, message2= message2)

@app.route('/wait', methods=['POST'])
def wait() :
    message = pet.timepassed()
    savepet(pet)
    return render_template('index.html', pet=pet, message=message)

@app.route('/revive', methods=['POST'])
def restart() :
    if pet.alive == 0 :
        pet.age = 1
        pet.hunger = 100
        pet.happiness = 100
        pet.alive = 1
        savepet(pet)
        message = f"{pet.name} was revived!"
        return render_template('index.html', pet=pet, message=message)
    else :
        message = f"{pet.name} is not dead."
        return render_template('index.html', pet=pet, message=message)

if __name__ == '__main__' :
    app.run()