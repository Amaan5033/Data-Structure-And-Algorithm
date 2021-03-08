# Given N number of activities with their start and end
# times.We need to select the maximum number of activites
# that can be performed by a single person,assuming that 
# a person can only work on a single activity at a time



class ActivitySelection:
    def __init__(self):
        self.activity=[]

    def add_activity(self,activity,startTime,FinishTime):
        self.activity.append((activity,startTime,FinishTime))

    def Activity(self,finishTime):
        self.activity.sort(key=lambda x:x[2])##???Read below the code
        first_activity=self.activity[0]
        for i in range(1,len(self.activity)):
            if self.activity[i][1]>finishTime:
                break
            else:
                if self.activity[i][1]>=self.activity[i-1][2]:
                    print(self.activity[i][0])


AS=ActivitySelection()
AS.add_activity("A1",0,6)
AS.add_activity("A2",3,4)
AS.add_activity("A3",1,2)
AS.add_activity("A4",5,8)
AS.add_activity("A5",5,7)
AS.add_activity("A6",8,9)

AS.Activity(10)



"""
sort doesnt return the sorted list; rather than
it sort the list in place.
Python habitually  returns None from functions
and methods that mutate the data such as list.sort,
list.append and random.shuffle with the idea being 
that it hints to the fact that it was mutating.
"""