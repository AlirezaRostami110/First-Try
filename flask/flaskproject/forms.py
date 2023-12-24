from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField
from wtforms.validators import DataRequired, length



class StudentCreateForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), length(min=5, max= 35)])
    subject = StringField('Subject',validators=[DataRequired(), length(min=2, max= 40)])
    un_id = IntegerField('UN_ID',validators=[DataRequired()])
    verify_date = DateField('Verification Date',validators=[DataRequired()])


class StudentUpdateForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), length(min=5, max= 35)])
    subject = StringField('Subject',validators=[DataRequired(), length(min=2, max= 40)])
    un_id = IntegerField('UN_ID',validators=[DataRequired()])
    verify_date = DateField('Verification Date',validators=[DataRequired()])
