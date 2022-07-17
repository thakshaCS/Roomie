import WeeklySchedule

class User:
    """A Roomie User.

    === Attributes ===
    username: the unique username of the user.
    password: the password for the user account
    users_todo: the user's to-do for the day
    """
    # Attribute types
    username: str
    password: str
    users_todo: list[str]

    def __init__(self, username: str, password: str, weekly_schedule: WeeklySchedule):
        self.username = username
        self.password = password
        self.users_todo = []
        self.weekly_schedule = weekly_schedule


