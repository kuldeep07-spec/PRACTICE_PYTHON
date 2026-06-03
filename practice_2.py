# ============================================
# Lesson 4 - Access Modifiers & @property
# ============================================

class Task:
    def __init__(self, name, assigned_to, priority):
        self.name = name                # Public — accessible from anywhere
        self._assigned_to = assigned_to # Protected — convention, don't access outside class
        self.__priority = priority      # Private — strictly protected, name mangled to _Task__priority

    def __str__(self):
        # For users — clean readable output
        return f"Task: {self.name} | Assigned to: {self._assigned_to} | Priority: {self.__priority}"

    @property
    def priority(self):
        # Getter — access private __priority like an attribute
        # Called when you do: task.priority
        return self.__priority

    @priority.setter
    def priority(self, value):
        # Setter — validates before setting private __priority
        # Called when you do: task.priority = "high"
        if value in ['low', 'medium', 'high']:
            self.__priority = value         # Valid — set the value
        else:
            self.__priority = 'low'         # Invalid — set default
            print("Invalid priority value. Setting to 'low'.")

# ============================================
# Testing
# ============================================

task1 = Task("python", "kuldeep_singh", "high")

print(task1)            # calls __str__

print(task1.priority)   # calls getter → high
task1.priority = 'medium'  # calls setter → valid
print(task1.priority)   # medium
task1.priority = 'hello'   # calls setter → invalid → sets 'low'
print(task1.priority)   # low