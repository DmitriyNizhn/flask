from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


ARTICLES = {
    1: {'author': 2,
        'title': 'text 1',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam aut corporis delectus\n'
                'dignissimos doloremque ex facere fuga, fugiat ipsam iste, minima modi nesciunt obcaecati \n'
                'odit optio reiciendis totam voluptas voluptate.'},
    2: {'author': 1,
        'title': 'text 2',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam aut corporis delectus\n'
                'dignissimos doloremque ex facere fuga, fugiat ipsam iste, minima modi nesciunt obcaecati \n'
                'odit optio reiciendis totam voluptas voluptate.'},
}

@article.route('/')
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)

@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'Article id {pk} not found')
    return render_template('articles/detail.html', article=article)