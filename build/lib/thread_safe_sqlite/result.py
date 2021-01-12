


class Row:

    def __init__(self, data):
        self.__dict__ = data

    def __str__(self) -> str:
        return str(self.__dict__)

class Result(list):

    def __init__(self, table, data):                      
        self.extend([Row(dict(list(zip(table.keys, d)))) for d in data])    
         