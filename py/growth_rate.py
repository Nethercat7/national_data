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

#计算招生、在校、毕业人数增长率
def count_enrollment_rate():
    sum2017 = 0
    sum2016 = 0
    sum2015 = 0
    sum2014 = 0
    sum2013 = 0
    for i in collection_2017.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2017 += i['enrollment']
    for i in collection_2016.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2016 += i['enrollment']
    for i in collection_2015.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2015 += i['enrollment']
    for i in collection_2014.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2014 += i['enrollment']
    for i in collection_2013.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2013 += i['enrollment']
    data = {
        "rate2017": round((sum2017 - sum2016) / sum2016 * 100, 1),
        "rate2016": round((sum2016 - sum2015) / sum2015 * 100, 1),
        "rate2015": round((sum2015 - sum2014) / sum2014 * 100, 1),
        "rate2014": round((sum2014 - sum2013) / sum2013 * 100, 1)
    }
    return data
def count_students_rate():
    sum2017 = 0
    sum2016 = 0
    sum2015 = 0
    sum2014 = 0
    sum2013 = 0
    for i in collection_2017.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2017 += i['students']
    for i in collection_2016.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2016 += i['students']
    for i in collection_2015.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2015 += i['students']
    for i in collection_2014.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2014 += i['students']
    for i in collection_2013.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2013 += i['students']
    data = {
        "rate2017": round((sum2017 - sum2016) / sum2016 * 100, 1),
        "rate2016": round((sum2016 - sum2015) / sum2015 * 100, 1),
        "rate2015": round((sum2015 - sum2014) / sum2014 * 100, 1),
        "rate2014": round((sum2014 - sum2013) / sum2013 * 100, 1)
    }
    return data
def count_graduate_rate():
    sum2017 = 0
    sum2016 = 0
    sum2015 = 0
    sum2014 = 0
    sum2013 = 0
    for i in collection_2017.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2017 += i['graduate']
    for i in collection_2016.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2016 += i['graduate']
    for i in collection_2015.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2015 += i['graduate']
    for i in collection_2014.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2014 += i['graduate']
    for i in collection_2013.find({'$and': [{'quota': {'$ne': '学前教育'}}, {'quota': {'$ne': '特殊教育'}}, {'quota': {'$ne': '职业初中'}}]}):
        sum2013 += i['graduate']
    data = {
        "rate2017": round((sum2017 - sum2016) / sum2016 * 100, 1),
        "rate2016": round((sum2016 - sum2015) / sum2015 * 100, 1),
        "rate2015": round((sum2015 - sum2014) / sum2014 * 100, 1),
        "rate2014": round((sum2014 - sum2013) / sum2013 * 100, 1)
    }

    return data