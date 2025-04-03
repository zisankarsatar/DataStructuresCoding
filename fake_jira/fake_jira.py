import queue

class Jira():
    def __init__(self):
        self.task_list = queue.PriorityQueue()
        self.task_list.put((2, "payment prosses bug"))
        self.task_list.put((1, "Server down"))
        self.task_list.put((1, "Database mess"))
        self.task_list.put((3, "background color"))
    
    def create_task(self, priorty, task_detail):
        self.task_list.put((priorty, task_detail))
        
    def get_all_tasks(self):
        temp_list = []
        while not self.task_list.empty():
            item = self.task_list.get()
            temp_list.append(item)
            
        return temp_list   
    
    def get_mandatory_task(self):
        temp_list = []
        while not self.task_list.empty():
            item = self.task_list.get()
            temp_list.append(item)
        
        priority_1_tasks = [task for priority, task in temp_list if priority == 1]
        return priority_1_tasks   

j = Jira()
#j.create_task()
print(j.get_mandatory_task())
