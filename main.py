#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import redirect
from flask import abort
import logging
from logging.handlers import RotatingFileHandler

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins = [40, 38, 37, 36, 35, 33, 32, 31, 29, 22, 18, 16, 15, 13, 12, 11]

GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)

def switch(pin):
    GPIO.output(pins[pin], GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(pins[pin], GPIO.HIGH)

app = Flask(__name__, static_url_path='')
tlist = [["1_1.png", "1_2.png", "0", "1"],
         ["2_1.png", "2_2.png", "3", "2"],
         ["3_1.png", "3_2.png", "5", "4"],
         ["4_1.png", "4_2.png", "7", "6"],
         ["5_1.png", "5_2.png", "9", "8"],
         ["6_1.png", "6_2.png", "10", "11"],
         ["7_2.png", "7_1.png", "13", "12"]]

@app.route('/')
def index():
    return render_template('index.html', turnout_list=tlist)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/turnout/<path:path>/')
def turnout_call(path):
    switch(int(path))
    return redirect("/", code=302)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
