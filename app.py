# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 23:22:34 2016

@author: Administrator
"""

from flask import Flask,request
from flask import jsonify
from recommendation.Engine import Engine
from recommendation.Utils import loadHeroDict
from recommendation.BaseModel import BaseModel

app = Flask(__name__)


@app.route('/api/v1.0/recommend',methods=["POST"])
def recommend():
    
    ownSide = request.json["ownSide"]
    print ownSide

    enemySide = request.json["enemySide"]
    topK = request.json["topK"]

    
    recommendInfo = engine.recommend(ownSide,enemySide,topK)
    print recommendInfo
    
    return jsonify(recommendInfo)

@app.route("/api/v1.0/predict",methods=["POST"])
def predict():  
    
    radiant = request.form["radiant"]
    dire = request.form["dire"]
        
if __name__ == '__main__':
    modelPath = "resource/model.pkl"    
    heroDict = loadHeroDict("resource/heroes.json")
    baseModel = BaseModel(modelPath,heroDict)
    engine = Engine(baseModel,heroDict,method="PureMC",epochs=100)
    app.run()