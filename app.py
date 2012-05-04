from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def on_submit():
    
    return 'has "owner_name": %s' % ('owner_name' in request.form)

if __name__ == '__main__':
    app.run()