import flask
import os

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')

@app.route('/contact/', methods=['GET'])
def contact():
    return flask.render_template('contact.html')

@app.route('/photos/', methods=['GET'])
def photos():
    return flask.render_template('photos.html')

@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')