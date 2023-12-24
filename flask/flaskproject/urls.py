from flaskproject import app, db
from .models import Student
from flask import render_template, request, redirect, flash
from .forms import StudentCreateForm, StudentUpdateForm



@app.route('/')
def home():
    all_st = Student.query.all()
    return render_template('home.html', students= all_st)

@app.route('/details/<int:st_id>/')
def details(st_id):
    student = Student.query.filter_by(un_id=st_id).first()
    return render_template('details.html', student= student)


@app.route('/delete/<int:st_id>')
def delete(st_id):
    st = Student.query.get(st_id)
    db.session.delete(st)
    db.session.commit()
    flash('Student delete successfully', 'success')

    return redirect('/')


@app.route('/create/', methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        form = StudentCreateForm(request.form) 

        if form.validate():
            name = form.name.data
            subject = form.subject.data
            verify_date = form.verify_date.data
            un_id = form.un_id.data


            new_student = Student(name=name, subject=subject, verify_date=verify_date, un_id=un_id)

            db.session.add(new_student)
            db.session.commit()

            flash('Student added successfully!', 'success')
            return redirect('/')
    else:
        form = StudentCreateForm()

    return render_template('create.html', form=form)


    

@app.route('/update/<int:st_id>', methods=['GET', 'POST'])
def update(st_id):
    student = Student.query.get(st_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.form, obj=student)

        if form.validate():
            form.populate_obj(student)
            db.session.commit()
            flash('Updated Successfully!', 'success')
            return redirect(f'/details/{st_id}')
    else:
        form = StudentUpdateForm(obj=student)

    return render_template('update.html', form=form)

