'''
Created on 16/03/2016

@author: bruno.martins
'''
class Properties:
    
    properties = Properties()
    props = {"language": "Python", "version":3}
    
    @classmethod
    def instance(cls):
        if(cls.properties == None):
            properties = Properties()
        return properties

p = Properties.instance()
x = Properties.instance()
print(p==x)
        