# -*- coding: utf-8 -*-
from app import db
from app import models
import datetime

db.create_all()

u = [models.News(title='Duyuru 1',
                 body='<p>One must discover the sun in order to shape the doer of honorable mineral. Trust happens when you trap music so substantially that whatsoever you are easing is your pain. One must gain the lama in order to facilitate the cow of secret heaven. One must hurt the explosion of the anger in order to love the spirit of unconditional career. When the follower of resurrection knows the tantras of the lama, the politics will know power.<//p>',
                 timestamp=datetime.datetime.utcnow()),
     models.News(title='Duyuru 2',
                 body='<p>Nunquam carpseris lapsus. Magnum, altus lunas vix acquirere de alter, mirabilis lapsus. Bassus, azureus vortexs aegre experientia de grandis, velox canis. Amicitia de camerarius assimilatio, experientia armarium! Ubi est lotus sensorem? Cum danista cadunt, omnes fortises demitto salvus, pius cannabises. Elevatus, medicina, et mensa. Cum sectam mori, omnes tuses captis fidelis, bi-color cobaltumes. Assimilant recte ducunt ad regius fraticinida. Audax, festus habitios nunquam locus de castus, altus clabulare.<//p>',
                 timestamp=datetime.datetime.utcnow())]

for i in u:
    db.session.add(i)

body = u'<p>Kendi hariç bütün sayıları....</p><p>Girdi: asdsadsad</p><p>Çıktı: asdsadsa</p><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">Örnek Girdi</h3></div><div class="panel-body">28</div></div><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">Örnek Çıktı</h3></div><div class="panel-body">EVET</div></div>'

p = [models.Problems(title=u'Mükemmel sayı', slug='mukemmel_sayi', body=body, count=5620, related='Basic op',
                     difficulty='Z1',
                     timestamp=datetime.datetime.utcnow()),
     models.Problems(title=u'Bozuk sayı', slug='bozuk_sayi', body='bozuk_sayi', count=55, related='Basic op',
                     difficulty='Z51',
                     timestamp=datetime.datetime.utcnow()),
     models.Problems(title=u'Yamuk sayı', slug='yamuk_sayi', body='yamuk_sayi', count=620, related='Basic op',
                     difficulty='Z61',
                     timestamp=datetime.datetime.utcnow()),
     models.Problems(title=u'Bozuk 2', slug='bozuk_2', body='bozuk_2', count=270, related='Basic op', difficulty='Z15',
                     timestamp=datetime.datetime.utcnow()),
     models.Problems(title=u'Yamuk 2', slug='yamuk_2', body='yamuk_2', count=20, related='Basic op', difficulty='Z13',
                     timestamp=datetime.datetime.utcnow()),
     models.Problems(title=u'sayı 2', slug='sayi_2', body='sayi_2', count=220, related='Basic op', difficulty='Z12',
                     timestamp=datetime.datetime.utcnow()),
     models.Problems(title=u'sayı 25', slug='sayi_25', body='sayi_25', count=20, related='Basic op', difficulty='Z12',
                     timestamp=datetime.datetime.utcnow())]
for i in p:
    db.session.add(i)

db.session.commit()