class Project:
    def __init__(self,name,description,status):
        self.name = name
        self.description = description
        self.status = status
# For users — clean readable output
    def __str__(self):
        return f"Project Name: {self.name} | Status: {self.status}"
# For developers — detailed debug output   
    def __repr__(self):
        return f"Project(name={self.name!r}, description={self.description!r}, status={self.status!r})"
    
#name = "Task Manager"

#print(f"{name}")    # Without !r->Task Manager
#print(f"{name!r}")  # With !r ->'Task Manager'
#             
    
#__str__  defined → print() uses __str__
#__str__  missing → print() falls back to __repr__
#__repr__ always stays independent

# Create an object
project1 = Project(
    name="Task Manager",
    description="A CLI based task management tool",
    status="active"
)

print(project1)  # Output: Project Name: Task Manager | Status: active
print(repr(project1))  # Output: Project(name='Task Manager', description='A CLI based task management tool', status='active')