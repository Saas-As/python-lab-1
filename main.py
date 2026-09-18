from importlib import import_module


task_modules = [
    'distance',
    'circle',
    'operations',
    'favorite_movies',
    'my_family',
    'zoo',
    'songs_list',
    'secret',
    'garden',
    'shopping',
    'store',
]


def run():
    for module_name in task_modules:
        module = import_module(f'tasks.{module_name}')
        module.run()
        print()


if __name__ == '__main__':
    run()