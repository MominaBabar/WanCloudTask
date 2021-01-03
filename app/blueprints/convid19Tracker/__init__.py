from flask import Blueprint, render_template, abort,jsonify
api2 = Blueprint('convid19tracker', __name__)
import requests
from database import db
from dateutil.parser import parse
import json
from models import API2
from flask_restful import Api, Resource, url_for

api = Api(api2)

class Fetch_Data(Resource):
    def get(self):
        db.create_all()
        r = requests.get("https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search").json()
        data = r['data']['rows']
        print(len(data), " entries. ")
        row = {}
        for i in data:
            row = API2(i["country"], i["country_abbreviation"], i["total_cases"], i["new_cases"], i["total_deaths"],
            i["new_deaths"], i["total_recovered"], i["active_cases"],
            i["serious_critical"], i["cases_per_mill_pop"], i["flag"])
            print(row)
            db.session.add(row)
            db.session.commit()

        return 'Data Stored from API: https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search'

class Display_Data(Resource):
    def get(self):
        data = API2.query.all()
        ret = []
        for i in data:
            i = i.as_dict()
            ret.append(i)
        return jsonify(ret)


api.add_resource(Fetch_Data, '/')
api.add_resource(Display_Data, '/list')
