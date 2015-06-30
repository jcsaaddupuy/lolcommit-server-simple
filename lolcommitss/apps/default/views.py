# coding: utf-8
from __future__ import unicode_literals

import os

from flask import make_response
from flask import Blueprint
from flask import current_app as c

# webargs
from webargs import Arg
from webargs.flaskparser import use_args
from werkzeug.datastructures import FileStorage
from flaskext.uploads import UploadSet, IMAGES

from flask import url_for
from flask import render_template
from .models import Photo

blueprint = Blueprint('default', __name__, template_folder='templates')


@blueprint.route('/upload', methods=['POST', ])
@use_args({
    'file': Arg(required=True, validate=lambda f : isinstance(f, FileStorage)),
    'repo': Arg(str, required=True),
}, locations=('files', 'form'))  # yapf: disable
def upload(args):
    repo = args['repo']
    _file = args['file']
    filename = c.photos.save(_file, folder=repo)

    photo = Photo(repo=repo, filename=filename)
    c.db.session.add(photo)
    c.db.session.commit()

    return make_response('Ok', 200)

@blueprint.route('/', methods=['GET', ])
def root():
    return render_template('root.html.j2')

@blueprint.route('/repo/<repo>', methods=['GET', ])
def repo(repo):
    photos = c.db.session.query(Photo).filter(Photo.repo == repo).all()
    return render_template('repo.html.j2', photos = photos)
