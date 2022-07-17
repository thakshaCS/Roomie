import User
from Task import Task


class WeeklySchedule:
    """A Weekly Schedule.

        === Attributes ===
       monday: the tasks to do on Monday
        tuesday : the tasks to do on Tuesday
        wednesday: the tasks to do on Wednesday
        thursday: the tasks to do on Thursday
        friday: the tasks to do on Friday
        saturday: the tasks to do on Saturday
        sunday: the tasks to do on Sunday
        """
    # Attribute types
    monday: list[Task]
    tuesday: list[Task]
    wednesday: list[Task]
    thursday: list[Task]
    friday: list[Task]
    saturday: list[Task]
    sunday: list[Task]

    def __init__(self):
        self.monday = []
        self.tuesday = []
        self.wednesday = []
        self.thursday = []
        self.friday = []
        self.saturday = []
        self.sunday = []

    def create_task(self, description: str, due_date: str, assigned_to: User):
        if due_date == 'monday':
            self.monday.append(Task(description, due_date, assigned_to))

        elif due_date == 'tuesday':
            self.tuesday.append(Task(description, due_date, assigned_to))

        elif due_date == 'wednesday':
            self.wednesday.append(Task(description, due_date, assigned_to))

        elif due_date == 'thursday':
            self.thursday.append(Task(description, due_date, assigned_to))

        elif due_date == 'friday':
            self.friday.append(Task(description, due_date, assigned_to))

        elif due_date == 'saturday':
            self.saturday.append(Task(description, due_date, assigned_to))

        else:
            self.sunday.append(Task(description, due_date, assigned_to))

