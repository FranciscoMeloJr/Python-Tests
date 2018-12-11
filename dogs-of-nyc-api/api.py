#!flask/bin/python
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/count', methods=['GET'])
def get_count():
    base_uri = 'https://www.googleapis.com/fusiontables/v2/query?sql='
    api_key = '&key=AIzaSyDMULA71K9KaGN9wPZF6_3Hnm4qOcKoiN0'
    query_str = 'SELECT * FROM 1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ'
    query_string = request.query_string

    if '&' not in query_string:
        requestKey = [query_string.split('=')[0]]
        requestValue = [query_string.split('=')[1]]
        query_str += ' WHERE ' + str(requestKey[0]) + ' CONTAINS IGNORING CASE \'' + str(requestValue[0] + '\'')
    else:
        request_data = { each.split('=')[0]:each.split('=')[1] for each in query_string.split('&')}
        print(request_data)
        for i, (requestKey, requestValue) in enumerate(request_data.items()):
            print(i)
            if (i == 0):
                query_str += ' WHERE ' + requestKey + ' CONTAINS IGNORING CASE \'' + requestValue + "\'"
            else:
                if requestValue.isdigit():
                    query_str += ' AND ' + requestKey + ' CONTAINS IGNORING CASE ' + requestValue
                else:
                    query_str += ' AND ' + requestKey + ' CONTAINS IGNORING CASE \'' + requestValue + "\'"
    return query_str


    # for each in request.query_string.split('&'):
    #      temp.append(each.split('=')[1])
    # return temp
    # return request.query_string

    # self.request.GET.get('variable_name')

    # resp = requests.get('https://fusiontables.google.com/data?docid=1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ#rows:id=1', headers={'Content-Type':'application/json'})

    # url = 'https://www.googleapis.com/fusiontables/v2/query?sql=SELECT%20*%20FROM%201pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ%20LIMIT%202&key=AIzaSyDMULA71K9KaGN9wPZF6_3Hnm4qOcKoiN0'
    # headers = {"Accept": "application/json"}
    # response = requests.get(url)

    jsonResponse = requests.get(base_uri + "SELECT * FROM 1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ" + api_key, headers={'Content-Type':'application/json'})
    # if (rowsLenght == 2) {
    #     return abort(400)
    # }

    try:
        rowsLenght = len(jsonResponse.json()['rows'])
        if rowsLenght < 1:
            return jsonify({'count': rowsLenght})
    except:
        return abort(400)

    # len(count['rows'])

if __name__ == '__main__':
    app.run(debug=True)
