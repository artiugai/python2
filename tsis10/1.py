import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    port = 5432,
    user = "postgres",
    password = "artemjkee"
)
sql = "select * from MyContacts where lastname = 'Shelby'"
cursor = conn.cursor()
cursor.execute(sql)
MyContacts = cursor.fetchall()
print(MyContacts)