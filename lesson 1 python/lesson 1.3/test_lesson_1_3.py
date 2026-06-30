"""
Тесты к уроку 1.3: Списки, кортежи, словари, множества.

Запусти после выполнения домашки:
    pytest test_main.py -v
"""

from data_collections import task_1, task_2, task_3, task_4, task_5, task_6


class TestHomework:
    def test_task_1_creates_list(self):
        result = task_1()
        assert isinstance(result, list)
        assert result == ["яблоко", "банан", "киви"]

    def test_task_2_list_index(self):
        result = task_2()
        assert result == "яблоко"

    def test_task_3_creates_tuple(self):
        result = task_3()
        assert isinstance(result, tuple)
        assert result == (10, 20)

    def test_task_4_creates_dict(self):
        result = task_4()
        assert isinstance(result, dict)
        assert result == {"name": "Анна", "age": 25}

    def test_task_5_adds_dict_key(self):
        result = task_5()
        assert result == {"name": "Анна", "age": 25, "city": "Москва"}

    def test_task_6_creates_set(self):
        result = task_6()
        assert isinstance(result, set)
        assert result == {"python", "docker"}
