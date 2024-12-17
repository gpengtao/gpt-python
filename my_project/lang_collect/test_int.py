#!/usr/bin/python

"""
python不支持 ++i，更不支持 i++ 语法错误
"""

i = 0
print(++i)
print(++i)
print(++i)

i = i + 1
print(i)


str = """
{"abnormalName":"\u51b7\u85cf\u5546\u54c1\u653e\u7f6e\u5728\u5e38\u6e29\u6574\u6539","originBizId":"3890173950146239","workName":"\u51b7\u85cf\u5546\u54c1\u653e\u7f6e\u5728\u5e38\u6e29\u6574\u6539","interveneType":"AI_STORE_CS","intelligenceOrderId":3890174043732678,"flowOrderId":2110174044414259}	
"""
print(str);