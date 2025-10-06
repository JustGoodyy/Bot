from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def keep_alive():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)










#from flask import Flask, jsonify
#from threading import Thread

#app = Flask('')
#@app.route('/')
#def home():
    #return "Discord Bot is running"

#def run():
    #app.run(host="0.0.0.0", port=8080)

#def keep_alive():
    #t = Thread(target=run)
    #t.start()