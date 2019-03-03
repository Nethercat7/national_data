import pymongo

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

#计算各年份的总人口中的在校生占比
def students2017():
    students_sum=0
    population=0
    for students in collection_2017.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        students_sum+=students['students']
    for peope in collection_population.find():
        population=peope['year2017']
    data={
        'students':round(students_sum/10000),
        'peope':population
    }
    return data
def students2016():
    students_sum=0
    population=0
    for students in collection_2016.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        students_sum+=students['students']
    for peope in collection_population.find():
        population=peope['year2016']
    data={
        'students':round(students_sum/10000),
        'peope':population
    }
    return data
def students2015():
    students_sum=0
    population=0
    for students in collection_2015.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        students_sum+=students['students']
    for peope in collection_population.find():
        population=peope['year2015']
    data={
        'students':round(students_sum/10000),
        'peope':population
    }
    return data
def students2014():
    students_sum=0
    population=0
    for students in collection_2017.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        students_sum+=students['students']
    for peope in collection_population.find():
        population=peope['year2014']
    data={
        'students':round(students_sum/10000),
        'peope':population
    }
    return data
def students2013():
    students_sum=0
    population=0
    for students in collection_2013.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        students_sum+=students['students']
    for peope in collection_population.find():
        population=peope['year2013']
    data={
        'students':round(students_sum/10000),
        'peope':population
    }
    return data