class Task:
    def __init__(self,name,status,priority):
        self.name=name
        self.status=status
        self.priority=priority

    def display(self):
        print(f"Task(name:{self.name}|status:{self.status}|priority:{self.priority})")
    
    def mark_complete(self):
        self.status="completed"
        print(f"{self.name} task is completed")

class BugTask(Task):
    def __init__(self,name,status,priority,severity):
        super().__init__(name,status,priority)
        self.severity=severity
    
    def display(self):
        super().display()  # call Task's display first
        print(f"Severity: {self.severity}")

class FeatureTask(Task):
    def __init__(self,name,status,priority,deadline):
        super().__init__(name,status,priority)
        self.deadline=deadline
    
    def display(self):
        super().display()  # call Task's display first
        print(f"deadline: {self.deadline}")

task1=BugTask("python","inprogress","Medium","high")
task2=FeatureTask("fastapi","inprogress","Medium","9-10-2026")
task1.mark_complete()
task1.display()
task2.mark_complete()
task2.display()
print(task2.deadline)