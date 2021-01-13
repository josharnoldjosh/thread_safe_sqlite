A DSL wrapper & threadsafe sqlite implementation.

---

If you ever need a light-weight database wrapper for python that's also thread-safe, look no further.

---

## Install

Its as easy as:

`pip3 install db-by-josh`

## Usage

First, lets import some modules.

```python
from db_by_josh import (
    schema,
    store,    
    query,
    result,    
)
```

### Creating a schema

Instead of worrying doing `CREATE TABLE`, etc, why not create a schema object?

```python
db_schema = schema.Schema("my_database")
```

### Adding a table

Now, let's add a table to our schema. Let's create a `User` table with two columns:

```python
users = schema.Table("User")
users.add_column("username", schema.Column.TEXT)
users.add_column("password", schema.Column.TEXT)
db_schema.add_table(users) # Don't forget to add your table to your schema
```

### Getting a reference to your a Database

It's as easy as:

```python
db = store.Database(db_schema)
```

### What about adding data?

Just call `insert_into` and pass in your table name followed by named arguments (`**kwargs`).

```python
db.insert_into("User", 
    username="Josh", password="1234")
```

### Queries, Queries, Queries.

Queries are in SQL are now fun.

First, you're going to want to define a query using this chain-notation.

```python
q = query.Query().select("User").where("username").equals("Josh")
```

Just call `.query` on your database reference and pass in your previously defined query, and voila, results!

```python
results = db.query(q)
```

Results are just a list of python dictionaries (wrapped in a light-weight class). 

```python
# Print results
for row in results:
    print(row) # print the dict
    print(row.username) # or access a value
```

You now have the basics!


### Non-supported Queries?

If the framework doesn't support your required logic, just call `.db.execute` on your database reference.

```python
result = my_database_reference.db.excecute("<MY SQL QUERY HERE>")
```


