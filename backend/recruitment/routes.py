from flask import request, jsonify
from models import db, RecruitingData, RecruitmentMember
from .__init__ import recruit_bp


@recruit_bp.route('/home', methods=['GET'])
def load_recruiting_data():

    recruting_data = RecruitingData.query.all()
    result = []

    for item in recruting_data:
        result.append({
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "membercount": item.membercount,
            "duration": item.duration,
            "place": item.place,
            "type": item.type
        })

    return jsonify({'Response': "Success", "RecruitingData": result}), 200


@recruit_bp.route('/upload', methods=['POST'])
def create_recruiting_data():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    membercount = data.get('membercount')
    duration = data.get('duration')
    place = data.get('place')
    r_type = data.get('type')

    if not title or not description or not membercount or not duration or not r_type:
        return jsonify({'Response': "제목, 설명, 멤버 수, 기간 그리고 타입이 필요합니다"}), 400

    new_recruiting_data = RecruitingData(
        title=title,
        description=description,
        membercount=membercount,
        duration=duration,
        place=place,
        type=r_type
    )

    db.session.add(new_recruiting_data)
    db.session.commit()

    return jsonify({'Response': 'Recruting data가 성공적으로 생성되었습니다.', "id": new_recruiting_data.id}), 201


@recruit_bp.route('/join', methods=["POST"])
def join_recruitment():
    data = request.get_json()
    user_id = data.get('user_id')
    recruitment_id = data.get('recruitment_id')

    if not user_id or not recruitment_id:
        return jsonify({"Response": "유저 아이디와 리크루먼트 아이디가 필요합니다."}), 400

    recruitment = db.session.get(RecruitingData,recruitment_id)
    if not recruitment:
        return jsonify({"Response": "존재하지 않는 리크루먼트 아이디입니다."}), 404

    new_member = RecruitmentMember(
        user_id=user_id, recruitment_id=recruitment_id)
    db.session.add(new_member)
    db.session.commit()

    return jsonify({"Response": "성공적으로 리크루먼트에 가입했습니다."}), 201
