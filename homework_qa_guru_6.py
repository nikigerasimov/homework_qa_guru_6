from datetime import time


def test_dark_theme_by_time():
    current_time = time(hour=21)
    if time(hour=22) <= current_time < time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=16)
    is_dark_theme = None


    if dark_theme_enabled_by_user == None:
        is_dark_theme = dark_theme_enabled_by_user
    if dark_theme_enabled_by_user:
        if time(hour=22) <= current_time < time(hour=6):
            assert is_dark_theme is True
            dark_theme_enabled_by_user = False

        if time(hour=22) > current_time > time(hour=6):
            assert is_dark_theme is False
            dark_theme_enabled_by_user = True


        # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    assert is_dark_theme is True


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    # TODO найдите пользователя с именем "Olga"
    suitable_users = None
    for suitable_users in users:
        if suitable_users['name'] == 'Olga':
            assert suitable_users == {"name": "Olga", "age": 45}
            break
    assert suitable_users == {"name": "Olga", "age": 45}


    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for i in users:
        if i['age'] < 20:
            suitable_users.append(i)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]





def test_read():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_name_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_name_args(open_browser, browser_name)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_name_args(open_browser, browser_name)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"

def print_name_args(func, *args):
    func_name = func._name_.replace('_', ' ').title()
    args_name = ", ".join([*args])
    print(f"{func_name [{args_name}]}")
    return f"{func_name [{args_name}]}"
