from abc import ABC ,abstractmethod

class Task(ABC):

    def __init__(self,name,status,priority):
        self.name=name
        self.status=status
        self.priority=priority

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def mark_complete(self):
        pass

    def get_priority(self):
        return self.priority
    
class MeetingTask(Task):

    def __init__(self,name,status,priority,attendees):
        super().__init__(name,status,priority)
        self.attendees=attendees

    def display(self):
        print(f"name:{self.name}|status:{self.status}|priority:{self.priority}|attendees:{self.attendees}")

    def mark_complete(self):
        self.status="completed"
        print(f"{self.name} is completed")

Task_1=MeetingTask("updates","completed","top",75)
Task_1.display()
Task_1.mark_complete()
print(Task_1.get_priority())