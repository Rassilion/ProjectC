from models import Submission
from CodeJudge import db

print db.query(Submission).all()
p=db.query(Submission).filter_by(error=None).first()

while p:
    p.error='ok'
    p =db.query(Submission).filter_by(error=None).first()


db.commit()