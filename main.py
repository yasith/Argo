from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
import json
import os.path

app = Flask(__name__)
api = Api(app)


civ_list = ['Greek', 'Egyptian', 'Norse', 'Atlantean']

json_data = open(os.path.dirname(__file__) + '/data/data.json').read()
data = json.loads(json_data)

#data = [{'civ': 'Greek', 'name': 'Dumbitis'}]

class CivList(Resource):
	def get(self):
		return civ_list

class UnitList(Resource):
	def get(self, civ_id):
		return [{'name': unit['Name']} for unit in data if unit['civ'] == civ_id]

class Unit(Resource):
	def get(self, civ_id, unit_id):
		unit = None
		for unit in data:
			if unit['Name'] == unit_id and unit['civ'] == civ_id:
				unit = unit
				break
		return unit
			

api.add_resource(CivList, '/api/v1/civs')
api.add_resource(UnitList, '/api/v1/civs/<string:civ_id>')
api.add_resource(Unit, '/api/v1/civs/<string:civ_id>/<string:unit_id>')

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
