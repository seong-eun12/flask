from flask import Flask, jsonify, request

app = Flask(__name__)

# GET
# 전체 게시글 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result': 'success', 'data': {"feed1": "data1", "feed2": "data2"}}
    return jsonify(data)

# 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result': 'success', 'data': {"feed_id": feed_id, "content": "data"}}
    return jsonify(data)

# POST
# 게시글 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form.get('name')
    age = request.form.get('age')

    print(name, age)
    return jsonify({'result': 'success'})

datas = [{"items": [{"name": "item1", "price": 10}]}]

# POST: 데이터 가져오는 API
@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return jsonify({'datas': datas})

# POST: 데이터 생성하는 API
@app.route('/api/v1/datas', methods=['POST'])
def create_data():
    request_data = request.get_json()

    new_data = {"items": request_data.get("items", [])}
    datas.append(new_data)

    return jsonify(new_data), 201

if __name__ == "__main__":
    app.run(debug=1)