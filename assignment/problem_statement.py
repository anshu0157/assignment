import json

class student:
    def __init__(self,marks):
        self.marks = marks
    def getStudentsWithMarksMoreThan(self):
        with open('data.json') as json_file:
            dict = json.load(json_file)
        print(dict)
        print('\n')
        dict1={}
        l=[]
        for key,value in dict.items():
            # print(key,value)
            for x in range(len(value)):
                details=value[x].get('details')
                if details.get('marks')>self.marks:
                    l.append(value[x])
                    dict1.update({key:l})
        jsd=json.dumps(dict)
        print(jsd)
                    
            
            
marks=student(31)
marks.getStudentsWithMarksMoreThan()
