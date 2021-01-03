from database import db
from dateutil.parser import parse
import json


class API1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    countrycode = db.Column(db.String(4))
    date = db.Column(db.Date())
    cases = db.Column(db.Integer())
    deaths = db.Column(db.Integer())
    recovered = db.Column(db.Integer())

    def __init__(self, countrycode, date, cases, deaths, recovered):
        self.countrycode = countrycode
        self.date = date
        self.cases = cases
        self.deaths = deaths
        self.recovered = recovered
    
    def __repr__(self):
        return '<Country %r>' % self.countrycode
    
    def as_dict(self):
        dictionary = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return dictionary

    

class API2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(40))
    country_abbreviation  = db.Column(db.String(4))
    total_cases  = db.Column(db.String(256))
    new_cases  = db.Column(db.String(256))
    total_deaths  = db.Column(db.String(256))
    new_deaths  = db.Column(db.String(256))
    total_recovered  = db.Column(db.String(256))
    active_cases  = db.Column(db.String(256))
    serious_critical  = db.Column(db.String(256))
    cases_per_mill_pop  = db.Column(db.String(256))
    flag =  db.Column(db.String(256))

    def __init__(self, country,country_abbreviation,total_cases,new_cases,total_deaths,new_deaths,
    total_recovered,active_cases,serious_critical,cases_per_mill_pop,flag):
        self.country = country
        self.country_abbreviation  = country_abbreviation
        self.total_cases  = total_cases
        self.new_cases  = new_cases
        self.total_deaths  = total_deaths
        self.new_deaths  = new_deaths
        self.total_recovered  = total_recovered
        self.active_cases  = active_cases
        self.serious_critical  = serious_critical
        self.cases_per_mill_pop  = cases_per_mill_pop
        self.flag = flag
    
    def __repr__(self):
        return '<Country %r>' % self.country_abbreviation
    
    def as_dict(self):
        dictionary = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return dictionary

class API3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    updated = db.Column(db.String(256))
    cases = db.Column(db.String(256))
    todayCases = db.Column(db.String(256))
    deaths = db.Column(db.String(256))
    todayDeaths = db.Column(db.String(256))
    recovered = db.Column(db.String(256))
    todayRecovered = db.Column(db.String(256))
    active = db.Column(db.String(256))
    critical = db.Column(db.String(256))
    casesPerOneMillion = db.Column(db.String(256))
    deathsPerOneMillion = db.Column(db.String(256))
    tests = db.Column(db.String(256))
    testsPerOneMillion = db.Column(db.String(256))
    population = db.Column(db.String(256))
    continent = db.Column(db.String(40),unique=True)
    activePerOneMillion = db.Column(db.String(256))
    recoveredPerOneMillion = db.Column(db.String(256))
    criticalPerOneMillion = db.Column(db.String(256))
    countries = db.Column(db.Text(20000))

    def __init__(self, updated, cases, todayCases, deaths, todayDeaths, recovered, todayRecovered,
    active, critical, casesPerOneMillion, deathsPerOneMillion, tests, testsPerOneMillion, population,
    continent, activePerOneMillion, recoveredPerOneMillion, criticalPerOneMillion,countries):
        self.updated = updated
        self.cases = cases
        self.todayCases = todayCases
        self.deaths = deaths
        self.todayDeaths = todayDeaths
        self.recovered = recovered
        self.todayRecovered = todayRecovered
        self.active = active
        self.critical = critical
        self.casesPerOneMillion = casesPerOneMillion
        self.deathsPerOneMillion = deathsPerOneMillion
        self.tests = tests
        self.testsPerOneMillion = testsPerOneMillion
        self.population = population
        self.continent = continent
        self.activePerOneMillion = activePerOneMillion
        self.recoveredPerOneMillion = recoveredPerOneMillion
        self.criticalPerOneMillion = criticalPerOneMillion
        self.countries = countries
    
    def __repr__(self):
        return '<Continent %r>' % self.continent
    
    def as_dict(self):
        dictionary = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return dictionary