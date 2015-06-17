# -*- coding: utf-8 -*-

import codecs
import os
import errno
from app import db
from app import models
from app.config import Config
from shutil import copy
import markdown
# bütün problemler
problems = os.listdir(os.path.dirname(__file__))
# flask basedir
basedir = Config.basedir
static_resources_dir =os.path.join(basedir, 'static','resources')
# markdown meta eklentili
md = markdown.Markdown(extensions=['meta'])

def import_db():
    for i in problems:
        # dosya adında nokta varsa atla
        if "." in i:
            continue
        # metadatyı oku
        input_file = codecs.open(os.path.join(i, 'meta'), mode="r", encoding="utf-8-sig")
        text = input_file.read()
        # metadatyı işle
        html = md.convert(text)
        # soruyu oku
        input_file = codecs.open(os.path.join(i, 'question.md'), mode="r", encoding="utf-8-sig")
        text = input_file.read()
        # çözümü oku
        input_file = codecs.open(os.path.join(i, 'solution.md'), mode="r", encoding="utf-8-sig")
        text2 = input_file.read()
        if models.Problems.query.filter_by(title=md.Meta['title'][0]).first() is None:
            # sql nesnesini yarat ve database ekle
            db.session.add(
                models.Problems(title=md.Meta['title'][0], author=md.Meta['author'][0], body=text, solution=text2,
                                count=0
                                ))
        # eğer resources verildiyse kopyala copy
        if os.path.isdir(os.path.join(i,'resources')):
            resdir=os.path.join(i,'resources')
            res = os.listdir(resdir)
            dest_res =os.path.join(static_resources_dir,i)
            # hedef klasör yoksa yarat
            make_sure_path_exists(dest_res)
            # bütün resourceleri kopyala i/resources to resources/i
            for j in res:
                copy(os.path.join(resdir,j),os.path.join(dest_res,j))

    # database değişikliklerini kaydet
    db.session.commit()

# klasör yaratma çalış varsa boşver ama başka hata çıkarsa bildir
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


if __name__ == "__main__":
    import_db()
