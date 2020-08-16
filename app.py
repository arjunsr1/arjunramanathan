import flask
import os
import random

app = flask.Flask(__name__)

image_link_set = dict()
pic_indexer = 0


@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')

def get_pics():
    context={}
    file_list = []
    img_dir = os.path.join(app.root_path, 'static/images')
    return os.listdir(img_dir)

@app.route('/api/randomurl/', methods=['GET'])
def get_random_pic():
    global image_link_set
    global pic_indexer
    context={}
    # if set is full, use global counter to index through set to display same pics in order.
    if len(get_pics()) == len(image_link_set):
        print ('set is of size ', len(image_link_set))
        url = image_link_set[pic_indexer]
        context['img_url'] = '/static/images/' + url
        pic_indexer = (pic_indexer + 1) % len(image_link_set)
        return flask.jsonify(**context)
    # get image file names.
    img_list = get_pics()
    img_list_len = len(img_list)
    temp = []
    for fn in img_list:
        # if set contains one, dont add it to temp array
        if fn not in image_link_set.values():
            temp.append(fn)
    
    url = random.choice(temp)
    image_link_set[pic_indexer] = (url)
    pic_indexer = (pic_indexer + 1) % img_list_len
    context['img_url'] = '/static/images/' + url
    print (context)
    return flask.jsonify(**context)
    # pick random image name from temp array and then add it to set

@app.route('/contact/', methods=['GET'])
def contact():
    return flask.render_template('contact.html')

@app.route('/photos/', methods=['GET'])
def photos():
    global image_link_set
    global pic_indexer
    context={}
    # if set is full, use global counter to index through set to display same pics in order.
    if len(get_pics()) == len(image_link_set):
        print ('set is of size ', len(image_link_set))
        url = image_link_set[pic_indexer]
        context['img_url'] = '/static/images/' + url
        pic_indexer = (pic_indexer + 1) % len(image_link_set)
        return flask.render_template('photos.html', **context)
        
    # get image file names.
    img_list = get_pics()
    img_list_len = len(img_list)
    temp = []
    for fn in img_list:
        # if set contains one, dont add it to temp array
        if fn not in image_link_set.values():
            temp.append(fn)
    
    url = random.choice(temp)
    image_link_set[pic_indexer] = (url)
    pic_indexer = (pic_indexer + 1) % img_list_len
    context['img_url'] = '/static/images/' + url
    print (pic_indexer)
    print ()
    print (context)
    return flask.render_template('photos.html', **context)

@app.route('/resume/', methods=['GET'])
def render_resume():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'), 'resume.pdf')

@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')