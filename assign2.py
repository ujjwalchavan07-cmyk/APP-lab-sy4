# Dynamic Report Generator

# Decorator to add a header and footer
def report_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 30 + " STUDENT REPORT " + "=" * 30)
        func(*args, **kwargs)
        print("=" * 76)
    return wrapper


class Report:

    # Class variable
    college_name = "ABC Engineering College"

    # Magic method to initialize student details
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Class method to change the college name
    @classmethod
    def change_college(cls, new_college):
        cls.college_name = new_college

    # Magic method to return a formatted report
    def __str__(self):

        # Determine result dynamically
        if self.marks >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        return (
            f"College : {Report.college_name}\n"
            f"Name : {self.name}\n"
            f"Roll No : {self.roll_no}\n"
            f"Marks : {self.marks}\n"
            f"Result : {result}"
        )

    # Display report with decorator
    @report_header
    def display_report(self):
        print(self)


# Create the first student report
student1 = Report("Rahul", 101, 85)

# Display the first report
student1.display_report()


# Change college name using the class method
Report.change_college("XYZ Institute of Technology")


# Create the second student report
student2 = Report("Priya", 102, 35)

# Display the second report
student2.display_report()