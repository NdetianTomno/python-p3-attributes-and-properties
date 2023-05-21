#!/usr/bin/env python3

# person.py

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job=None):
        self._name = None
        self._job = None
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 25:
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value is not None and value not in APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = value
