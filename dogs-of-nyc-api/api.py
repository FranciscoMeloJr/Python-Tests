#!flask/bin/python
from flask import Flask, jsonify, request, abort
import requests

app = Flask(__name__)


@app.route('/count', methods=['GET'])
def get_count():
    """
    Get the count of a query.
    :return: Query value.
    """
    base_uri = 'https://www.googleapis.com/fusiontables/v2/query?sql='
    api_key = '&key=AIzaSyDMULA71K9KaGN9wPZF6_3Hnm4qOcKoiN0'
    query_str = 'SELECT * FROM 1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ'
    query_string = request.query_string

    fields_in_case_of_failure = []

    # Simple queries:
    if '&' not in query_string:
        request_key = [query_string.split('=')[0]]
        request_value = [query_string.split('=')[1]]
        query_str += ' WHERE ' + str(request_key[0]) + ' MATCHES \'' + str(request_value[0] + '\'')

        fields_in_case_of_failure.append(request_key)
    else:
        query_str = create_mult_query(query_str, query_string, fields_in_case_of_failure)

    try:
        # Content-Type value:
        json_response = requests.get(base_uri + query_str + api_key, headers={'Content-Type':'application/json'})
        rows_length = len(json_response.json()['rows'])
    # Using bare except:
    except:
        return bad_request_unknown_fields(fields_in_case_of_failure)
    if rows_length > 0:
        return jsonify({'count': rows_length})
    return abort(400)


def create_mult_query(query_str, orig_string, fields_in_case_of_failure):
    """
    Creates the string for dict.
    :param query_str Default value + result strings for query.
    :param orig_string Original queried values.
    :param fields_in_case_of_failure Accumulator of the results.
    :return:  String query.
    """
    # Dict Comprehension for combined queries
    request_data = {each.split('=')[0]: each.split('=')[1] for each in orig_string.split('&')}
    for i, (request_key, request_value) in enumerate(request_data.items()):
        # Appending values in case of fail:
        fields_in_case_of_failure.append(request_key)
        if i == 0:
            # Query done using CONTAINS IGNORING CASE
            query_str += ' WHERE ' + request_key + ' CONTAINS IGNORING CASE \'' + request_value + "\'"
        else:
            if request_value.isdigit():
                query_str += ' AND ' + request_key + ' = ' + request_value
            else:
                query_str += ' AND ' + request_key + ' CONTAINS IGNORING CASE \'' + request_value + "\'"

    return query_str


def bad_request_unknown_fields(fields):
    """
    Return answer for wrong field.
    :param fields: Keys to be displayed on the error message.
    :return: Bad request response.
    """
    fields.sort()
    response = jsonify({'unknown fields': fields})
    response.status_code = 400
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
