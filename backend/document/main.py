# from flask import Flask, request, jsonify
# from flask_restful import Api, Resource

# from Document_Verify.Verify_main import API_Document_Verify

# app = Flask(__name__)
# api = Api(app)


# class DocumentCheck(Resource):
#     """
#     Document Verif API를 위한 main class
#     """
#     def post(self):

#         data = request.get_json()

#         if not data or 'Username' not in data or 'DocumentPath' not in data or 'Title' not in data or 'Description' not in data:
#             return {"Response": "잘못된 요청입니다."}, 500

#         username = data['Username']
#         document_path = data['DocumentPath']
#         document_description = data['Title'] + data['Description']

#         is_not_duplicated, is_well_cateogrized, message, category = API_Document_Verify(document_path,
#                                                                               document_description)

#         if is_not_duplicated and is_well_cateogrized:
#             """ ##TODO## Save In DB by username


#             """
#             return {"Response": "Success"}, 200
#         else:
#             if not is_not_duplicated:
#                 return {"Response": message}, 401
#             elif not is_well_cateogrized:
#                 return {"Response": message}, 402
#             else:
#                 return {"Response": "알 수 없는 오류가 발생했습니다."}, 500
# api.add_resource(DocumentCheck, '/Verify')


# if __name__ == "__main__":
#     app.run(debug=True)
