from random import randrange
from flask import abort, flash, redirect, render_template, url_for
from .models import Opinion
from .forms import OpinionForm
from . import app, db


@app.route('/')
def index_view():
    """Показывает случайное мнение."""
    quantity = Opinion.query.count()
    if not quantity:
        abort(500)
    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()
    return render_template('opinion.html', opinion=opinion)


@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    """Добавляет новое мнение."""
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first() is not None:
            flash('Такое мнение уже было оставлено ранее!')
            return render_template('add_opinion.html', form=form)
        opinion = Opinion(
            title=form.title.data, text=text, source=form.source.data
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)


@app.route('/opinion/<int:id>')
def opinion_view(id):
    """Показывает мнение по его идентификатору."""
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)
