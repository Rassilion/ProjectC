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

body = u"""Mükemmel sayı, kendisi hariç bütün pozitif tam bölenlerinin toplamı kendisine eşit olan sayıdır.
Örneğin, 6 bir mükemmel sayıdır, çünkü pozitif bölenlerinin toplamı 1+2+3=6 kendisine eşittir.
Bu soruda size verilen inputun mükemmel sayı olup olmadığını belirteceksiniz.

### Özet:
	Girilen sayı mükemmel sayı ise "YES", değilse "NO" bastırınız.

### Input biçimi:
	Tek bir satırda bir tam sayı, N.
	0<N<10^9

### Output biçimi:
	Input'ta girilen sayı mükemmel ise "YES", değil ise "NO".
	Output'un sonuna endline ("\\n") koyabilirsiniz.

| Örnek Input 1: |\n
| -------------- |\n
| 28             |\n

| Örnek Output 1: |\n
| --------------- |\n
| YES             |\n

* Örnek 1'de input olarak verilen sayının kendisi hariç pozitif tam bölenlerinin toplamı 1+2+4+7+14=28. Bu nedenle 28 bir mükemmel sayıdır. Bu yüzden Örnek 1'in output'u "YES" olmalı.

| Örnek Input 2: |\n
| -------------- |\n
| 38             |\n

| Örnek Output 2: |\n
| --------------- |\n
| NO              |\n

* Örnek 2'de input olarak verilen sayının kendisi hariç pozitif tam bölenlerinin toplamı 1+2+19=22. 22, 38'e eşit olmadığı için 38 bir mükemmel sayı değildir. Bu nedenle Örnek 2'nin output'u "NO" olmalı.


"""
p = [models.Problems(title=u'Mükemmel sayı', body=body, count=5620, related='Basic op',
                     difficulty='Z1',
                     ),
     models.Problems(title=u'Bozuk sayı', body='bozuk_sayi', count=55, related='Basic op',
                     difficulty='Z51',
                     ),
     models.Problems(title=u'Yamuk sayı', body='yamuk_sayi', count=620, related='Basic op',
                     difficulty='Z61',
                     ),
     models.Problems(title=u'Bozuk 2', body='bozuk_2', count=270, related='Basic op', difficulty='Z15',
                     ),
     models.Problems(title=u'Yamuk 2', body='yamuk_2', count=20, related='Basic op', difficulty='Z13',
                     ),
     models.Problems(title=u'sayı 2', body='sayi_2', count=220, related='Basic op', difficulty='Z12',
                     ),
     models.Problems(title=u'sayı 25', body='sayi_25', count=20, related='Basic op', difficulty='Z12',
                     )]
for i in p:
    db.session.add(i)

db.session.commit()
