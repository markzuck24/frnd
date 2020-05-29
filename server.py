#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import requests
import json
import sys
import os
import time
from flask import Flask, request, render_template,jsonify
from bot import toolBot

parser = argparse.ArgumentParser()
grid = None
parser.add_argument(
    "--host", default="localhost", help="The host of the server(eg. 0.0.0.0)")
parser.add_argument(
    "--port", default=9010, help="The port of the server(eg. 8500)", type=int)
parser.add_argument(
    "--debug",
    default=True,
    help="Enable debug for flask or not(eg. False)",
    type=bool)

args = parser.parse_args(sys.argv[1:])
application = Flask(__name__)

@application.route("/", methods=["GET"])
def index():
    return render_template('game.html')


@application.route("/play", methods=["POST"])
def play():
    data = request.form['data']
    toolBot(data)
    # toolBot(data)
    return jsonify("")




@application.route("/disp", methods=["POST"])
def disp():
    f=open("output.txt","r")
    data = f.read()
    os.remove("output.txt")
    inputFile = "input.txt"
    hypo = "h.txt"

    os.system("perl blu1.pl %s < %s" % (inputFile,hypo))
    time.sleep(1)
    return jsonify(data)

@application.route("/blu1", methods=["POST"])
def blu1():
    f=open("bleu1.txt","r")
    data = f.read()
    os.remove("bleu1.txt")
    return jsonify(data)

@application.route("/blu2", methods=["POST"])
def blu2():
    f=open("bleu.txt","r")
    data = f.read()
    os.remove("bleu.txt")
    return jsonify(data)

def main():
    port = int(os.environ.get('PORT', args.port))
    application.run(host=args.host, port=port, debug=args.debug,  threaded=True)
	
if __name__ == "__main__":
	main()
