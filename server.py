from flask import Flask, render_template
from flask import request
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_routes(page_name=None):
    return render_template(f'{page_name}.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([name,email,subject,message])

@app.route('/contact_form', methods=['POST', 'GET'] )
def contact_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('/thankyou.html', name=data['name'])
        except:
            return 'error with database'
    else:
        return render_template('/thankyou.html', error='Oops, Something Went Wrong!')

if __name__ == "__main__":
    app.run(debug=True)
