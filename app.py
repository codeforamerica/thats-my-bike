import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def on_submit():
    
    filename = request.form['owner_name'] + '.txt'
    
    path = os.path.abspath(os.path.join('.','tmp',filename))
    
    ensure_dir(path)
    
    try:
        # Create text file.
        f = open(path, 'w')
        try:
            # Write form data to the casefile
            f.write(request.form['owner_name'])
        finally:
            f.close()
    except IOError:
        return "write failed"
    
    # See if it worked!
    try:
        f = open(path, 'r')
        try:
            f.read()
        finally:
            f.close()
    except IOError:
        return "read failed"
    
    return "all done!"


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

if __name__ == '__main__':
    port = int('PORT' in os.environ and os.environ['PORT'] or '5000')
    app.run(host='0.0.0.0',port=port)