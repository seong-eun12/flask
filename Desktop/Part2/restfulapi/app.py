from flask import Flask
from flask_restful import Api
from .resources import Item

app = Flask(__name__)

api = Api(app)

items = []  # 간단한 DB 역할

api.add_resource(Item, '/item/<string:name>')  # 경로 추가

if __name__ == '__main__':
    app.run(debug=1)