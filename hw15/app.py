#!/var/www/u997259/data/flaskenv/bin/python3

import sys

from flask import Flask, render_template, request, redirect, url_for  
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker  
from database_setup import Base, Methodics, Reagents, Assigns  
  
app = Flask(__name__)  
  
# Подключаемся и создаем сессию базы данных  
engine = create_engine("mysql+pymysql://u997259_test:Waha40k@localhost/u997259_test")
Base.metadata.bind = engine  
  
DBSession = sessionmaker(bind=engine)  
session = DBSession()  
  
  
# Эта функция работает в режиме чтения.  
@app.route('/')
def showIndex():
    return render_template("index.html")

@app.route('/methodics')  
def showMethodics():
    query = session.query(Methodics, Reagents)
    query = query.outerjoin(Assigns, Assigns.methodic_id == Methodics.id)
    query = query.outerjoin(Reagents, Reagents.id == Assigns.reagent_id)
    all_methodics = query.all()
    methodics = {}
    for methodic, reagent in all_methodics:
        if not methodics.get(methodic):
            methodics[methodic] = []
            if reagent:
                methodics[methodic].append(reagent.name)
            else:
                methodics[methodic].append("")
        else:
            if reagent:
                methodics[methodic].append(reagent.name)
            else:
                methodics[methodic].append("")
        
    return render_template("methodics.html", methodics=methodics)  
  
  
@app.route('/methodics/new/', methods=['GET', 'POST'])  
def newMethodic():  
    if request.method == 'POST':  
        newMethodic = Methodics(name=request.form['name'], year=request.form['year'])  
        session.add(newMethodic)  
        session.commit()  
        return redirect(url_for('showMethodics'))  
    else:  
        return render_template('newMethodic.html')  
  
  
@app.route("/methodics/<int:methodic_id>/edit/", methods=['GET', 'POST'])  
def editMethodic(methodic_id):  
    editedMethodic = session.query(Methodics).filter_by(id=methodic_id).one()
    if request.method == 'POST':
        if request.form['name']:  
            if request.form['year']:
                editedMethodic.name = request.form['name']
                editedMethodic.year = request.form['year']
                session.commit()
                return redirect(url_for('showMethodics'))
            else:  
                return render_template('editMethodic.html', methodic=editedMethodic)  
        else:  
            return render_template('editMethodic.html', methodic=editedMethodic)  
    else:  
        return render_template('editMethodic.html', methodic=editedMethodic)  
  
  
@app.route('/methodics/<int:methodic_id>/delete/', methods=['GET', 'POST'])  
def deleteMethodic(methodic_id):  
    methodicToDelete = session.query(Methodics).filter_by(id=methodic_id).one()  
    if request.method == 'POST':  
        session.delete(methodicToDelete)  
        session.commit()  
        return redirect(url_for('showMethodics', methodic_id=methodic_id))  
    else:  
        return render_template('deleteMethodic.html', methodic=methodicToDelete)


@app.route('/reagents')  
def showReagents():
    query = session.query(Reagents, Methodics)
    query = query.outerjoin(Assigns, Assigns.reagent_id == Reagents.id)
    query = query.outerjoin(Methodics, Methodics.id == Assigns.methodic_id)
    all_reagents = query.all()
    reagents = {}
    for reagent, methodic in all_reagents:
        if not reagents.get(reagent):
            reagents[reagent] = []
            if methodic:
                reagents[reagent].append(methodic.name)
            else:
                reagents[reagent].append("")
        else:
            if methodic:
                reagents[reagent].append(methodic.name)
            else:
                reagents[reagent].append("")
        
    return render_template("reagents.html", reagents=reagents)  
  
  
@app.route('/reagents/new/', methods=['GET', 'POST'])  
def newReagent():  
    if request.method == 'POST':  
        newReagent = Reagents(name=request.form['name'], qty=request.form['qty'], best=request.form['best'])  
        session.add(newReagent)  
        session.commit()  
        return redirect(url_for('showReagents'))  
    else:  
        return render_template('newReagent.html')  
  
  
@app.route("/reagents/<int:reagent_id>/edit/", methods=['GET', 'POST'])  
def editReagent(reagent_id):  
    editedReagent = session.query(Reagents).filter_by(id=reagent_id).one()
    if request.method == 'POST':
        if request.form['name']:  
            if request.form['qty']:
                if request.form['best']:
                    editedReagent.name = request.form['name']
                    editedReagent.qty = request.form['qty']
                    editedReagent.best = request.form['best']
                    session.commit()
                    return redirect(url_for('showReagents'))
                else:  
                    return render_template('editReagent.html', reagent=editedReagent)  
            else:  
                return render_template('editReagent.html', reagent=editedReagent) 
        else:  
            return render_template('editReagent.html', reagent=editedReagent)  
    else:  
        return render_template('editReagent.html', reagent=editedReagent)  
  
  
@app.route('/reagents/<int:reagent_id>/delete/', methods=['GET', 'POST'])  
def deleteReagent(reagent_id):  
    reagentToDelete = session.query(Reagents).filter_by(id=reagent_id).one()  
    if request.method == 'POST':  
        session.delete(reagentToDelete)  
        session.commit()  
        return redirect(url_for('showReagents', reagent_id=reagent_id))  
    else:  
        return render_template('deleteReagent.html', reagent=reagentToDelete)
  

@app.route('/assigns/new/', methods=['GET', 'POST'])  
def newAssign():  
    if request.method == 'POST':  
        try:
            methodic_to_assign = session.query(Methodics).filter_by(name=request.form['methodic']).one() 
            reagent_to_assign = session.query(Reagents).filter_by(name=request.form['reagent']).one() 
            newAssign = Assigns(methodic_id=methodic_to_assign.id, reagent_id=reagent_to_assign.id)  
            session.add(newAssign)  
            session.commit()  
            return redirect(url_for('showMethodics'))
        except (NameError, NoResultFound):
            return render_template('newAssign.html') 
    else:  
        return render_template('newAssign.html') 

  
if __name__ == '__main__':  
    app.debug = True  
    app.run(port=4996)