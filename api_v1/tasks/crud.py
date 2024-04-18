from api_v1.utils import BaseObjectCRUD, BaseObjectDependencies
from api_v1.models import Task


task_crud = BaseObjectCRUD(Task)
task_dependencies = BaseObjectDependencies(task_crud, "task")
