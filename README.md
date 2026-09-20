# Лабораторные работы по Python

Репозиторий с выполненными заданиями по дисциплине "Теория алгоритмов", 3 курс.

---

## Структура проекта

```
python-lab-1/
├── main.py                 # верхнеуровневый модуль — запускает все задания
├── tasks/                  # модули с логикой заданий
│   ├── __init__.py
│   ├── distance.py         # задание 1: расстояния между городами
│   ├── circle.py           # задание 2: площадь круга, точка внутри круга
│   ├── operations.py       # задание 3: расстановка знаков 1 2 3 4 5 = 25
│   ├── favorite_movies.py  # задание 4: срезы строк
│   ├── my_family.py        # задание 5: рост семьи
│   ├── zoo.py              # задание 6: список зоопарка
│   ├── songs_list.py       # задание 7: длительность песен
│   ├── secret.py           # задание 8: расшифровка сообщения
│   ├── garden.py           # задание 9: множества цветов
│   ├── shopping.py         # задание 10: минимальные цены
│   └── store.py            # задание 11: стоимость товаров на складе
├── tests/
│   └── test_tasks.py       # тесты для всех заданий
├── conftest.py             # конфиг pytest (rootdir)
├── requirements.txt        # зависимости проекта
├── .gitignore
└── README.md
```

---

## Требования

- Python 3.10+
- pip

---

## Установка

```bash
git clone https://github.com/ТВОЙ_НИК/python-lab-1.git
cd python-lab-1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## Запуск

Все задания сразу:

```bash
python main.py
```

Отдельное задание:

```bash
python -m tasks.distance
python -m tasks.circle
```

Тесты:

```bash
pytest -v
```

---

## Задания

| №  | Модуль                | Тема                             |
|----|-----------------------|----------------------------------|
| 1  | `distance.py`         | Расстояния между городами        |
| 2  | `circle.py`           | Площадь круга и точка внутри     |
| 3  | `operations.py`       | Расстановка знаков операций      |
| 4  | `favorite_movies.py`  | Срезы строк                      |
| 5  | `my_family.py`        | Списки и суммы                   |
| 6  | `zoo.py`              | Операции над списками            |
| 7  | `songs_list.py`       | Работа со списками и словарями   |
| 8  | `secret.py`           | Срезы и расшифровка              |
| 9  | `garden.py`           | Множества                        |
| 10 | `shopping.py`         | Словари и минимальные цены       |
| 11 | `store.py`            | Вложенные структуры              |

---

## Технологии

- Python 3.12
- pytest (тестирование)
- Git (контроль версий)

---

## Ссылки на материалы

- [Официальная документация Python](https://docs.python.org/3/)
- [pytest документация](https://docs.pytest.org/)
- [Git документация](https://git-scm.com/doc)
