from flask import request, jsonify, make_response
from .views import bp_1
from ..models.models import Parties

parties_list = []


@bp_1.route('/parties', methods=['POST'])
def create_party():
    '''Create a party'''
    try:
        data = request.get_json()
        id = len(parties_list) + 1
        name = data['name']
        hq_address = data['hq_address']
        logo_url = data['logo_url']
        chairperson = data['chairperson']     
    except:
        return jsonify({
                "status": 400,
                "error": "invalid request"
        })
    

    #Create instance of Parties and pass in data
    new_party = Parties(id, name, hq_address, logo_url, chairperson)
    parties_list.append(new_party)
    
    #Loop through the parties list to return the recently added item
    for party in range(len(parties_list)):
        if (parties_list[party]['id']) == int(id):
            return make_response(jsonify({
            "status": 201,
            "data": [{ "id": parties_list[party]['id'],
                 "name": parties_list[party]['name'],
                  "chairperson": parties_list[party]['chairperson']
                 }]
    }))

