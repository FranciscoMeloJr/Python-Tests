#!flask/bin/python
from flask import Flask, jsonify, request, abort
import requests

app = Flask(__name__)

@app.route('/count', methods=['GET'])
def get_count():
    base_uri = 'https://www.googleapis.com/fusiontables/v2/query?sql='
    api_key = '&key=AIzaSyDMULA71K9KaGN9wPZF6_3Hnm4qOcKoiN0'
    query_str = 'SELECT * FROM 1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ'
    query_string = request.query_string

    fields_in_case_of_failure = []

    if '&' not in query_string:
        requestKey = [query_string.split('=')[0]]
        requestValue = [query_string.split('=')[1]]
        query_str += ' WHERE ' + str(requestKey[0]) + ' MATCHES \'' + str(requestValue[0] + '\'')

        fields_in_case_of_failure.append(requestKey)
    else:
        request_data = { each.split('=')[0]:each.split('=')[1] for each in query_string.split('&')}
        print(request_data)
        for i, (requestKey, requestValue) in enumerate(request_data.items()):
            fields_in_case_of_failure.append(requestKey)
            print(i)
            if (i == 0):
                query_str += ' WHERE ' + requestKey + ' CONTAINS IGNORING CASE \'' + requestValue + "\'"
            else:
                if requestValue.isdigit():
                    query_str += ' AND ' + requestKey + ' = ' + requestValue
                else:
                    query_str += ' AND ' + requestKey + ' CONTAINS IGNORING CASE \'' + requestValue + "\'"


    print("----------------------------------------------------")
    print(fields_in_case_of_failure)

    try:
        jsonResponse = requests.get(base_uri + query_str + api_key, headers={'Content-Type':'application/json'})
        rowsLenght = len(jsonResponse.json()['rows'])
    except:
        return bad_request_unknown_fields(fields_in_case_of_failure)
    if rowsLenght > 0:
        return jsonify({'count': rowsLenght})
    return abort(400)

def bad_request_unknown_fields(fields):
    print(fields)
    fields.sort()
    response = jsonify({'unknown fields': fields})
    response.status_code = 400
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
