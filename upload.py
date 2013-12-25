# -*- coding: cp936 -*-
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

API_KEY = 'YOUR-API_KEY'
API_SECRET = 'YOUR-API_SECRET'

from facepp import API,File
api = API(API_KEY, API_SECRET)

                                        
result = api.detection.detect(img = File(r'F:\AI\TestPhoto\111180.jpg'), mode = 'oneface')
print_result('Detection result for {}:'.format('blue'), result)
face_id=result['face'][0]['face_id']
api.person.create(person_name = u'Name',
                  face_id = face_id,tag=u'自定义标签',
                  group_name = u'群组名称)

result = api.recognition.train(group_name = u'Ⱥ��', type = 'all')

print_result('Train result:', result)

session_id = result['session_id']
while True:
    result = api.info.get_session(session_id = session_id)
    if result['status'] == u'SUCC':
        print_result('Async train result:', result)
        break
    time.sleep(1)
