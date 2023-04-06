import pymysql,pygame,time,os

conn = pymysql.connect(host="localhost",user="root",password="111111",db="kongfc",charset="utf8")
cur = conn.cursor()
# sql = "select * from kongfc"
# cur.execute(sql)
# emps = cur.fetchall()
# print(emps)
# sql1 = 'insert into kongfc values (6,"诸葛瑾","吴国")'
# cur.execute(sql1)
# conn.commit()
# cur.close()
# conn.close()
pygame.mixer.init()
path = 'F:\音乐'
file = os.listdir(path)
count = 0
for f in file:
    ru = os.path.join(path,f)
    print(ru) #获取文件绝对路径
    if '.mp3' in ru:
        pygame.mixer.music.load(ru)
        pygame.mixer.music.play(-1)
        count += 1
        print(count)
        time.sleep(200)


