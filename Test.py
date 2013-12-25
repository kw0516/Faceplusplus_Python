# -*- coding: cp936 -*-
#App应用标识
API_KEY = 'YOUR-API_KEY'
API_SECRET = 'YOUR-API_SECRET'

# 导入系统库并定义辅助函数
import time
from pprint import pformat
def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])


# 导入SDK中的API类
from facepp import API,File
api = API(API_KEY, API_SECRET)

# 识别未知脸部图片
result = api.recognition.recognize(img = File(r'F:\AI\TestPhoto\550.jpg'),
                                   group_name = '群组')
print_result('Recognize result:', result)
print '=' * 60
print 'The person with highest confidence:', \
        result['face'][0]['candidate'][0]['person_name'],\
        result['face'][0]['candidate'][0]['tag']



    

