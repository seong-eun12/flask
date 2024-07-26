from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Board 

board_blp = Blueprint('Boards','boards',description='Operations on boards', url_prefix='/board')

#API 리스트

@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
    

        return jsonify([{"id":board.id,'title': board.title,'content': board.content,'user_id': board.user_id,'author_name': board.author.name,'author_email': board.author.email }for board in boards])
    
    def post(self):
        data = request.json
        new_board = Board(title=data['title'], content=data['content'],user_id=data['user_id'])
        print(new_board)

        db.session.add(new_board)
        db.session.commit()

        return jsonify({'msg':'success create board'}), 201
    
#/board
#전체 게시글 불러오기(GET)
#게시글 작성(Post)

@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)
        return jsonify({"title": board.title, "content": board.content, "author": board.author.name})

    def put(self, board_id):
        board = Board.query.get_or_404(board_id)
        data = request.json
        board.title = data['title']
        board.content = data['content']
        db.session.commit()
        return jsonify({"message": "Board updated"})

    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({"message": "Board deleted"})