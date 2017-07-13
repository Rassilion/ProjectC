__author__ = 'deniz'


class Table:
    """store html tables with sortable header"""

    def __init__(self, sortable, column, content):
        """
        Constructor.
        :param sortable:
        sortable header dict
        :param column:
        :param content:
        pagination object
        """
        self.sortable = sortable
        self.column = column
        self.content = content
