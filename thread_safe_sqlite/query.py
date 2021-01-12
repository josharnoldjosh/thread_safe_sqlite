

def parse_value(value):
    if isinstance(value, str): value = f"'{value}'"
    if isinstance(value, bool): value = int(value)
    return value


class Query:

    def __init__(self):
        self.result = ""
        self.table_name = ""

    def select(self, table_name):
        self.table_name = table_name
        self.result += f"SELECT * from {table_name} "
        return self

    def update(self, table_name):
        self.table_name = table_name
        self.result += f"UPDATE {table_name} "
        return self

    def set(self, key):
        self.result += f"SET {key} "
        return self

    def delete(self, table_name):
        self.table_name = table_name
        self.result += f"DELETE from {table_name} "
        return self

    def where(self, column_name):
        if "WHERE" in self.result:
            self.result += f"AND {column_name} "
        else:    
            self.result += f"WHERE {column_name} "
        return self

    def equals(self, value):        
        self.result += f"= {parse_value(value)} "
        return self

    def greater_than(self, value):
        self.result += f"> {parse_value(value)} "
        return self
      
    def greater_or_equal(self, value):
        self.result += f">= {parse_value(value)} "
        return self

    def less_than(self, value):
        self.result += f"< {parse_value(value)} "
        return self
      
    def lesser_or_equal(self, value):
        self.result += f"<= {parse_value(value)} "
        return self