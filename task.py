"""
Module: management_system.py

This module contains classes for managing employees, projects, and tasks in a fictional company.
"""

class Task:
    """
    Class representing a task in the company.

    Attributes:
        task_id (str): The ID of the task.
        description (str): The description of the task.
        deadline (str): The deadline of the task.
        status (str): The status of the task.
        project (Project): The project associated with the task.
    """
    str t_task_id
    str t_description
    str t_deadline
    str t_status
    str t_status
    Project t_project

    def __init__(self, task_id, description, deadline, status, project):
        """
        Initialize a Task object.

        Args:
            task_id (str): The ID of the task.
            description (str): The description of the task.
            deadline (str): The deadline of the task.
            status (str): The status of the task.
            project (Project): The project associated with the task.
        """
        self.t_task_id = task_id
        self.t_description = description
        self.t_deadline = deadline
        self.t_status = status
        self.t_project = project

        pass
