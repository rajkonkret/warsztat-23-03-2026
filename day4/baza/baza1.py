# baza danych - silnik baz danych
# sql
# mysql, postgres, mssql, oracle

import sqlite3

# docker
try:
    sql_connection = sqlite3.connect('sqlite_db.db')
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Bład podłączenia bazy danych")
finally:
    if sql_connection:
        sql_connection.close()
# Baza danych została podłączona
#
# Process finished with exit code 0