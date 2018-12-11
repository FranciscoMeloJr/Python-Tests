#!flask/bin/python
from flask import Flask, jsonify, request, abort
import requests

app = Flask(__name__)


@app.route('/count', methods=['GET'])
def get_count():
    """
    Return the account.
    :return: The count result.
    """
    base_uri = 'https://www.googleapis.com/fusiontables/v2/query?sql='
    # API_KEY Acess:
    api_key = '&key=AIzaSyDMULA71K9KaGN9wPZF6_3Hnm4qOcKoiN0'
    query_str = 'SELECT * FROM 1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ'
    # String:
    query_string = request.query_string

    fields_in_case_of_failure = []

    if '&' not in query_string:
        request_key = [query_string.split('=')[0]]
        request_value = [query_string.split('=')[1]]
        query_str += ' WHERE ' + str(request_key[0]) + ' MATCHES \'' + str(request_value[0] + '\'')

        fields_in_case_of_failure.append(requestKey)
    else:
        query_str = create_query_dict(query_string)

    try:
        json_response = requests.get(base_uri + query_str + api_key, headers={'Content-Type':'application/json'})
        rows_length = len(json_response.json()['rows'])
    except:
        return bad_request_unknown_fields(fields_in_case_of_failure)
    if rowsLenght > 0:
        return jsonify({'count': rows_length})
    return abort(400)


def create_query_dict(query_string):
    """
    Creates the string for dict.
    :return:  String query.
    """

    request_data ={each.split('=')[0]: each.split('=')[1] for each in query_string.split('&')}
    # iterating Over dict:
    query_str = []
    for i, (requestKey, requestValue) in enumerate(request_data.items()):
        if i == 0:
            # Ignores case vs Match
            query_str += ' WHERE ' + requestKey + ' CONTAINS IGNORING CASE \'' + requestValue + "\'"
        else:
            if requestValue.isdigit():
                query_str += ' AND ' + requestKey + ' CONTAINS IGNORING CASE ' + requestValue
            else:
                query_str += ' AND ' + requestKey + ' CONTAINS IGNORING CASE \'' + requestValue + "\'"

    return query_str


def bad_request_unknown_fields(fields):
    """
    Returns unknown fields message request.
    :return:  Response.
    """
    # Alphabetic order:
    fields.sort()
    response = jsonify({'unknown fields': fields})
    response.status_code = 400
    return response


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
