# -*- coding: utf-8 -*-

import codecs
import os
from app import db
from app import models
import markdown
#bütün problemler
problems = os.listdir('.')
#markdown meta eklentili
md = markdown.Markdown(extensions=['meta'])
def import_db():
    for i in problems:
        # dosya adında nokta varsa atla
        if "." in i:
            continue
        #metadatyı oku
        input_file = codecs.open(os.path.join(i, 'meta'), mode="r", encoding="utf-8-sig")
        text = input_file.read()
        #metadatyı işle
        html = md.convert(text)
        #soruyu oku
        input_file = codecs.open(os.path.join(i, 'question.md'), mode="r", encoding="utf-8-sig")
        text = input_file.read()
        #çözümü oku
        input_file = codecs.open(os.path.join(i, 'solution.md'), mode="r", encoding="utf-8-sig")
        text2 = input_file.read()
        #sql nesnesini yarat ve database ekle
        db.session.add(
            models.Problems(title=md.Meta['title'][0], author=md.Meta['author'][0], body=text, solution=text2, count=0
                            ))
    #database değişikliklerini kaydet
    db.session.commit()


if __name__ == "__main__":
    import_db()