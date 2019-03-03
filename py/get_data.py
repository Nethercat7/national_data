import pymongo
from py import spider,growth_rate,graduate_and_enrollment,students_in_population

#连接mongodb，创建数据库和集合。
client=pymongo.MongoClient('localhost:27017')
db=client['national_data']
#各年份的学生信息集合
collection_2017=db['data2017']
collection_2016=db['data2016']
collection_2015=db['data2015']
collection_2014=db['data2014']
collection_2013=db['data2013']
#各年份的总人口集合
collection_population=db['population']
#招生、在校、毕业增长率集合
collection_enrollment_rate=db['enrollment_rate']
collection_students_rate=db['students_rate']
collection_graduate_rate=db['graduate_rate']
#各年份的毕业生和招生数集合
collection_gae2017=db['gae2017']
collection_gae2016=db['gae2016']
collection_gae2015=db['gae2015']
collection_gae2014=db['gae2014']
collection_gae2013=db['gae2013']
#各年份的总人口中的在校生占比集合
collection_sip2017=db['sip2017']
collection_sip2016=db['sip2016']
collection_sip2015=db['sip2015']
collection_sip2014=db['sip2014']
collection_sip2013=db['sip2013']

#插入数据
def insert():
    try:
        #各年份的学生数据
        if not collection_2017.find().count():
            collection_2017.insert_many(spider.data2017())
        if not collection_2016.find().count():
            collection_2016.insert_many(spider.data2016())
        if not collection_2015.find().count():
            collection_2015.insert_many(spider.data2015())
        if not collection_2014.find().count():
            collection_2014.insert_many(spider.data2014())
        if not collection_2013.find().count():
            collection_2013.insert_many(spider.data2013())
        #各年份的总人口数量
        if not collection_population.find().count():
            collection_population.insert_many(spider.population())
        else:
            pass
    except Exception as e:
        return e
    finally:
        #招生、在校、毕业人数增长率
        if not collection_enrollment_rate.find().count():
            collection_enrollment_rate.insert_one(growth_rate.count_enrollment_rate())
        if not collection_students_rate.find().count():
            collection_students_rate.insert_one(growth_rate.count_students_rate())
        if not collection_graduate_rate.find().count():
            collection_graduate_rate.insert_one(growth_rate.count_graduate_rate())
        #各年份的高中职毕业生数和专本科招生数
        if not collection_gae2017.find().count():
            collection_gae2017.insert_one(graduate_and_enrollment.gae2017())
        if not collection_gae2016.find().count():
            collection_gae2016.insert_one(graduate_and_enrollment.gae2016())
        if not collection_gae2015.find().count():
            collection_gae2015.insert_one(graduate_and_enrollment.gae2015())
        if not collection_gae2014.find().count():
            collection_gae2014.insert_one(graduate_and_enrollment.gae2014())
        if not collection_gae2013.find().count():
            collection_gae2013.insert_one(graduate_and_enrollment.gae2013())
        #各年份的总人口中的在校生占比
        if not collection_sip2017.find().count():
            collection_sip2017.insert_one(students_in_population.students2017())
        if not collection_sip2016.find().count():
            collection_sip2016.insert_one(students_in_population.students2016())
        if not collection_sip2015.find().count():
            collection_sip2015.insert_one(students_in_population.students2015())
        if not collection_sip2014.find().count():
            collection_sip2014.insert_one(students_in_population.students2014())
        if not collection_sip2013.find().count():
            collection_sip2013.insert_one(students_in_population.students2013())
        else:
            pass