from dataclasses import dataclass

@dataclass()
class Human():
    name: str
    age: int
    occupation: str
    
@dataclass()
class Engineer(Human):
    skills: list
    
@dataclass()
class Employee(Engineer):
    Employee_id: str
    
abc_engineer = ("John Doe", 30, "Software Engineer", ["Python", "Java"])
print(abc_engineer)