from sqlite3worker import Sqlite3Worker
from result import Result


class Database:
    """
    A thread safe sqlite3 database.
    """

    @property
    def path(self):
        """The path to the database file."""
        return self.directory+self.schema.name+".sqlite"

    def __init__(self, schema, directory="./", log_errors = False, verbose = False):        
        """Inits the database, creating a table if needed."""                
        self.schema = schema         
        if len(directory) > 0 and directory[-1] != '/': directory += '/'
        self.directory = directory
        self.log_errors = log_errors
        self.verbose = verbose
        self.db = Sqlite3Worker(self.path, log_errors=log_errors)
        self.create_tables_if_needed()

    def create_tables_if_needed(self):
        for table in self.schema.tables.values():
            try:
                columns = ", ".join([f"{key} {val}" for key, val in table.columns.items()])   
                command = f"CREATE TABLE {table.name} ({columns})"
                self.db.execute(command)            
                if self.verbose:    
                    print(f"Created '{table.name}'' with columns ({columns})")
            except Exception as e:
                if self.verbose:
                    print(e)

    def insert_into(self, table_name, **kwargs):
        """Inserts kwargs into a table."""
        if table_name not in self.schema.tables.keys():
            raise RuntimeError(f"Could not find the table, {table_name}, in database, {self.schema.name}")
        keys, values = zip(*kwargs.items())
        keys = ', '.join(keys)
        values = ', '.join(["'"+i+"'" if isinstance(i, str) else str(i) for i in values]).replace("True", "1").replace("False", "0")
        self.db.execute(f"INSERT into {table_name} ({keys}) values ({values})")

    def query(self, query):
        """Performs a given query."""
        try:
            table = self.schema.tables[query.table_name]
            data = self.db.execute(query.result)                        
            return Result(table, data)
        except Exception as e:
            if self.verbose:
                print(e)
        return []