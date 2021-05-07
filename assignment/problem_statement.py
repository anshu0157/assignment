import json

class student:
    def __init__(self,marks):
        self.marks = marks
    def getStudentsWithMarksMoreThan(self):
        with open('data.json') as json_file:
            dict = json.load(json_file)
        dict1={}
        l=[]
        for key,value in dict.items():
            for x in range(len(value)):
                details=value[x].get('details')
                if details.get('marks')>self.marks:
                    l.append(value[x])
                    dict1.update({key:l})
       
        # converts it into json   
        jsd=json.dumps(dict)
        print(jsd)
                    
            
            
marks=student(31)
marks.getStudentsWithMarksMoreThan()
