# Tasks are added, stored in a queue, sorted by priority, processed one at a time, and can be undone using a stack.

# Each task has:
    # name
    # priority (number)
    # deadline

class Task_Manager():

    def __init__(self, name, priority, deadline, completed):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.completed = completed

    def __str__(self):
        result = ""
        