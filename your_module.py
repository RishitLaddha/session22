# Improved implementation with enhanced comments and encapsulation

class Person:
    def __init__(self, name: str, age: int, job: str):
        # Store values as "private" attributes to encourage encapsulation.
        self._name = name
        self._age = age
        self._job = job

    @property
    def name(self):
        """Return the name of the person."""
        return self._name
    
    @property
    def age(self):
        """Return the age of the person."""
        return self._age

    @property
    def job(self):
        """Return the job of the person."""
        return self._job

    def get_details(self):
        """
        Return a string representation of the person's details.
        Expected format: "Name: {name}, Age: {age}, Job: {job}"
        """
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"   


class Student(Person):
    def __init__(self, name: str, age: int, job: str, grade: str):
        # Initialize the base Person class attributes.
        super().__init__(name, age, job)
        self._grade = grade

    @property
    def grade(self):
        """Return the grade of the student."""
        return self._grade

    def get_details(self):
        """
        Extend the base Person details by appending the student's grade.
        Expected format: "Name: {name}, Age: {age}, Job: {job}, Grade: {grade}"
        """
        person_details = super().get_details()
        return f"{person_details}, Grade: {self.grade}"


class Professor(Person):   
    def __init__(self, name: str, age: int, job: str, courses: list):
        # Initialize the base Person class attributes.
        super().__init__(name, age, job)
        self._courses = courses

    @property
    def courses(self):
        """Return the list of courses taught by the professor."""
        return self._courses 

    def get_details(self):
        """
        Extend the base Person details by appending the professor's courses.
        Expected format: "Name: {name}, Age: {age}, Job: {job}, Courses: {courses}"
        """
        person_details = super().get_details()
        return f"{person_details}, Courses: {self.courses}"   


class Employee(Person): 
    def __init__(self, name: str, age: int, job: str, department: str):
        # Initialize the base Person class attributes.
        super().__init__(name, age, job)
        self._department = department
    
    @property
    def department(self):
        """Return the department in which the employee works."""
        return self._department 

    def get_details(self):
        """
        Extend the base Person details by appending the employee's department.
        Expected format: "Name: {name}, Age: {age}, Job: {job}, Department: {department}"
        """
        person_details = super().get_details()
        return f"{person_details}, Department: {self.department}" 


class StudentProfessor(Student, Professor):
    def __init__(self, name: str, age: int, job: str, courses: list, grade: str):
        """
        In multiple inheritance, to avoid conflicts from super() calls,
        we directly initialize the base class (Person) and then set additional attributes.
        """
        # Directly call Person's __init__ to initialize the common attributes.
        Person.__init__(self, name, age, job)
        # Set Student-specific and Professor-specific attributes.
        self._grade = grade
        self._courses = courses
    
    def get_details(self):
        """
        Combine both student and professor details without redundancy.
        We use the stored attributes directly.
        Expected format:
        "Name: {name}, Age: {age}, Job: {job}, Courses: {courses}, Grade: {grade}"
        """
        return (
            f"Name: {self.name}, Age: {self.age}, Job: {self.job}, "
            f"Courses: {self._courses}, Grade: {self._grade}"
        )


class Location:
    # Use __slots__ to restrict attributes to save memory and prevent dynamic attribute creation.
    __slots__ = '_name', '_longitude', '_latitude'
    
    def __init__(self, name, longitude, latitude):
        # Initialize the location with private attributes.
        self._name = name
        self._longitude = longitude
        self._latitude = latitude
    
    @property
    def name(self):
        """Return the name of the location."""
        return self._name  
    
    @name.setter
    def name(self, new_name):
        """Allow updating the name of the location."""
        self._name = new_name
        
    @property
    def longitude(self):
        """Return the longitude coordinate."""
        return self._longitude
    
    @property
    def latitude(self):
        """Return the latitude coordinate."""
        return self._latitude

    def get_coordinates(self):
        """
        Return a tuple of (longitude, latitude).
        This represents the location's coordinates.
        """
        return (self.longitude, self.latitude)
