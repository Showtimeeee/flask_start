from flask import Flask, render_template, request, flash, url_for, redirect

from peewee import IntegrityError, fn

from config import SECRET_KEY, DEBUG

from models import English


app = Flask(__name__)
app.config.from_object(__name__)


lst_main_menu = [{'name': 'Главная', 'url': '/'},
                 {'name': 'Добавить', 'url': '/add'},
                 {'name': 'Обновить', 'url': '/update'},
                 {'name': 'Удалить', 'url': '/delete'},
                 {'name': 'Просмотр', 'url': '/show'}]


@app.route('/')
def index():
    return render_template('index.html', title='Главная страница', lst_main_menu=lst_main_menu)


@app.route('/add')
def add():
    return render_template('add.html', title='Добавить', lst_main_menu=lst_main_menu)


@app.route('/update')
def update():
    return render_template('update.html', title='Обновить', lst_main_menu=lst_main_menu)


@app.route('/delete')
def delete():
    return render_template('delete.html', title='Удалить', lst_main_menu=lst_main_menu)


@app.route('/show')
def show():
    return render_template('show.html', title='Просмотр', lst_main_menu=lst_main_menu)


if __name__ == "__main__":
    app.run(debug=DEBUG, port=8000)

