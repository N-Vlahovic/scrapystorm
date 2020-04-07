import os
from scrapystorm import API
from typing import List, NoReturn


class Config:
    resources_path: str = f'{os.path.abspath(os.path.dirname(__file__))}/resources'


def create_resource(task_id: int) -> NoReturn:
    """Create an excel file containing the URLs needed for our first task"""
    url_list: List[str] = ['https://www.instagram.com/sennheiser/', 'https://www.instagram.com/nexup_official/']
    folder = f'{Config.resources_path}/{task_id}'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    with open(f'{folder}/urls.txt', 'w') as file:
        file.write('\n'.join(url_list))


def main(task_name: str):
    task = API.get_task_by_name(task_name=task_name)
    create_resource(task_id=task.task_id)
    print(task.status())
    print(f'Starting task\n{task}')
    task.start()
    print(task.status())


if __name__ == '__main__':
    main(task_name='INSTAGRAM_TASK_1')
