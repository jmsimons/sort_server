from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cf808b01eca1b48b52ac925de441a16c'

class Upload(FlaskForm):
    upload_file = FileField('Select file to upload')
    submit = SubmitField('Upload')

def list_sort(file): ### Reads file in as list, sorts, writes over file, returns list ###
    print('Listing and sorting {}'.format(file))
    with open('uploads/{}'.format(file)) as f: # Open file to read #
        list = f.read().split('\n')
    print('Listing and sorting {}'.format(file))
    list = sorted(list, key=str.lower) # list sorted #
    with open('uploads/{}'.format(file), 'w') as f: # Open file to write #
        for line in list:
            f.write('{}\n'.format(line))
    return list

@app.route('/', methods = ['GET', 'POST'])
def home(): ### Serves GET with html upload form, POST adds sorted lines to bottom of page ###
    form = Upload()
    if form.validate_on_submit():
        print(request.files)
        file = request.files['upload_file']
        file.save('uploads/{}'.format(file.filename))
        file = list_sort(file.filename)
        # Add file system link from Flask #
        print('Upload Successful')
        return render_template('index.html', form = form, title = 'Line Sort', file = file)
    return render_template('index.html', form = form, title = 'Line Sort')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')

'''
Additional Ideas:

    >Add a link to the file instead of print it out,
     would be more secure against client side injection

    >Add file extension validator

    >Add Bootstrap styles - or - style from scratch

    >Add logic for docx and other extensions (PDF, OpenOffice)

'''