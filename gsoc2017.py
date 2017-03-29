from flask import Flask
from glam_templates import NationalArchieve as na
from glam_templates.NationalArchieve import NationalArchieve

app = Flask(__name__)

glam_mapping = {
    'National Archieve': NationalArchieve
}

better_naming = [
    {
        'name': 'National Archieve'
    }
]


@app.route('/')
def index():
    print('it works fine')
    return '<html><title>This is a test</title> <body> test this out </body> < /html>'

@app.route('/upload/<string:GLAM>/<int:ID>/',)
def upload(GLAM, ID):
    """

    :param GLAM: Name of GLAM institiution
    :param ID: Image unique identifier
    :return:
    """
    print(GLAM)
    try:

        glam_instance = glam_mapping[GLAM]
    except:
        return '<html><title>This is a test</title> <body> <h1>Glam Template not found</h1></body> </html>'
    success = na.main(GLAM, ID)
    if success:
        return '<html><title>This is a test</title> <body> <h1>operation successful </h1></body> </html>'
    else:
        return '<html><title>This is a test</title> <body> <h1>operation Failed </h1></body> </html>'

if __name__ == '__main__':
    app.run(
        port=8090
    )
