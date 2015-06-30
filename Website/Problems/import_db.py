# -*- coding: utf-8 -*-

import codecs
import os
import errno
from datetime import datetime
from app import db
from app import models
from app.config import Config
from shutil import copy
import markdown
from flask.ext.script import Command


class ImportDB(Command):
    """Imports problem markdown to database"""

    def run(self, **kwargs):
        self.import_db()

    @staticmethod
    def import_db():
        # bütün problemler
        problems = os.listdir(os.path.dirname(os.path.abspath(__file__)))
        # flask basedir
        basedir = Config.basedir
        static_resources_dir = os.path.join(basedir, 'static', 'resources')
        # markdown meta eklentili
        md = markdown.Markdown(extensions=['meta'])
        for i in problems:
            # dosya adında nokta varsa atla
            if "." in i:
                continue
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), i)
            # metadatyı oku
            input_file = codecs.open(os.path.join(path, 'meta'), mode="r", encoding="utf-8-sig")
            text = input_file.read()
            # metadatyı işle
            html = md.convert(text)
            # soruyu oku
            input_file = codecs.open(os.path.join(path, 'question.md'), mode="r", encoding="utf-8-sig")
            text = input_file.read()
            # çözümü oku
            input_file = codecs.open(os.path.join(path, 'solution.md'), mode="r", encoding="utf-8-sig")
            text2 = input_file.read()

            if models.Problem.query.filter_by(title=md.Meta['title'][0]).first() is None:
                # sql nesnesini yarat ve database ekle
                author = models.User.query.filter_by(username=md.Meta['author'][0]).first()
                if author is None:
                    author = models.User.query.filter_by(username="admin").first()
                prob = models.Problem(title=md.Meta['title'][0], body=text, solution=text2)
                # tarihi düzenle
                prob.timestamp = datetime.strptime(md.Meta['date'][0], "%Y-%m-%d")
                # tag ekle
                for i in md.Meta['relate']:
                    tag = models.get_or_create(models.Tag, name=i)
                    prob.tags.append(tag)
                # soruya yazar ekle
                author.problems.append(prob)
            else:
                print "skip " + md.Meta['title'][0]
            # eğer resources verildiyse kopyala copy
            if os.path.isdir(os.path.join(path, 'resources')):
                resdir = os.path.join(path, 'resources')
                res = os.listdir(resdir)
                dest_res = os.path.join(static_resources_dir, i)
                # hedef klasör yoksa yarat
                try:
                    os.makedirs(dest_res)
                except OSError as exception:
                    if exception.errno != errno.EEXIST:
                        raise
                # bütün resourceleri kopyala i/resources to resources/i
                for j in res:
                    copy(os.path.join(resdir, j), os.path.join(dest_res, j))

        # database değişikliklerini kaydet
        db.session.commit()


if __name__ == "__main__":
    ImportDB.import_db()
