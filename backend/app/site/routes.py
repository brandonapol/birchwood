from flask import Blueprint

site = Blueprint('site', __name__)

@site.route('/test')
def test():
    return '<h2>it worked</h2>'