import re
from flask import Blueprint, render_template, redirect
from flaskr.models import Menu
from flaskr import db
import random

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/result')
def result():

    # params
    menus = []
    message = 'ガチャ結果'
    money = 1000
    balance = money
    total = 0


    while not menus:
        rand = random.randrange(
            0, db.session.query(Menu.id).count()
            ) + 1
        menus = db.session.query(Menu).filter(
            Menu.id == rand,
            Menu.category == 'drink',
            Menu.price <= balance
        ).all()

    # calc
    balance -= int(menus[0].price)

    # Appetizers
    count = 0
    while balance > 0:
        count += 1
        if count > 100:
            break

        candidate = db.session.query(Menu).filter(
            Menu.category == 'food',
            Menu.price <= balance
        ).all()

        if not candidate:
            break

        appetizers = random.choice(candidate)
        menus.append(appetizers)
        balance -= int(appetizers.price)

    total = money - balance


    return render_template('result.html', menus=menus, total=total)
