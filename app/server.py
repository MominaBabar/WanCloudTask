from database import db
from flask import Flask,Blueprint
from blueprints.coronaVirusDataAPI import api1
from blueprints.convid19Tracker import api2
from blueprints.novelConvidAPI import api3
from blueprints.cumulative_data import api4
from views import index
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api, Resource, url_for

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://momina:wantask2021@localhost/corona_stats"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)    
    with app.app_context():
        db.create_all()
    app.register_blueprint(api1,url_prefix='/coronavirusapi')
    app.register_blueprint(api2,url_prefix='/convid19tracker')
    app.register_blueprint(api3,url_prefix='/novelconvid')
    app.register_blueprint(api4,url_prefix='/cumulative')
    app.register_blueprint(index,url_prefix='/')
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    return manager
     
if __name__ == '__main__':
    app = create_app()
    app.run()
