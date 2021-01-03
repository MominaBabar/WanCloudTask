from flask import Blueprint, render_template, abort,jsonify
api3 = Blueprint('novelconvid', __name__)
import requests
from database import db
from dateutil.parser import parse
import json
from models import API3
from flask_restful import Api, Resource, url_for

api = Api(api3)

class Fetch_Data(Resource):
    def get(self):
        db.create_all()
        r = requests.get("https://corona.lmao.ninja/v2/continents?yesterday=true&sort=").json()
        data = r
        print(len(data), " entries. ")
        row = {}
        for i in data:
            countries = ",".join(i["countries"])
            row = API3(i["updated"], i["cases"], i["todayCases"], i["deaths"], i["todayDeaths"], i["recovered"], i["todayRecovered"],
        i["active"], i["critical"], i["casesPerOneMillion"], i["deathsPerOneMillion"], i["tests"], i["testsPerOneMillion"], i["population"],
        i["continent"], i["activePerOneMillion"], i["recoveredPerOneMillion"], i["criticalPerOneMillion"],countries)
            print(row)
            db.session.add(row)
            db.session.commit()

        return 'Data Stored of  API: https://corona.lmao.ninja/v2/continents?yesterday=true&sort='

class Display_Data(Resource):
    def get(self):
        data = API3.query.all()
        ret = []
        for i in data:
            i = i.as_dict()
            ret.append(i)
        return jsonify(ret)


api.add_resource(Fetch_Data, '/')
api.add_resource(Display_Data, '/list')
