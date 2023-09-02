import psycopg2
conn=psycopg2.connect(
    user="admin",
    port="5432",
    password="admin",
    host="localhost",
    database="za"
)
cur=conn.cursor()

# creating table
# cur.execute("create table zamzam6(id INT PRIMARY KEY,floor VARCHAR(50),office_type VARCHAR(50),availabi INT)")
# conn.commit()

# # 2nd of creating of table
# tab="create table zamzam7(id7 int primary key,floor varchar(50),office varchar(50) )"
# cur.execute(tab)
# conn.commit()

# # insert the value
# cur.execute("insert into zamzam6(id,floor,office_type,availabi)values(3,'ground','shop',5),(4,'mezzninie','s.shop',10)")
# conn.commit()

# #2 insert the value
# ins="insert into zamzam7(id7,floor,office)values(1,'ground','5')"
# cur.execute(ins)
# conn.commit()

# # 3rd way
# ins="insert into zamzam7(id7,floor,office)values(%s,%s,%s)"
# t=('3','mezzanine','10')
# cur.execute(ins,t)
# conn.commit()

# # 4th way
# ins="insert into zamzam7(id7,floor,office)values(%s,%s,%s)"
# t=[('3','mezzanine','10'),('4','1st','12')]
# cur.executemany(ins,t)
# conn.commit()


 # # # displying data
# cur.execute('select * from zamzam6')
# result=cur.fetchall()
# for i in result:
#      id=i[0]
#      floor=i[1]
#      office_type=i[2]
#      availabi=i[3]
#      print(id,floor,office_type,availabi)

# #  # 2nd way
# cur.execute('select * from zamzam7')
# rows=cur.fetchall()
# for row in rows:
#     print(row)

# #3rd way
# print("{:<15} {:<20} {:<20}".format("id","floor","office"))
# s="select * from zamzam7"
# cur.execute(s)
# rows=cur.fetchall()
# for r in rows:
#     print("{:<15} {:<20} {:<20}".format(r[0],r[1],r[2]))


# # update the zamzam6
# cur.execute("update zamzam6 set floor='ground_change',availabi=505 where id=3")
# conn.commit()

# # 2nd way
# up="update zamzam7 set floor=%s,office=%s where id7=%s"
# data=('ground_change','505',1)
# cur.execute(up,data)
# conn.commit()

# delete
# cur.execute("delete from zamzam6 where id=2")
# conn.commit()

