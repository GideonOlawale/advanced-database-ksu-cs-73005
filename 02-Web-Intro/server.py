from contextlib import redirect_stderr
from bottle import route, template, run, redirect, get, post,request
import sqlite3
connection = sqlite3.connect('shopping_list.db')


@route('/')
@route('/list')
def get_list():
    cursor = connection.cursor()
    shopping_list = cursor.execute('select id, description from list')
    shopping_list = list(shopping_list)    
    shopping_list = [{'id':row[0], 'desc':row[1]} for row in shopping_list]
    return template('shopping_list', shopping_list = shopping_list, template_lookup=['C:/Users/gsodipo/Desktop/Gideon/Courses/Advanced Database and System/Classes/MyPractice/VisualStudio/02-Web-Intro'])

@route('/delete/<id>')
def get_delete(id):
    cursor = connection.cursor()
    cursor.execute(f'delete from list where id={id}')
    connection.commit()
    redirect('/list')

@get('/edit/<id>')
def get_edit(id):
    cursor = connection.cursor()
    item = cursor.execute(f'select description from list where id ={id}')
    item = list(item)
    item = item[0]
    return template('edit_item.tpl',item=item[0],id=id)

@post('/edit/<id>')
def post_edit(id):
    cursor = connection.cursor()
    item = request.forms.get('item')
    cursor.execute(f'update list set description="{item}" where id = {id}')
    connection.commit()
    redirect('/list')

@route('/add')
def get_add():
    return template('add_item.tpl')

@post('/add')
def post_add():
    cursor = connection.cursor()
    item = request.forms.get('newItem')
    cursor.execute(f'insert into list(description) values("{item}")')
    print("You have successfully inserted ",item)
    connection.commit()
    redirect('/')
run(host='localhost', debug = True, port = 8080)
    