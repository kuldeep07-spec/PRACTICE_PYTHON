# Practice file 1 - Class Variables vs Instance Variables
class Project:
    total_projects = 0  # Class variable to keep track of total projects
    valid_statuses = ["active", "completed", "on hold"] 
    
    def __init__(self,name,description,status):
        self.name=name
        self.description=description
        
        if status in Project.valid_statuses:
            self.status=status
        else:
            print(f"Invalid status! Setting default to 'active'")
            self.status="active"
            
        Project.total_projects += 1  # Increment total projects when a new project is created
    # For users — clean readable output
    def __str__(self):
        return f"Project Name: {self.name} | Status: {self.status}"
    # For developers — detailed debug output
    def __repr__(self):
        return f"Project(name={self.name!r}, description={self.description!r}, status={self.status!r})" 
    

# Create an object
project1 = Project("Task Manager","A CLI based task management tool","active")
project2 = Project("Website Redesign","Redesign the company website","completed")
project3 = Project("Mobile App","Develop a mobile app for our services","on hold")

print(project1)  # Output: Project Name: Task Manager | Status: active
print(project2)  # Output: Project Name: Website Redesign | Status: completed       
print(project3)  # Output: Project Name: Mobile App | Status: on hold

# Add this at the bottom of the file to test the class variable
# Add a 4th project with wrong status
project4 = Project("Blog", "A personal blog", "wrong_status")
print(project4)  # Output: Project Name: Blog | Status: active
print(f"\nTotal Projects: {Project.total_projects}")  # Output: Total Projects: 4
