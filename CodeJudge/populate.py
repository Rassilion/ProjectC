from models import Submission
from CodeJudge import db

for i in range(10):
    s=Submission(problem_id=1,user_id=1,code='lololololo'+str(i))
    print s.code
    db.add(s)

db.commit()