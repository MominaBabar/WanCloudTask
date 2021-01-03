from flask import Blueprint, render_template, abort,jsonify
api4 = Blueprint('cumulative', __name__)
import requests
from database import db
from dateutil.parser import parse
import json
from models import API1,API2,API3
from flask_restful import Resource, Api
from flask_restful import Api, Resource, url_for

api = Api(api4)

class Display_Data(Resource):
    def get(self):
        all_data = []
        data = API1.query.all()
        ret = []
        for i in data:
            i = i.as_dict()
            ret.append(i)
        all_data.append({"api_link": "https://thevirustracker.com/timeline/map-data.json", "data": ret})
        data = API2.query.all()
        ret = []
        for i in data:
            i = i.as_dict()
            ret.append(i)
        all_data.append({"api_link": "https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search", "data": ret})
        data = API3.query.all()
        ret = []
        for i in data:
            i = i.as_dict()
            ret.append(i)
        all_data.append({"api_link": "https://corona.lmao.ninja/v2/continents?yesterday=true&sort=", "data": ret})
    
        return jsonify(all_data)

api.add_resource(Display_Data, '/')
