import User


class Task:
    """A Task.

        === Attributes ===
        description: the description of the task to do.
        is_done: True iff the task has been done.
        due_date: The date by which the task should be done.
        assigned_to: the user to whom the task is assigned
        """
    # Attribute types
    description: str
    is_done: bool
    due_date: str
    assigned_to: User

    def __init__(self, description: str, due_date: str, assigned_to: User):

        self.assigned_to = assigned_to
        self.description = description
        self.is_done = False
        self.due_date = due_date

    def edit_task(self, modified_task: str):
        self.description = modified_task

    def reassign_task(self, user_to_reassign_task_to: User):
        self.assigned_to = user_to_reassign_task_to

    def mark_task_as_done(self):
        self.is_done = True

    def change_due_date(self, new_due_date: str):
        self.due_date = new_due_date
