from typing import List, Dict


class Human:
    def __init__(self, age: int, name: str, surname: str, person_id: int, gender: str, address: str):
        self.age = age
        self.name = name
        self.surname = surname
        self.person_id = person_id
        self.gender = gender
        self.address = address

    def get_id(self) -> int:
        return self.person_id  # Основна функція для отримання ID

    def get_address(self) -> str:
        pass  # Заглушка: функція може повертати адресу, але це не критично


class Worker(Human):
    def __init__(self, age: int, name: str, surname: str, person_id: int, gender: str, address: str, position: str):
        super().__init__(age, name, surname, person_id, gender, address)
        self.position = position
        self.assigned_projects: List['Project'] = []

    def login(self):
        print(f"{self.name} logged in.")  # Основна функція

    def logout(self):
        pass  # Заглушка: вихід із системи не критичний для демонстрації

    @staticmethod
    def upload_work_report(report: str):
        pass  # Заглушка: завантаження звіту реалізуємо окремо

    def view_assigned_projects(self) -> List['Project']:
        return self.assigned_projects  # Основна функція для перегляду проектів


class Accountant(Worker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tax_report = ""
        self.financial_report = ""
        self.payroll_report = ""

    @staticmethod
    def generate_or_upload_work_time_report() -> str:
        return "Generated work-time report"  # Основна функція: створення звітів

    @staticmethod
    def get_project_lists() -> List['Project']:
        pass  # Заглушка: отримання списку проектів


class HeadOfDepartment(Worker):
    def __init__(self, *args, department_name: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.department_name = department_name
        self.current_projects: List['Project'] = []
        self.number_of_employees = 0

    @staticmethod
    def grant_leave(employee: Worker, days: int):
        print(f"{employee.name} granted leave for {days} days.")  # Основна функція

    @staticmethod
    def assign_project(employee: Worker, project: 'Project'):
        employee.assigned_projects.append(project)
        print(f"Assigned project {project.project_name} to {employee.name}")  # Основна функція

    @staticmethod
    def change_current_project(employee: Worker, new_project: 'Project'):
        pass  # Заглушка: зміна проекту не критична


class Director(Worker):
    def __init__(self, *args, budget: float, strategic_goals: List[str], years_of_experience: int, company_vision: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.budget = budget
        self.strategic_goals = strategic_goals
        self.years_of_experience = years_of_experience
        self.company_vision = company_vision

    @staticmethod
    def change_role(employee: Worker, new_position: str):
        employee.position = new_position
        print(f"{employee.name}'s position changed to {new_position}")  # Основна функція

    @staticmethod
    def delete_staff(employee: Worker):
        pass  # Заглушка: видалення працівника

    @staticmethod
    def add_staff(employee: Worker):
        pass  # Заглушка: додавання працівника


class Departments:
    def __init__(self, department_id: int, department_name: str):
        self.department_id = department_id
        self.department_name = department_name
        self.workers: List[Worker] = []

    def add_worker(self, worker: Worker):
        self.workers.append(worker)
        print(f"{worker.name} added to department {self.department_name}")  # Основна функція

    def remove_worker(self, worker: Worker):
        pass  # Заглушка: видалення працівника з відділу

    def get_workers(self) -> List[Worker]:
        return self.workers  # Основна функція для отримання списку працівників


class Organisation:
    def __init__(self, organisation_id: int, organisation_name: str, location: str):
        self.organisation_id = organisation_id
        self.organisation_name = organisation_name
        self.location = location
        self.workers: List[Worker] = []
        self.departments: List[Departments] = []

    @staticmethod
    def list_all_projects() -> List['Project']:
        pass  # Заглушка: отримання списку проектів

    def calculate_worker_distribution(self) -> Dict[str, int]:
        return {dept.department_name: len(dept.get_workers()) for dept in self.departments}  # Основна функція

    def update_organisation_name(self, new_name: str):
        pass  # Заглушка: оновлення назви організації


class Project:
    def __init__(self, project_id: int, project_name: str, budget: float):
        self.project_id = project_id
        self.project_name = project_name
        self.budget = budget

    def update_budget(self, new_budget: float):
        self.budget = new_budget
        print(f"Budget updated to {new_budget}")  # Основна функція

    def generate_report(self) -> str:
        return f"Report for project {self.project_name}"  # Основна функція

    def calculate_remaining_budget(self) -> float:
        pass  # Заглушка: залишок бюджету

    def assign_deadline(self, deadline: str):
        pass  # Заглушка: призначення дедлайну

    def prioritize(self, priority_level: str):
        pass  # Заглушка: встановлення пріоритету


# Створення проектів
project1 = Project(1, "Project A", 10000.0)
project2 = Project(2, "Project B", 20000.0)

# Створення працівників
worker1 = Worker(30, "John", "Doe", 101, "Male", "123 Main St", "Developer")
worker2 = Worker(25, "Alice", "Smith", 102, "Female", "456 Oak St", "Tester")

# Призначення проектів працівникам
HeadOfDepartment.assign_project(worker1, project1)
HeadOfDepartment.assign_project(worker2, project2)

# Логування працівників
worker1.login()
worker2.login()

# Перегляд призначених проектів
print(f"{worker1.name}'s projects: {[project.project_name for project in worker1.view_assigned_projects()]}")
print(f"{worker2.name}'s projects: {[project.project_name for project in worker2.view_assigned_projects()]}")

# Зміна ролі працівника
Director.change_role(worker1, "Lead Developer")
print(f"{worker1.name} new position: {worker1.position}")

# Оновлення бюджету проекту
project1.update_budget(15000.0)
print(f"Updated budget for {project1.project_name}: {project1.budget}")