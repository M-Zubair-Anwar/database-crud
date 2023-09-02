import psycopg2
con=psycopg2.connect(
    user="admin",
    port="5432",
    password="admin",
    host="localhost",
    database="za")
cur=con.cursor()
# #1 create database
# # try:
# #     db="create database zamzam3"
# #     cur.execute(db)
# #     print("data is created")
# # except:
# #     print("some rror")
cur.execute("create table zamzam6(id INT PRIMARY KEY,floor VARCHAR(50),office_type VARCHAR(50),availability INT)" )
con.commit()
#
# # #1 create table
# cur.execute("create table zamzam4(id INT PRIMARY KEY ,floor VARCHAR(50),office VARCHAR(50),avail INT)")
# con.commit()
# # cur.close()
# # con.close()