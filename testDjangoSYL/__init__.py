import  pymysql
pymysql.install_as_MySQLdb()


db=pymysql.connect("localhost","root","password","autoSmoke")

cursor1 = db.cursor()
cursor1.execute("SELECT VERSION()")
data = cursor1.fetchone()#将一条结果放入data
# data = cursor1.fetchmany(3)#将3条数据放入data
print("Database version: %s" % data)

cursor = db.cursor()
sql = "SELECT * FROM book"
cursor.execute(sql)
rr = cursor.fetchall()
print(cursor.rowcount)
for row in rr:
    print("id是：%s,名字是：%s,作者是：%s,出版社是：%s,出版时间是：%s,出版哈哈哈是：%s"%row)

db.close()
cursor.close()