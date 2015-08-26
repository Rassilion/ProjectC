# -*- coding: utf-8 -*-

from app import db
from app import models
from flask.ext.script import Command


class ResetDB(Command):
    """Drops all tables and recreates them"""

    def run(self, **kwargs):
        self.drop_collections()

    @staticmethod
    def drop_collections():
        db.drop_all()
        db.create_all()


class PopulateDB(Command):
    """Fills in predefined data to DB"""

    def run(self, **kwargs):
        self.create_roles()
        self.create_users()
        self.create_news()

    @staticmethod
    def create_roles():
        for role in ('admin', 'end-user', 'author'):
            models.user_datastore.create_role(name=role, description=role)
        models.user_datastore.commit()

    @staticmethod
    def create_users():
        for u in (('admin', 'admin@admin.com', '123456', ['admin'], True),
                  ('user', 'user@user.com', '123456', ['end-user'], True),
                  ('lavasystem', 'lava@lava.com', '123456', ['admin'], True),
                  ('tiya', 'tiya@lp.com', '123456', [], False)):
            user = models.user_datastore.create_user(
                username=u[0],
                email=u[1],
                password=u[2],
                roles=u[3],
                active=u[4]
            )

            models.user_datastore.commit()

    @staticmethod
    def create_news():
        u = [models.News(title=u'Duyuru 1',
                         body=u'<p>One must discover the sun in order to shape the doer of honorable mineral. Trust happens when you trap music so substantially that whatsoever you are easing is your pain. One must gain the lama in order to facilitate the cow of secret heaven. One must hurt the explosion of the anger in order to love the spirit of unconditional career. When the follower of resurrection knows the tantras of the lama, the politics will know power.<//p>'
                         ),
             models.News(title=u'Duyuru 2',
                         body=u'<p>Nunquam carpseris lapsus. Magnum, altus lunas vix acquirere de alter, mirabilis lapsus. Bassus, azureus vortexs aegre experientia de grandis, velox canis. Amicitia de camerarius assimilatio, experientia armarium! Ubi est lotus sensorem? Cum danista cadunt, omnes fortises demitto salvus, pius cannabises. Elevatus, medicina, et mensa. Cum sectam mori, omnes tuses captis fidelis, bi-color cobaltumes. Assimilant recte ducunt ad regius fraticinida. Audax, festus habitios nunquam locus de castus, altus clabulare.<//p>'
                         )]

        for i in u:
            db.session.add(i)

        db.session.commit()


if __name__ == "__main__":
    ResetDB.drop_collections()
    PopulateDB.create_roles()
    PopulateDB.create_users()
    PopulateDB.create_news()
