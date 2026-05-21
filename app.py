from flask import Flask, render_template
from tama import Tamagochi

app = Flask(__name__)
pet = Tamagochi("dfsdfeasf")

@app.route('/')
def index() :
    return render_template('index.html', pet=pet)

@app.route('/feed', methods=['POST'])
def feed() :
    pet.feed()
    pet.timepassed()
    return render_template('index.html', pet=pet)

@app.route('/play', methods=['POST'])
def play() :
    pet.play()
    pet.timepassed()
    return render_template('index.html', pet=pet)

@app.route('/wait', methods=['POST'])
def wait() :
    pet.timepassed()
    return render_template('index.html', pet=pet)

if __name__ == '__main__' :
    app.run()