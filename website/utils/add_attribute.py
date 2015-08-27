from __future__ import absolute_import
from __future__ import unicode_literals
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension


class AddAttributeTreeprocessor(Treeprocessor):
    """ get tag and add class """

    def run(self, root):
        tags = root.getiterator("table")
        for tag in tags:
            tag.set("class", self.config["table"])


class AddAttributeExtension(Extension):
    """ Extension """

    def __init__(self, *args, **kwargs):
        self.config = {
            'table': ["table",
                      "table class attr"],
        }
        super(AddAttributeExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        add_attributes = AddAttributeTreeprocessor(md)
        add_attributes.config = self.getConfigs()
        md.treeprocessors.add("add_attributes", add_attributes, "_end")

        md.registerExtension(self)


def makeExtension(*args, **kwargs):
    return AddAttributeExtension(*args, **kwargs)
