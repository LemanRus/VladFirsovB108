#!/var/www/u997259/data/flaskenv/bin/python3

import sys
import os

from flask import Flask, render_template, request, redirect, url_for  
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from database_setup import Methodics, Reagents, Assigns
from database_session import DBSession

app = Flask(__name__)  

@app.route('/')
def show_index():
    return render_template("index.html")

@app.route('/methodics')  
def show_methodics():
    with DBSession() as session:
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
def add_methodic():  
    with DBSession() as session:
        if request.method == 'POST':  
            new_methodic = Methodics(name=request.form['name'], year=request.form['year'])  
            session.add(new_methodic)  
            session.commit()  
            return redirect(url_for('show_methodics'))  
        else:  
            return render_template('new_methodic.html')  


@app.route("/methodics/<int:methodic_id>/edit/", methods=['GET', 'POST'])  
def edit_methodic(methodic_id):
    with DBSession() as session:  
        edited_methodic = session.query(Methodics).filter_by(id=methodic_id).one()
        if request.method == 'POST' and request.form['name'] and request.form['year']:
            edited_methodic.name = request.form['name']
            edited_methodic.year = request.form['year']
            session.commit()
            return redirect(url_for('show_methodics'))
        else:  
            return render_template('edit_methodic.html', methodic=edited_methodic)  


@app.route('/methodics/<int:methodic_id>/delete/', methods=['GET', 'POST'])  
def delete_methodic(methodic_id):
    with DBSession() as session:  
        methodic_to_delete = session.query(Methodics).filter_by(id=methodic_id).one()  
        if request.method == 'POST':  
            session.delete(methodic_to_delete)  
            session.commit()  
            return redirect(url_for('show_methodics', methodic_id=methodic_id))  
        else:  
            return render_template('delete_methodic.html', methodic=methodic_to_delete)


@app.route('/reagents')  
def show_reagents():
    with DBSession() as session:
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
def add_reagent():
    with DBSession() as session:  
        if request.method == 'POST':  
            new_reagent = Reagents(name=request.form['name'], qty=request.form['qty'], best=request.form['best'])  
            session.add(new_reagent)  
            session.commit()  
            return redirect(url_for('show_reagents'))  
        else:  
            return render_template('new_reagent.html')  


@app.route("/reagents/<int:reagent_id>/edit/", methods=['GET', 'POST'])  
def edit_reagent(reagent_id):
    with DBSession() as session:  
        edited_reagent = session.query(Reagents).filter_by(id=reagent_id).one()
        if request.method == 'POST' and request.form['name'] and request.form['qty'] and request.form['best']:
            edited_reagent.name = request.form['name']
            edited_reagent.qty = request.form['qty']
            edited_reagent.best = request.form['best']
            session.commit()
            return redirect(url_for('show_reagents'))
        else:  
            return render_template('edit_reagent.html', reagent=edited_reagent)  


@app.route('/reagents/<int:reagent_id>/delete/', methods=['GET', 'POST'])  
def delete_reagent(reagent_id):
    with DBSession() as session:  
        reagent_to_delete = session.query(Reagents).filter_by(id=reagent_id).one()  
        if request.method == 'POST':  
            session.delete(reagent_to_delete)  
            session.commit()  
            return redirect(url_for('show_reagents', reagent_id=reagent_id))  
        else:  
            return render_template('delete_reagent.html', reagent=reagent_to_delete)


@app.route('/assigns/new/', methods=['GET', 'POST'])  
def new_assign():
    with DBSession() as session:
        query = session.query(Methodics, Reagents)
        # FULL JOIN не работает в MySQL
        # query = session.execute("SELECT met.id, met.name, met.year FROM Methodics met FULL JOIN Reagents rea ON met.id=rea.id")
        query = session.execute("SELECT met.name, rea.name FROM methodics met LEFT JOIN reagents rea ON rea.id = met.id \
            UNION \
                SELECT met.name, rea.name FROM methodics met RIGHT JOIN reagents rea ON rea.id = met.id;")
        all = query.all()  
        if request.method == 'POST':  
            try:
                methodic_got = request.form
                reagent_got = request.form
                methodic_to_assign = session.query(Methodics).filter_by(name=request.form.get('methodic')).one() 
                reagent_to_assign = session.query(Reagents).filter_by(name=request.form.get('reagent')).one() 
                new_assign = Assigns(methodic_id=methodic_to_assign.id, reagent_id=reagent_to_assign.id)  
                session.add(new_assign)  
                session.commit()  
                return redirect(url_for('show_methodics'))
            except (NameError, NoResultFound, MultipleResultsFound) as err:
                return render_template('error.html', args = [methodic_got, reagent_got], error=err) 
        else:  
            return render_template('new_assign.html', all=all) 


if __name__ == '__main__':  
    app.debug = True  
    app.run(port=4996)