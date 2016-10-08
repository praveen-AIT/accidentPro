from app import db

class Blogpost(db.Model):

	__tablename__ = "accidents"

	serial = db.Column(db.Integer, primary_key=True)
	victim = db.Column(db.String)
	hospitals = db.Column(db.String)
	distance = db.Column(db.Integer)
	
	def __init__(self, victim, hospitals, distance):
		self.victim = victim
		self.hospitals = hospitals
		self.distance = distance

	def __repr__(self):
		return '{}-{}-{}'.format(self.victim, self.hospitals, self.distance)