__author__ = 'deniz'


class Table():
    """store html tables with sortable header"""

    def __init__(self, sortable, column, content):
        """
        Constructor.
        :param sortable:
        :param column:
        :param content:
        """
        self.sortable = sortable
        self.column = column
        self.content = content
