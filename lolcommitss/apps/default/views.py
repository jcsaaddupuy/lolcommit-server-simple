# coding: utf-8
from __future__ import unicode_literals


from flask import make_response
from flask import Blueprint
from flask import current_app as c

# webargs
from webargs import Arg
from webargs.flaskparser import use_args
from werkzeug.datastructures import FileStorage

from flask import render_template
from .models import LolCommit

try:
    from urlib.parse import quote
except ImportError:
    from urllib2 import quote

blueprint = Blueprint('default', __name__, template_folder='templates')


@blueprint.route('/upload', methods=['POST', ])
@use_args({
    'file': Arg(required=True, validate=lambda f: isinstance(f, FileStorage)),
    'repo': Arg(str, required=True),
    'author_name': Arg(str, required=False),
    'author_email': Arg(str, required=False),
    'message': Arg(str, required=False),
    'sha': Arg(str, required=False),
}, locations=('files', 'form'))  # yapf: disable
def upload(args):
    repo = args['repo']
    _file = args['file']
    author_name = args['author_name']
    author_email = args['author_email']
    message = args['message']
    sha = args['sha']

    filename = c.photos.save(_file, folder=repo)

    commit = LolCommit(repo=repo, filename=filename, message=message, author_email=author_email, author_name=author_name, sha=sha)
    c.db.session.add(commit)
    c.db.session.commit()

    return make_response('Ok', 200)


@blueprint.route('/', methods=['GET', ])
def root():

    from sqlalchemy.sql import select
    stmt = select([LolCommit.repo]).group_by(LolCommit.repo)
    results = c.db.session.execute(stmt)

    results = {r[0]: '/repo/' + quote(r[0], safe='') for r in results}
    return render_template('root.html.j2', repos=results)


@blueprint.route('/repo/<path:repo>', methods=['GET', ])
def repo(repo):
    commits = c.db.session.query(LolCommit).filter(LolCommit.repo == repo).all()
    return render_template('repo.html.j2', commits=commits)
