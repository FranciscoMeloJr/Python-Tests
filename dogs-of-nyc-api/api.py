#!flask/bin/python
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/count', methods=['GET'])
def get_count():
    """
    Return the count result from a query.
    :return: The count result.
    """
    base_uri = 'https://www.googleapis.com/fusiontables/v2/query?sql='
    api_key = '&key=AIzaSyDMULA71K9KaGN9wPZF6_3Hnm4qOcKoiN0'
    query_str = 'SELECT * FROM 1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ'
    query_string = request.query_string

    if '&' not in query_string:
        request_key = [query_string.split('=')[0]]
        request_value = [query_string.split('=')[1]]
        query_str += ' WHERE ' + str(request_key[0]) + ' CONTAINS IGNORING CASE \'' + str(request_value[0] + '\'')
    else:
        query_str = create_query_dict(query_string)

    #Do the query
    json_response = requests.get(base_uri + "SELECT * FROM 1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ" + api_key, headers={'Content-Type':'application/json'})

    if rowsLenght > 0:
            return jsonify({'count': rowsLenght})
    return abort(400)


def create_query_dict(query_string):
    """
    Creates the string for dict.
    :return:  String query.
    """

    request_data ={each.split('=')[0]: each.split('=')[1] for each in query_string.split('&')}
    #iterating Over dict:
    for i, (requestKey, requestValue) in enumerate(request_data.items()):
        print(i)
        if i == 0:
            query_str += ' WHERE ' + requestKey + ' CONTAINS IGNORING CASE \'' + requestValue + "\'"
        else:
            if requestValue.isdigit():
                query_str += ' AND ' + requestKey + ' CONTAINS IGNORING CASE ' + requestValue
            else:
                query_str += ' AND ' + requestKey + ' CONTAINS IGNORING CASE \'' + requestValue + "\'"

    return query_str


if __name__ == '__main__':
    app.run(debug=True)
