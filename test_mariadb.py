import mariadb

print("mariadb.__version__")
connection = mariadb.connect(
    host = "localhost",
    user = "root",
    passwd = "5413",
    database = "test_db",
    port = 3306,

)
print('Connection established successfully')