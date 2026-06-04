# ============================================
# Lesson 5 - Inheritance & super()
# ============================================

# Parent class — contains common attributes and methods
class Task:
    def __init__(self, name, status, priority):
        self.name = name            # task name
        self.status = status        # task status
        self.priority = priority    # task priority

    def display(self):
        # Display basic task information
        print(f"Task(name:{self.name}|status:{self.status}|priority:{self.priority})")

    def mark_complete(self):
        # Update status to completed — inherited by all child classes
        self.status = "completed"
        print(f"{self.name} task is completed")


# Child class — inherits from Task, adds severity
class BugTask(Task):
    def __init__(self, name, status, priority, severity):
        super().__init__(name, status, priority)  # call parent __init__ to get common attributes
        self.severity = severity                   # extra attribute specific to BugTask

    def display(self):
        super().display()               # call parent display first — no code repetition!
        print(f"Severity: {self.severity}")  # then add BugTask specific info


# Child class — inherits from Task, adds deadline
class FeatureTask(Task):
    def __init__(self, name, status, priority, deadline):
        super().__init__(name, status, priority)  # call parent __init__ to get common attributes
        self.deadline = deadline                   # extra attribute specific to FeatureTask

    def display(self):
        super().display()               # call parent display first — no code repetition!
        print(f"Deadline: {self.deadline}")  # then add FeatureTask specific info


# ============================================
# Testing
# ============================================

task1 = BugTask("python", "inprogress", "Medium", "high")
task2 = FeatureTask("fastapi", "inprogress", "Medium", "9-10-2026")

task1.mark_complete()   # inherited from Task — status → completed
task1.display()         # shows Task info + severity
print()
task2.mark_complete()   # inherited from Task — status → completed
task2.display()         # shows Task info + deadline
print(task2.deadline)   # direct attribute access