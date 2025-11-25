import time


def test_guest_should_see_add_to_basket_button(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Пауза для визуальной проверки языка
    time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину
    add_to_basket_button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    
    # Убеждаемся, что кнопка есть на странице
    assert len(add_to_basket_button) > 0, "Add to basket button is not found on the page"
    
    # Проверяем, что кнопка видима и активна
    assert add_to_basket_button[0].is_displayed(), "Add to basket button is not visible"
    assert add_to_basket_button[0].is_enabled(), "Add to basket button is not enabled"