# ДЗ 2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

import setup

setup(
    name='file-manager',
    version='1.0.0',
    description='Пакет для работы с файлами разных форматов',
    author='Esin EA',
    author_email='your@email.com',
    install_requires=[
        'json',
        'csv',
        'pickle'
    ]
)
