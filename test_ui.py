import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import base_url_ui


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Поиск на сайте")
@allure.title("Поиск по названию книги")
def test_search_by_name(driver):
    with allure.step("Открыть главную страницу"):
        driver.get(base_url_ui)

    with allure.step("Ввести в поиск название книги 'Ребенок Розмари'"):
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-search__input"))
        )
        search_input.send_keys("Ребенок Розмари")

    with allure.step("Нажать кнопку поиска"):
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header-search__button"))
        )
        search_button.click()

    with allure.step("Проверить, что отображаются результаты поиска"):
        result_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p'))
        ).text
        assert "Показываем результаты по запросу" in result_text


@allure.feature("Поиск на сайте")
@allure.title("Поиск по автору книги")
def test_search_by_author(driver):
    with allure.step("Открыть главную страницу"):
        driver.get(base_url_ui)

    with allure.step("Ввести в поиск автора 'Айра Левин'"):
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-search__input"))
        )
        search_input.send_keys("Айра Левин")

    with allure.step("Нажать кнопку поиска"):
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header-search__button"))
        )
        search_button.click()

    with allure.step("Проверить, что отображаются результаты поиска"):
        result_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p'))
        ).text
        assert "Показываем результаты по запросу" in result_text


@allure.feature("Поиск на сайте")
@allure.title("Поиск по части названия книги")
def test_using_part_of_the_title(driver):
    with allure.step("Открыть главную страницу"):
        driver.get(base_url_ui)

    with allure.step("Ввести в поиск часть названия 'Ребенок Роз'"):
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-search__input"))
        )
        search_input.send_keys("Ребенок Роз")

    with allure.step("Нажать кнопку поиска"):
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header-search__button"))
        )
        search_button.click()

    with allure.step("Проверить, что отображаются результаты поиска"):
        result_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p'))
        ).text
        assert "Показываем результаты по запросу" in result_text


@allure.feature("Поиск на сайте")
@allure.title("Поиск по названию книги из чисел")
def test_search_by_name_from_numbers(driver):
    with allure.step("Открыть главную страницу"):
        driver.get(base_url_ui)

    with allure.step("Ввести в поиск название '1984'"):
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-search__input"))
        )
        search_input.send_keys("1984")

    with allure.step("Нажать кнопку поиска"):
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header-search__button"))
        )
        search_button.click()

    with allure.step("Проверить, что отображаются результаты поиска"):
        result_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p'))
        ).text
        assert "Показываем результаты по запросу" in result_text


@allure.feature("Поиск на сайте")
@allure.title("Поиск по названию книги с точками")
def test_search_by_name_with_dots(driver):
    with allure.step("Открыть главную страницу"):
        driver.get(base_url_ui)

    with allure.step("Ввести в поиск название 's.n.u.f.f.'"):
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-search__input"))
        )
        search_input.send_keys("s.n.u.f.f.")

    with allure.step("Нажать кнопку поиска"):
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header-search__button"))
        )
        search_button.click()

    with allure.step("Проверить, что отображаются результаты поиска"):
        result_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p'))
        ).text
        assert "Показываем результаты по запросу" in result_text