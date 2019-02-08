from flask import request, jsonify, make_response
from .views import bp_1
from ..models.models import Offices

offices_list = []


@bp_1.route('/offices', methods=['POST'])
def create_office():
    '''Create a Political Office'''
    try:
        data = request.get_json()
        id = len(offices_list) + 1
        name = data['name']
        type = data['type']
             
    except:
        return jsonify({
                "status": 400,
                "error": "invalid request"
        })
    

    #Create instance of offices and pass in data
    new_office = Offices(id, name, type)
    offices_list.append(new_office)
    
    #Loop through the offices list to return the recently added item
    for office in range(len(offices_list)):
        if (offices_list[office]['id']) == int(id):
            return make_response(jsonify({
            "status": 201,
            "message": "Office Created Succesfully",
            "data": [{ "id": offices_list[office]['id'],
                 "name": offices_list[office]['name'],
                  "type": offices_list[office]['type']
                 }]
    }), 201)


@bp_1.route('/offices', methods=['GET'])
def get_office():
    if len(offices_list) > 0:
        return make_response(jsonify({
            "status": 200,
            "message": "Request was successful",
            "data": [office.__dict__ for office in offices_list]
        }), 200)

    return make_response(jsonify({
        "status": 404,
        "message": "No Offices Available"
    }), 404)


@bp_1.route('/offices/<int:id>', methods=['GET'])
def get_office_byid(id):
    for office in range(len(offices_list)):
        if (offices_list[office]["id"]) == int(id):
            return jsonify({
                "status": 200,
                "message": "Request was successful",
                "data": [{
                   "id": offices_list[office]["id"],
                   "name": offices_list[office]["name"],
                   "type": offices_list[office]["type"]
                }]
                    
            }), 200
    return jsonify({
        "status": 404,
        "message": "Resource could not be found",
    }), 404
