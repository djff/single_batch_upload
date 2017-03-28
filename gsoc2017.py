from flask import Flask
from glam_templates import NationalArchieve as na
from glam_templates.NationalArchieve import NationalArchieve

app = Flask(__name__)

id_mapping = {
    'id_00001': NationalArchieve
}


@app.route('/')
def index():
    print('it works fine')
    return '<html><title>This is a test</title> <body> test this out </body> < /html'

@app.route('/upload/<string:GLAM>/<int:ID>/')
def upload(GLAM, ID):
    """

    :param GLAM: Name of GLAM institiution
    :param ID: Image unique identifier
    :return:
    """
    print(GLAM)
    glam_instance = id_mapping['id_00001']
    na.main(GLAM, ID)
    return '<html><title>This is a test</title> <body> <h1>operation successful </h1></body> </html>'

if __name__ == '__main__':
    app.run(
        port=4000
    )
