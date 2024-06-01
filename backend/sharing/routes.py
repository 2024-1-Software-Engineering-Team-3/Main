from flask import request, jsonify
from models import db, Sharing, User
from .__init__ import sharing_bp


@sharing_bp.route('/home', methods=['POST'])
def get_sharing():
    data = request.get_json()
    username = data.get('Username')

    if not username:
        return jsonify({'Response': '유저이름이 필요합니다.'}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'Response': "해당 유저가 존재하지 않습니다."}), 404

    sharing_entries = Sharing.query.all()
    result = {
        'Response': 'Success',
        "Sharing": [{
            "id": entry.id,
            'title': entry.title,
            'description': entry.description,
            'userid': entry.user_id,
            'username': entry.user.username,
            'date_created': entry.date_created.isoformat(),
            'recommend': entry.recommend,
            'downloadcount': entry.downloadcount,
            'point': entry.point,
            'fileurl': entry.fileurl
        } for entry in sharing_entries]
    }
    return jsonify(result), 200


@sharing_bp.route('/upload', methods=['POST'])
def create_sharing():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    user_id = data.get('user_id')
    point = data.get('point', 0)
    fileurl = data.get('fileurl')

    if not title or not description or not user_id:
        return jsonify({'Response': '제목과 설명, 아이디가 필요합니다.'}), 400

    user = db.session.get(User, user_id)
    if not user:
        return jsonify({'Response': '해당 유저를 찾을 수 없습니다.'}), 404

    new_entry = Sharing(
        title=title,
        description=description,
        user_id=user_id,
        point=point,
        fileurl=fileurl
    )
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'Response': 'Success', 'id': new_entry.id, 'message': 'Content shared successfully'}), 201
