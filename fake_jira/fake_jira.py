import queue

class Jira():
    def __init__(self):
        self.task_list = queue.PriorityQueue()
        self.task_list.put((2, "payment prosses bug"))
        self.task_list.put((1, "Server down"))
        self.task_list.put((1, "Database mess"))
        self.task_list.put((3, "background color"))
    
    def create_task(self, priorty, task_detail):
        self.task_list.put((int(priorty), task_detail))
        
    def get_all_tasks(self):
        temp_list = []
        while not self.task_list.empty():
            item = self.task_list.get()
            temp_list.append(item)
        
        for item in temp_list:
            self.task_list.put(item)
            
        return temp_list
    
    def get_mandatory_task(self):
        temp_list = []
        while not self.task_list.empty():
            item = self.task_list.get()
            temp_list.append(item)
        
        priority_1_tasks = [task for priority, task in temp_list if priority == 1]
        
        # Rebuild the queue
        for item in temp_list:
            self.task_list.put(item)
            
        return priority_1_tasks   
    
    def remove_task(self, priorty, task_detail):
        temp_list = []
        task_to_remove = (priorty, task_detail)
        # Extract tasks and filter out the one to remove
        
        while not self.task_list.empty():
            item = self.task_list.get()
            if item != task_to_remove:  # Keep only tasks that are NOT the one to remove
                temp_list.append(item)

        # Rebuild the queue
        for item in temp_list:
            self.task_list.put(item)

        return temp_list

j = Jira()
task_desc = input('pls write task desc : ')
priorty =  input('pls write task priorty : ')
j.create_task(priorty, task_desc)
print(j.get_mandatory_task())
print(j.get_all_tasks())
print(j.remove_task(1, "Database mess"))
