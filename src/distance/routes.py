from flask import Flask, Blueprint, request, redirect, jsonify
from src.distance.base import processing
import os 

distance = Blueprint('distance', __name__)

@distance.route('/distance/estimate', methods=['GET', 'POST'])
def estimate_distance():
    # if request.method == 'POST':
    tmp = "Done!"
    os.system('python3 src/distance/base.py')
    
    return jsonify(tmp=tmp)