from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class RecruitingData(db.Model):
    __tablename__ = 'recruiting_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    membercount = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.String, nullable=False)
    place = db.Column(db.String(255), nullable=True)
    type = db.Column(db.String(50), nullable=False)


class RecruitmentMember(db.Model):
    __tablename__ = "recruitment_member"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), nullable=False)
    recruitment_id = db.Column(db.Integer, db.ForeignKey(
        'recruiting_data.id'), nullable=False)
    recruitment = db.relationship(
        "RecruitingData", backref=db.backref('members', lazy=True))


class QAEntry(db.Model):
    __tablename__ = 'qa_entries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    point = db.Column(db.Integer, nullable=False, default=0)
    answered = db.Column(db.Boolean, nullable=False, default=False)
    fileurl = db.Column(db.String(255), nullable=True)

    user = db.relationship('User', backref=db.backref('qa_entries', lazy=True))


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'qa_entries.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('answers', lazy=True))
    question = db.relationship(
        'QAEntry', backref=db.backref('answers', lazy=True))


class Sharing(db.Model):
    __tablename__ = 'sharing'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    point = db.Column(db.Integer, nullable=False, default=0)
    fileurl = db.Column(db.String(255), nullable=True)
    recommend = db.Column(db.Integer, nullable=False, default=0)
    downloadcount = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship('User', backref=db.backref('sharing', lazy=True))
