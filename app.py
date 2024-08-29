from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    print('hello')
    return 'Hello, World!'

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='43.202.63.11', port=5000)

# 2024-