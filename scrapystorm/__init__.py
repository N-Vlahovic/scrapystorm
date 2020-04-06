from enum import Enum, unique
import requests
from pydantic import BaseModel
from typing import List, Optional, Union

__all__ = ['API']


@unique
class TaskType(str, Enum):
    flowchart = 'flowchart'
    smart = 'smart'


class Task(BaseModel):
    name: str
    time_create: Union[float, int]
    task_id: int
    type: TaskType


class APIConfig:
    root: str = 'localhost'
    port: int = 8080


class APIResponse(BaseModel):
    code: int
    list: Optional[List[Task]]
    msg: str
    status: Optional[str]


@unique
class APIAction(str, Enum):
    copy = 'copy'
    data_clear = 'data/clear'
    delete = 'delete'
    list = 'list'
    start = 'start'
    status = 'status'
    stop = 'stop'


class Utils(APIConfig):
    @classmethod
    def build_url(cls, action: APIAction, task_id: int = None, **kwargs) -> str:
        url = f'http://{cls.root}:{cls.port}/rest/v1/task/' + (f'{task_id}/' if task_id else '') + action.value
        if kwargs:
            url += '?' + '&'.join(f'{k}={v}' for k, v in kwargs.items() if v)
        return url


class API(Utils):
    @classmethod
    def get_tasks(cls, timeout: int = 5) -> APIResponse:
        """
        Get All Tasks
        :param timeout: Number of seconds to wait for a response.
        :return: An APIResponse instance containing a list of tasks.
        """
        response = requests.get(cls.build_url(action=APIAction.list), timeout=timeout)
        return APIResponse(**response.json())

    @classmethod
    def task_start(cls, task_id: int) -> APIResponse:
        """
        Start Task
        :param task_id: The of the task.
        :return: An APIResponse instance.
        """
        return APIResponse(**requests.get(cls.build_url(action=APIAction.start, task_id=task_id)).json())

    @classmethod
    def task_stop(cls, task_id: int) -> APIResponse:
        """
        Stop Task
        :param task_id: The of the task.
        :return: An APIResponse instance.
        """
        return APIResponse(**requests.get(cls.build_url(action=APIAction.stop, task_id=task_id)).json())

    @classmethod
    def task_status(cls, task_id: int) -> APIResponse:
        """
        Get Task Status
        :param task_id: The of the task.
        :return: An APIResponse instance containing the task's status.
        """
        return APIResponse(**requests.get(cls.build_url(action=APIAction.status, task_id=task_id)).json())

    @classmethod
    def task_copy(cls, task_id: int, name: None, translate_chart: bool = None) -> APIResponse:
        return APIResponse(**requests.get(cls.build_url(action=APIAction.delete, task_id=task_id, name=name,
                                                        translate_chart='true' if translate_chart else 'false')).json())

    @classmethod
    def task_delete(cls, task_id: int) -> APIResponse:
        """
        Delete Task
        :param task_id: The of the task.
        :return: An APIResponse instance.
        """
        return APIResponse(**requests.get(cls.build_url(action=APIAction.delete, task_id=task_id)).json())

    @classmethod
    def task_clear_data(cls, task_id: int) -> APIResponse:
        """
        Clear Task Data
        :param task_id: The of the task.
        :return: An APIResponse instance.
        """
        return APIResponse(**requests.get(cls.build_url(action=APIAction.data_clear, task_id=task_id)).json())
