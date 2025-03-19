import requests
import allure
from config import headers, base_url

API_URL = base_url + "/api/v1/recommend/semantic"


@allure.feature("Поиск книг")
@allure.title("Поиск по названию книги")
def test_search_by_name():
    with allure.step("Выполнить поиск по названию книги 'Ребенок Розмари'"):
        res = requests.get(
            f"{API_URL}?phrase=Ребенок Розмари&perPage=48", headers=headers)
    with (allure.step("Проверить, что статус-код ответа равен 200")):
        assert res.status_code == 200, (f"Ожидался статус-код 200,"
                                        f" но получен {res.status_code}")


@allure.feature("Поиск книг")
@allure.title("Поиск по автору книги")
def test_search_by_author():
    with allure.step("Выполнить поиск по автору 'Айра Левин'"):
        res = requests.get(
            f"{API_URL}?phrase=Айра Левин&perPage=48", headers=headers)
    with (allure.step("Проверить, что статус-код ответа равен 200")):
        assert res.status_code == 200, (f"Ожидался статус-код 200,"
                                        f" но получен {res.status_code}")


@allure.feature("Поиск книг")
@allure.title("Поиск по части названия книги")
def test_using_part_of_the_title():
    with allure.step("Выполнить поиск по части названия 'Ребенок'"):
        res = requests.get(
            f"{API_URL}?phrase=Ребенок&perPage=48", headers=headers)
    with (allure.step("Проверить, что статус-код ответа равен 200")):
        assert res.status_code == 200, (f"Ожидался статус-код 200,"
                                        f" но получен {res.status_code}")


@allure.feature("Поиск книг")
@allure.title("Поиск по названию книги из чисел")
def test_search_by_name_from_numbers():
    with allure.step("Выполнить поиск по названию '1984'"):
        res = requests.get(
            f"{API_URL}?phrase=1984&perPage=48", headers=headers)
    with (allure.step("Проверить, что статус-код ответа равен 200")):
        assert res.status_code == 200, (f"Ожидался статус-код 200,"
                                        f" но получен {res.status_code}")


@allure.feature("Поиск книг")
@allure.title("Поиск по названию книги с точками")
def test_search_by_name_with_dots():
    with allure.step("Выполнить поиск по названию 's.n.u.f.f.'"):
        res = requests.get(
            f"{API_URL}?phrase=s.n.u.f.f.&perPage=48", headers=headers)
    with (allure.step("Проверить, что статус-код ответа равен 200")):
        assert res.status_code == 200, (f"Ожидался статус-код 200,"
                                        f" но получен {res.status_code}")