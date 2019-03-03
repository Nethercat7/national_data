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

#计算各年份的高中职毕业生数和专本科招生数
def gae2017():
    high_school = 0  # 高中和中职
    university = 0  # 专科和本科
    for h_graduate, v_graduate, b_enrollment, c_enrollment in zip(collection_2017.find({'quota': '普通高中'}),collection_2017.find({'quota': '中等职业教育'}),collection_2017.find({'quota': '普通本专科'}),collection_2017.find({'quota': '专科'})):
        high_school = (h_graduate['graduate'] + v_graduate['graduate'])
        university = (b_enrollment['enrollment'] + c_enrollment['enrollment'])
    graduate_and_enrollment_compare = {
        'graduate': round(high_school / 10000),
        'enrollment': round(university / 10000)
    }
    return graduate_and_enrollment_compare
def gae2016():
    high_school = 0  # 高中和中职
    university = 0  # 专科和本科
    for h_graduate, v_graduate, b_enrollment, c_enrollment in zip(collection_2016.find({'quota': '普通高中'}),collection_2016.find({'quota': '中等职业教育'}),collection_2016.find({'quota': '普通本专科'}), collection_2016.find({'quota': '专科'})):
        high_school = (h_graduate['graduate'] + v_graduate['graduate'])
        university = (b_enrollment['enrollment'] + c_enrollment['enrollment'])
    graduate_and_enrollment_compare = {
        'graduate': round(high_school / 10000),
        'enrollment': round(university / 10000)
    }
    return graduate_and_enrollment_compare
def gae2015():
    high_school = 0  # 高中和中职
    university = 0  # 专科和本科
    for h_graduate, v_graduate, b_enrollment, c_enrollment in zip(collection_2015.find({'quota': '普通高中'}),collection_2015.find({'quota': '中等职业教育'}),collection_2015.find({'quota': '普通本专科'}),collection_2015.find({'quota': '专科'})):
        high_school = (h_graduate['graduate'] + v_graduate['graduate'])
        university = (b_enrollment['enrollment'] + c_enrollment['enrollment'])
    graduate_and_enrollment_compare = {
        'graduate': round(high_school / 10000),
        'enrollment': round(university / 10000)
    }
    return graduate_and_enrollment_compare
def gae2014():
    high_school = 0  # 高中和中职
    university = 0  # 专科和本科
    for h_graduate, v_graduate, b_enrollment, c_enrollment in zip(collection_2014.find({'quota': '普通高中'}), collection_2014.find({'quota': '中等职业教育'}),collection_2014.find({'quota': '普通本专科'}),collection_2014.find({'quota': '专科'})):
        high_school = (h_graduate['graduate'] + v_graduate['graduate'])
        university = (b_enrollment['enrollment'] + c_enrollment['enrollment'])
    graduate_and_enrollment_compare = {
        'graduate': round(high_school / 10000),
        'enrollment': round(university / 10000)
    }
    return graduate_and_enrollment_compare
def gae2013():
    high_school = 0  # 高中和中职
    university = 0  # 专科和本科
    for h_graduate, v_graduate, b_enrollment, c_enrollment in zip(collection_2013.find({'quota': '普通高中'}),collection_2013.find({'quota': '中等职业教育'}),collection_2013.find({'quota': '普通本专科'}),collection_2013.find({'quota': '专科'})):
        high_school = (h_graduate['graduate'] + v_graduate['graduate'])
        university = (b_enrollment['enrollment'] + c_enrollment['enrollment'])
    graduate_and_enrollment_compare = {
        'graduate': round(high_school / 10000),
        'enrollment': round(university / 10000)
    }
    return graduate_and_enrollment_compare