import  sqlite3

con=sqlite3.connect("test.db")  #


cusor=con.cursor()   #获取游标
sql='''
        create table movie250
        (id int primary key not null,
        name text not null,
        price char(50),
        info char(50));
        


'''

cusor.execute(sql)  #执行语句


#提交
con.commit()
#关闭
con.close()

print('finish')


print("crate db success")