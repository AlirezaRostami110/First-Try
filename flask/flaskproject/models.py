from flaskproject import db


class Student(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    subject = db.Column(db.String, unique = True, nullable = False)
    un_id = db.Column(db.Integer )
    verify_date = db.Column(db.Date)


    def __repr__(self):
            return f"Student('{self.name}', '{self.subject}', '{self.verify_date}', '{self.un_id}')"