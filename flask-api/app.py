from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html', test="TEST"),200,headers)

class Latest(Resource):
    def get(self):
        try:
            scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
            client = gspread.authorize(creds)
            sheet = client.open("Solar Panel Data").sheet1
            return sheet.row_values(5)
        except:
            return None

api.add_resource(Home, '/')
api.add_resource(Latest, '/api/latest-value')

if __name__ == '__main__':
    app.run()