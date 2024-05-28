from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from models import db, User
from .__init__ import auth_bp


@auth_bp.route('/signup', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not email or not password:
        return jsonify({'Response': '아이디 또는 이메일, 패스워드가 필요합니다.'}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'Response': '사용자 이름 또는 이메일이 존재합니다.'}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'Response': '회원가입이 성공적으로 완료되었습니다.'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        access_token = create_access_token(
            identity={'username': user.username, 'email': user.email})
        return jsonify(user_info={'email': email, 'username': user.username}, access_token=access_token), 200

    return jsonify({'Response': '잘못된 이메일 또는 패스워드 입니다.'}), 401


@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"Response": "보호받는 route입니다."}), 200
