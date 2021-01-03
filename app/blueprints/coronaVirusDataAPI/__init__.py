from flask import Blueprint, render_template, abort,jsonify
api1 = Blueprint('coronavirusdataapi', __name__)
import requests
from database import db
import json
from models import API1
from flask_restful import Api, Resource, url_for

api = Api(api1)

class Fetch_Data(Resource):
    def get(self):
        db.create_all()
        r = requests.get("https://thevirustracker.com/timeline/map-data.json").json()
        data = r['data']
        print(len(data), " entries. ")
        row = {}
        for i in data:
            date = parse( i["date"]).strftime("%Y-%m-%d")
            cases = int(i["cases"]) if i["cases"] != '' else 0
            death = int(i["deaths"]) if i["deaths"] != '' else 0
            recovered = int(i["recovered"]) if i["recovered"] != '' else 0
            row = API1(i["countrycode"], date, cases, death, recovered)
            print(row)
            db.session.add(row)
            db.session.commit()

        return 'Data Stored from API https://thevirustracker.com/timeline/map-data.json'

class Display_Data(Resource):
    def get(self):
        data = API1.query.all()
        ret = []
        for i in data:
            i = i.as_dict()
            ret.append(i)
        return jsonify(ret)


api.add_resource(Fetch_Data, '/')
api.add_resource(Display_Data, '/list')
