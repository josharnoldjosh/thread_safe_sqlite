---

A DSL wrapper & threadsafe sqlite implementation.

---

## Install

Its as easy as:

`pip3 install db-by-josh`

## Usage

First, let's import some modules.

```python
from db_by_josh.schema import Database
from db_by_josh.schema import Schema, Table, Column
from db_by_josh.query import Query
```

### Creating a schema

Instead of worrying about doing `CREATE TABLE`, etc, why not just create a schema object? A schema refers to a single database `.sqlite` file.

```python
db_schema = Schema("my_database")
```

### Adding a table

Now, let's add a table to our schema. Let's create a `User` table with two columns:

```python
users = Table("User")
users.add_column("username", Column.TEXT)
users.add_column("password", Column.TEXT)
db_schema.add_table(users) # Don't forget to add your table to your schema
```

### Getting a reference to your a Database

It's as easy as:

```python
db = Database(db_schema)
```

### What about adding data?

Just call `insert_into` and pass in your table name followed by named arguments (`**kwargs`).

```python
db.insert_into("User", 
    username="Josh", password="1234")
```

### Queries, Queries, Queries.

Queries in SQL are now fun.

First, you're going to want to define a query using this chain-notation.

```python
q = Query().select("User").where("username").equals("Josh")
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

### A Few More Example Queries

Updating a value in your database.

```python
# Update a user's password where username = "Josh"
q = Query().update("User").set("password").equals("new password value").where("username").equals("Josh")
```

Deleting a row in your database.

```python
# Delete a user who's username = "Josh"
q = Query().delete("User").where("username").equals("Josh")
```

