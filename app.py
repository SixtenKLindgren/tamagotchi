from flask import Flask, render_template
from tama import Tamagochi

app = Flask(__name__)
pet = Tamagochi("dfsdfeasf")

@app.route('/')
def index() :
    return render_template('index.html', pet=pet)

@app.route('/feed', methods=['POST'])
def feed() :
    message = pet.feed()
    message2 = pet.timepassed()
    if message == message2 :
        message2 = ""
    return render_template('index.html', pet=pet, message=message, message2= message2)

@app.route('/play', methods=['POST'])
def play() :
    message = pet.play()
    message2 = pet.timepassed()
    if message == message2 :
        message2 = ""
    return render_template('index.html', pet=pet, message=message, message2= message2)

@app.route('/wait', methods=['POST'])
def wait() :
    message = pet.timepassed()
    return render_template('index.html', pet=pet, message=message)

if __name__ == '__main__' :
    app.run()