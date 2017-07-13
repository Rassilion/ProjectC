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

# TODO read testcases from files
testcases = [['14 \n5 9 4 19 11 17 12 13 14 1 16 20 15 6 \n', '2  \r\n 3    \n \t 7  \n  8 10  \n  18 \n'],
             ['1 \n8 \n', '1 2 3 4 5 6 7 9 10 11 12 13 14 15 16 17 18 19 20 \n'],
             ['17 \n5 1 3 12 11 4 20 15 14 13 6 18 17 2 16 7 9 \n', '8 10 19 \n'],
             ['15 \n9 6 5 7 3 8 17 11 2 14 15 16 1 10 13 \n', '4 12 18 19 20 \n'],
             ['7 \n18 10 19 12 13 20 11 \n', '1 2 3 4 5 6 7 8 9 14 15 16 17 \n'],
             ['13 \n9 10 7 6 8 3 12 18 1 15 2 20 13 \n', '4 5 11 14 16 17 19 \n'],
             ['12 \n7 12 15 4 11 19 17 6 16 18 2 10 \n', '1 3 5 8 9 13 14 20 \n'],
             ['14 \n1 20 6 8 14 19 7 2 16 9 3 18 13 11 \n', '4 5 10 12 15 17 \n'],
             ['16 \n10 11 3 9 18 16 14 7 12 2 1 17 6 5 20 15 \n', '4 8 13 19 \n'],
             ['16 \n4 1 8 5 10 17 20 18 9 3 16 2 14 11 13 12 \n', '6 7 15 19 \n'],
             ['12 \n3 7 19 12 17 20 14 18 2 13 1 6 \n', '4 5 8 9 10 11 15 16 \n'],
             ['10 \n11 20 16 10 17 9 18 19 7 6 \n', '1 2 3 4 5 8 12 13 14 15 \n'],
             ['6 \n20 14 15 5 12 16 \n', '1 2 3 4 6 7 8 9 10 11 13 17 18 19 \n'],
             ['18 \n13 14 6 18 19 5 11 9 10 17 7 1 16 3 15 20 4 8 \n', '2 12 \n'],
             ['15 \n2 16 6 15 5 11 19 13 20 14 3 7 17 8 4 \n', '1 9 10 12 18 \n'],
             ['4 \n12 15 8 14 \n', '1 2 3 4 5 6 7 9 10 11 13 16 17 18 19 20 \n'],
             ['6 \n14 1 18 8 4 6 \n', '2 3 5 7 9 10 11 12 13 15 16 17 19 20 \n'],
             ['8 \n14 7 10 18 17 5 2 16 \n', '1 3 4 6 8 9 11 12 13 15 19 20 \n'],
             ['20 \n15 3 12 4 10 9 20 6 7 13 19 18 8 14 11 16 2 17 1 5 \n', ' \n'],
             ['13 \n7 4 12 11 14 5 17 1 8 19 3 16 15 \n', '2 6 9 10 13 18 20 \n'],
             ['2 \n2 1 \n', '3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 \n'],
             ['8 \n9 6 5 11 8 20 15 7 \n', '1 2 3 4 10 12 13 14 16 17 18 19 \n'],
             ['19 \n6 9 17 1 15 16 2 13 4 10 19 8 3 12 5 7 14 11 18 \n', '20 \n'],
             ['2 \n8 19 \n', '1 2 3 4 5 6 7 9 10 11 12 13 14 15 16 17 18 20 \n'],
             ['8 \n7 11 12 15 17 1 4 20 \n', '2 3 5 6 8 9 10 13 14 16 18 19 \n'],
             ['14 \n17 18 7 19 20 4 9 3 5 6 14 16 11 8 \n', '1 2 10 12 13 15 \n'],
             ['13 \n7 5 8 11 14 6 9 3 2 12 15 17 1 \n', '4 10 13 16 18 19 20 \n'],
             ['19 \n6 11 19 7 5 20 14 10 12 8 1 13 15 9 3 18 16 4 2 \n', '17 \n'],
             ['8 \n3 4 17 9 15 5 10 20 \n', '1 2 6 7 8 11 12 13 14 16 18 19 \n'],
             ['6 \n18 15 10 4 1 12 \n', '2 3 5 6 7 8 9 11 13 14 16 17 19 20 \n'],
             ['15 \n18 15 8 13 6 9 17 4 10 11 1 5 12 14 20 \n', '2 3 7 16 19 \n'],
             ['14 \n18 3 5 19 6 7 2 20 12 14 11 1 15 17 \n', '4 8 9 10 13 16 \n'],
             ['0 \n \n', '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 \n'],
             ['2 \n14 7 \n', '1 2 3 4 5 6 8 9 10 11 12 13 15 16 17 18 19 20 \n'],
             ['4 \n4 20 16 7 \n', '1 2 3 5 6 8 9 10 11 12 13 14 15 17 18 19 \n'],
             ['6 \n17 4 16 2 19 1 \n', '3 5 6 7 8 9 10 11 12 13 14 15 18 20 \n'],
             ['2 \n16 9 \n', '1 2 3 4 5 6 7 8 10 11 12 13 14 15 17 18 19 20 \n'],
             ['4 \n4 9 7 16 \n', '1 2 3 5 6 8 10 11 12 13 14 15 17 18 19 20 \n'],
             ['14 \n5 3 14 9 4 2 16 11 10 12 7 20 18 17 \n', '1 6 8 13 15 19 \n'],
             ['8 \n14 19 5 20 18 12 3 16 \n', '1 2 4 6 7 8 9 10 11 13 15 17 \n'],
             ['3 \n15 6 3 \n', '1 2 4 5 7 8 9 10 11 12 13 14 16 17 18 19 20 \n'],
             ['13 \n1 20 11 7 8 19 9 13 10 18 12 17 4 \n', '2 3 5 6 14 15 16 \n'],
             ['10 \n5 12 3 1 7 15 4 2 9 19 \n', '6 8 10 11 13 14 16 17 18 20 \n'],
             ['7 \n8 16 2 5 20 9 11 \n', '1 3 4 6 7 10 12 13 14 15 17 18 19 \n'],
             ['14 \n17 4 20 1 12 5 16 2 3 18 14 10 19 9 \n', '6 7 8 11 13 15 \n'],
             ['3 \n2 10 15 \n', '1 3 4 5 6 7 8 9 11 12 13 14 16 17 18 19 20 \n'],
             ['5 \n9 8 10 4 12 \n', '1 2 3 5 6 7 11 13 14 15 16 17 18 19 20 \n'],
             ['14 \n20 5 12 18 17 9 6 14 13 16 11 8 15 19 \n', '1 2 3 4 7 10 \n'],
             ['3 \n1 2 16 \n', '3 4 5 6 7 8 9 10 11 12 13 14 15 17 18 19 20 \n'],
             ['6 \n19 6 16 13 7 10 \n', '1 2 3 4 5 8 9 11 12 14 15 17 18 20 \n'],
             ['5 \n1 6 12 7 3 \n', '2 4 5 8 9 10 11 13 14 15 16 17 18 19 20 \n'],
             ['1 \n18 \n', '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 19 20 \n'],
             ['8 \n6 18 15 3 19 10 4 17 \n', '1 2 5 7 8 9 11 12 13 14 16 20 \n'],
             ['5 \n4 6 7 20 9 \n', '1 2 3 5 8 10 11 12 13 14 15 16 17 18 19 \n'],
             ['6 \n8 16 15 11 20 18 \n', '1 2 3 4 5 6 7 9 10 12 13 14 17 19 \n'],
             ['18 \n19 15 20 6 4 2 11 12 18 14 16 8 1 5 10 7 9 13 \n', '3 17 \n'],
             ['15 \n9 7 16 12 17 8 11 14 5 20 18 2 1 15 10 \n', '3 4 6 13 19 \n'],
             ['15 \n14 2 5 16 17 12 1 19 4 13 9 20 7 18 3 \n', '6 8 10 11 15 \n'],
             ['8 \n12 13 20 15 6 10 5 14 \n', '1 2 3 4 7 8 9 11 16 17 18 19 \n'],
             ['7 \n2 19 5 14 6 4 15 \n', '1 3 7 8 9 10 11 12 13 16 17 18 20 \n'],
             ['17 \n11 15 16 13 10 14 17 8 6 12 3 2 19 9 20 1 18 \n', '4 5 7 \n'],
             ['8 \n15 9 11 3 6 17 4 13 \n', '1 2 5 7 8 10 12 14 16 18 19 20 \n'],
             ['7 \n13 10 18 6 5 15 2 \n', '1 3 4 7 8 9 11 12 14 16 17 19 20 \n'],
             ['17 \n18 11 4 12 14 8 1 13 9 7 6 10 20 19 5 16 2 \n', '3 15 17 \n'],
             ['11 \n4 6 8 7 3 1 18 14 17 19 13 \n', '2 5 9 10 11 12 15 16 20 \n'],
             ['9 \n3 5 6 1 10 2 4 17 13 \n', '7 8 9 11 12 14 15 16 18 19 20 \n'],
             ['11 \n7 17 12 1 14 5 6 18 20 19 13 \n', '2 3 4 8 9 10 11 15 16 \n'],
             ['10 \n3 15 2 13 6 12 5 20 9 1 \n', '4 7 8 10 11 14 16 17 18 19 \n'],
             ['8 \n20 2 15 14 7 11 10 19 \n', '1 3 4 5 6 8 9 12 13 16 17 18 \n'],
             ['9 \n8 14 18 17 1 7 19 3 6 \n', '2 4 5 9 10 11 12 13 15 16 20 \n'],
             ['5 \n18 5 3 19 7 \n', '1 2 4 6 8 9 10 11 12 13 14 15 16 17 20 \n'],
             ['10 \n2 18 13 1 19 12 17 7 15 11 \n', '3 4 5 6 8 9 10 14 16 20 \n'],
             ['8 \n9 8 4 12 19 11 2 14 \n', '1 3 5 6 7 10 13 15 16 17 18 20 \n'],
             ['18 \n8 3 20 10 12 16 11 6 9 2 4 7 14 5 15 19 17 1 \n', '13 18 \n'],
             ['17 \n7 15 1 16 8 11 19 13 6 18 12 3 17 5 10 2 4 \n', '9 14 20 \n'],
             ['15 \n13 6 16 17 9 3 15 11 5 12 20 14 10 8 1 \n', '2 4 7 18 19 \n'],
             ['5 \n5 20 1 9 4 \n', '2 3 6 7 8 10 11 12 13 14 15 16 17 18 19 \n'],
             ['6 \n7 19 13 4 15 18 \n', '1 2 3 5 6 8 9 10 11 12 14 16 17 20 \n'],
             ['19 \n14 19 13 6 15 11 4 3 5 12 2 1 8 9 7 18 16 17 20 \n', '10 \n'],
             ['17 \n1 2 15 17 12 6 5 8 7 18 13 20 19 11 3 10 9 \n', '4 14 16 \n'],
             ['16 \n16 12 1 9 8 7 11 10 15 13 4 18 19 5 6 3 \n', '2 14 17 20 \n'],
             ['9 \n2 1 14 3 8 12 9 18 11 \n', '4 5 6 7 10 13 15 16 17 19 20 \n'],
             ['2 \n10 7 \n', '1 2 3 4 5 6 8 9 11 12 13 14 15 16 17 18 19 20 \n'],
             ['4 \n8 18 6 16 \n', '1 2 3 4 5 7 9 10 11 12 13 14 15 17 19 20 \n'],
             ['11 \n13 9 10 14 2 7 19 16 12 8 11 \n', '1 3 4 5 6 15 17 18 20 \n'],
             ['6 \n18 17 11 9 16 4 \n', '1 2 3 5 6 7 8 10 12 13 14 15 19 20 \n'],
             ['16 \n7 6 20 10 2 19 18 8 4 9 12 1 11 16 15 17 \n', '3 5 13 14 \n'],
             ['11 \n11 13 12 6 17 4 18 19 3 5 20 \n', '1 2 7 8 9 10 14 15 16 \n'],
             ['4 \n14 7 5 1 \n', '2 3 4 6 8 9 10 11 12 13 15 16 17 18 19 20 \n'],
             ['3 \n12 18 16 \n', '1 2 3 4 5 6 7 8 9 10 11 13 14 15 17 19 20 \n'],
             ['7 \n19 13 18 10 2 3 15 \n', '1 4 5 6 7 8 9 11 12 14 16 17 20 \n'],
             ['10 \n7 4 9 3 17 11 2 18 6 13 \n', '1 5 8 10 12 14 15 16 19 20 \n'],
             ['18 \n16 15 19 8 17 7 18 4 1 20 12 9 10 13 11 6 3 5 \n', '2 14 \n'],
             ['4 \n9 14 6 13 \n', '1 2 3 4 5 7 8 10 11 12 15 16 17 18 19 20 \n'],
             ['10 \n3 8 17 6 16 18 7 10 4 11 \n', '1 2 5 9 12 13 14 15 19 20 \n'],
             ['10 \n16 3 8 14 19 1 10 11 15 12 \n', '2 4 5 6 7 9 13 17 18 20 \n'],
             ['19 \n9 15 3 11 4 17 8 7 1 18 2 19 20 14 10 5 13 6 16 \n', '12 \n'],
             ['5 \n1 13 4 17 8 \n', '2 3 5 6 7 9 10 11 12 14 15 16 18 19 20 \n'],
             ['8 \n18 14 5 13 12 3 19 6 \n', '1 2 4 7 8 9 10 11 15 16 17 20 \n'],
             ['12 \n7 9 6 1 20 16 10 14 8 15 12 4 \n', '2 3 5 11 13 17 18 19 \n']]


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
                prob.test_cases = testcases
                # tag ekle
                for j in md.Meta['relate']:
                    tag = models.get_or_create(models.Tag, name=j)
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
