from flask import request, jsonify
from models import db, QAEntry, User, Answer
from .__init__ import qa_bp


@qa_bp.route('/home', methods=['GET'])
def get_qa_entries():
    entries = QAEntry.query.all()
    result = []
    for entry in entries:
        result.append({
            'id': entry.id,
            'title': entry.title,
            'content': entry.content,
            'date_created': entry.date_created.isoformat(),
            'userid': entry.user_id,
            'username': entry.user.username,
            'point': entry.point,
            'answered': entry.answered,
            'fileurl': entry.fileurl
        }
        )
    return jsonify({"Response": "Success", "Questions": result}), 200


@qa_bp.route('/upload', methods=["POST"])
def create_qa_entry():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = data.get('user_id')
    point = data.get('point', 0)
    fileurl = data.get('fileurl')

    if not title or not content or not user_id:
        return jsonify({'Response': "제목, 내용, 유저 아이디가 필요합니다."}), 400

    user = db.session.get(User, user_id)
    if not user:
        return jsonify({'Response': 'User not found'}), 404

    new_entry = QAEntry(title=title, content=content,
                        user_id=user_id, point=point, fileurl=fileurl)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'Response': 'QA entry가 성공적으로 생성되었습니다.', 'id': new_entry.id}), 201


@qa_bp.route('/answer', methods=['POST'])
def post_answer():
    data = request.get_json()
    description = data.get('description')
    user_id = data.get('user_id')
    question_id = data.get('question_id')

    if not description or not user_id or not question_id:
        return jsonify({'Response': '내용, 유저 아이디 또는 질문 아이디가 필요합니다.'}), 400

    user = db.session.get(User, user_id)
    if not user:
        return jsonify({'Response': 'User not found'}), 404

    question = db.session.get(QAEntry, question_id)
    if not question:
        return jsonify({'Response': 'Question not found'}), 404

    new_answer = Answer(description=description,
                        user_id=user_id, question_id=question_id)
    db.session.add(new_answer)
    db.session.commit()

    return jsonify({'Response': 'Success', 'id': new_answer.id}), 201
