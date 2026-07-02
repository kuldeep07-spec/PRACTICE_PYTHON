# ============================================
# Lesson 6 - Abstract Classes
# ============================================

from abc import ABC, abstractmethod  # ABC = Abstract Base Class, abstractmethod = forces child to implement

# Abstract class — cannot be created directly
# Acts as a blueprint/contract for all child classes
class Task(ABC):

    def __init__(self, name, status, priority):
        self.name = name          # task name
        self.status = status      # task status
        self.priority = priority  # task priority

    @abstractmethod
    def display(self):
        # Child MUST implement this — no choice!
        # If child doesn't implement → TypeError on object creation
        pass

    @abstractmethod
    def mark_complete(self):
        # Child MUST implement this — no choice!
        pass

    def get_priority(self):
        # Concrete method — child gets this for FREE!
        # Can override if needed, but not mandatory
        return self.priority


# Child class — MUST implement all abstract methods
# Adds extra attribute: attendees
class MeetingTask(Task):

    def __init__(self, name, status, priority, attendees):
        super().__init__(name, status, priority)  # call parent __init__
        self.attendees = attendees                 # extra attribute for MeetingTask

    def display(self):
        # Implementing abstract method — required! ✅
        print(f"name:{self.name}|status:{self.status}|priority:{self.priority}|attendees:{self.attendees}")

    def mark_complete(self):
        # Implementing abstract method — required! ✅
        self.status = "completed"
        print(f"{self.name} is completed")


# ============================================
# Testing
# ============================================

Task_1 = MeetingTask("updates", "completed", "top", 75)
Task_1.display()          # calls MeetingTask's display
Task_1.mark_complete()    # calls MeetingTask's mark_complete
print(Task_1.get_priority())  # calls concrete method from Task — inherited for free!

# This would give ERROR — cannot create abstract class directly!
# task = Task("Some Task", "todo", "high")  ❌ TypeError