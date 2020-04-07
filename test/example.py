import os
import pandas as pd
from scrapystorm import API
from typing import List, NoReturn


task = API.get_task_by_name(task_name='INSTAGRAM_TASK_1')


class Config:
    resources_path: str = f'{os.path.abspath(os.path.dirname(__file__))}/resources'


def create_resource(task_id: int) -> NoReturn:
    """Create an excel file containing the URLs needed for our first task"""
    url_list: List[str] = ['https://www.instagram.com/sennheiser/', 'https://www.instagram.com/nexup_official/']
    # df = pd.DataFrame(data=url_list, columns=['URL'])
    folder = f'{Config.resources_path}/{task_id}'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    with open(f'{folder}/urls.txt', 'w') as file:
        file.write('\n'.join(url_list))
    print(f'Saved at {folder}/urls.txt')
    # df.to_excel(f'{folder}/urls.xlsx', index=False)


if __name__ == '__main__':
    create_resource(task_id=task.task_id)
    print(task)
