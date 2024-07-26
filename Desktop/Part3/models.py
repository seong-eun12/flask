#Model -> Table 생성 
#게시글 - board
#유저 - user

from db import db

class User(db.Model) : #db.model 상속
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30), nullable =False)
    email = db.Column(db.String(100), unique = True, nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic') 
    #lazy='dynamic' 게시판 글들 중 특정 글 조회할 때 사용


class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    author = db.relationship('User',back_populates='boards')


