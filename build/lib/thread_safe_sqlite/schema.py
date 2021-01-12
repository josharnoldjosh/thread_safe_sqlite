from enum import Enum, auto


class Column(Enum):
    TEXT=auto()    
    INTEGER=auto()        
    NUMERIC=auto()
    

class Table:

    def __init__(self, name):
        self.name = name
        self.columns = {}
        self.keys = []

    def add_column(self, name, type):
        if name in self.columns:
            raise RuntimeWarning(f"Column, {name}, already exists in your table!")
        self.columns[name] = type.name
        self.keys.append(name)


class Schema:

    def __init__(self, name):
        if "." in name:
            raise RuntimeWarning(
                f"You shouldn't have a period, a.k.a, '.', in your Schema name: {name}"
            )
        self.name = name
        self.tables = {}

    def add_table(self, table):
        if table.name in self.tables:
            raise RuntimeWarning(f"Table, {table.name}, already exists in your schema!")
        self.tables[table.name] = table