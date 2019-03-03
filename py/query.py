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
#各年份的总人口总在校生占比
collection_sip2017=db['sip2017']
collection_sip2016=db['sip2016']
collection_sip2015=db['sip2015']
collection_sip2014=db['sip2014']
collection_sip2013=db['sip2013']

#查询各年份学生信息
def data2017():
    results=collection_2017.find({'$and':[{'quota':{'$ne':'学前教育'}},{'quota':{'$ne':'特殊教育'}},{'quota':{'$ne':'职业初中'}}]},{'_id':0})
    return results
def data2016():
    results=collection_2016.find({'$and':[{'quota':{'$ne':'学前教育'}},{'quota':{'$ne':'特殊教育'}},{'quota':{'$ne':'职业初中'}}]},{'_id':0})
    return results
def data2015():
    results=collection_2015.find({'$and':[{'quota':{'$ne':'学前教育'}},{'quota':{'$ne':'特殊教育'}},{'quota':{'$ne':'职业初中'}}]},{'_id':0})
    return results
def data2014():
    results=collection_2014.find({'$and':[{'quota':{'$ne':'学前教育'}},{'quota':{'$ne':'特殊教育'}},{'quota':{'$ne':'职业初中'}}]},{'_id':0})
    return results
def data2013():
    results=collection_2013.find({'$and':[{'quota':{'$ne':'学前教育'}},{'quota':{'$ne':'特殊教育'}},{'quota':{'$ne':'职业初中'}}]},{'_id':0})
    return results

#查询招生、在校、毕业人数增长率
def enrollment_rate():
    results=collection_enrollment_rate.find({},{'_id':0})
    return results
def students_rate():
    results=collection_students_rate.find({},{'_id':0})
    return results
def graduate_rate():
    results=collection_graduate_rate.find({},{'_id':0})
    return results

#查询2017年到2013年的高中职毕业生数和专本科招生数
def gae2017():
    results=collection_gae2017.find({},{'_id':0})
    return results
def gae2016():
    results=collection_gae2016.find({},{'_id':0})
    return results
def gae2015():
    results=collection_gae2015.find({},{'_id':0})
    return results
def gae2014():
    results=collection_gae2014.find({},{'_id':0})
    return results
def gae2013():
    results=collection_gae2013.find({},{'_id':0})
    return results

#查询总人口
def population():
    results=collection_population.find({},{'_id':0})
    return results

#查询2017年到2013年的总人口总在校生占比
def sip2017():
    results=collection_sip2017.find({},{'_id':0})
    return results
def sip2016():
    results=collection_sip2016.find({},{'_id':0})
    return results
def sip2015():
    results=collection_sip2015.find({},{'_id':0})
    return results
def sip2014():
    results=collection_sip2014.find({},{'_id':0})
    return results
def sip2013():
    results=collection_sip2013.find({},{'_id':0})
    return results