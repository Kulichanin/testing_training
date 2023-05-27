import pytest

@pytest.fixture()
def set_up(monkeypatch):
    """
    Выполняется действие в начале каждой функции и завершается в конце каждой функции.
    """
    print('START TEST !')
    inputs = iter(['mr.gn0m@yandex.ru', '1235789460578901', 'nivona'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    yield
    print('FINAL TEST !')

@pytest.fixture(scope='module')
def set_group():
    """
    Выполняется действие в начале первой функции и завершается в конце всех функций.
    """
    print('ENTER SYSTEM !')
    yield
    print('EXIT SYSTEM !')
