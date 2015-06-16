# -*- coding: utf-8 -*-

from app import db
from app import models

db.drop_all()
db.create_all()

u = [models.News(title=u'Duyuru 1',
                 body=u'<p>One must discover the sun in order to shape the doer of honorable mineral. Trust happens when you trap music so substantially that whatsoever you are easing is your pain. One must gain the lama in order to facilitate the cow of secret heaven. One must hurt the explosion of the anger in order to love the spirit of unconditional career. When the follower of resurrection knows the tantras of the lama, the politics will know power.<//p>'
                 ),
     models.News(title=u'Duyuru 2',
                 body=u'<p>Nunquam carpseris lapsus. Magnum, altus lunas vix acquirere de alter, mirabilis lapsus. Bassus, azureus vortexs aegre experientia de grandis, velox canis. Amicitia de camerarius assimilatio, experientia armarium! Ubi est lotus sensorem? Cum danista cadunt, omnes fortises demitto salvus, pius cannabises. Elevatus, medicina, et mensa. Cum sectam mori, omnes tuses captis fidelis, bi-color cobaltumes. Assimilant recte ducunt ad regius fraticinida. Audax, festus habitios nunquam locus de castus, altus clabulare.<//p>'
                 )]

for i in u:
    db.session.add(i)

db.session.commit()
