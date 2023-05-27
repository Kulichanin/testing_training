import pytest

@pytest.fixture()
def set_up_1(monkeypatch):
    """
    Выполняется действие в начале каждой функции и завершается в конце каждой функции.
    """
    print('\n START TEST 1!')
    inputs = iter(['mr.gn0m@yandex.ru', '1235789460578901', 'nivona'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    yield
    print('\nFINAL TEST 1!')

@pytest.fixture()
def set_up_2(monkeypatch):
    """
    Выполняется действие в начале каждой функции и завершается в конце каждой функции.
    """
    print('\n START TEST 2!')
    inputs = iter(['mr.gn0m@yandex.ru', '1235789460578901', 'delonghi'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    yield
    print('\nFINAL TEST 2!')

@pytest.fixture()
def set_up_3(monkeypatch):
    """
    Выполняется действие в начале каждой функции и завершается в конце каждой функции.
    """
    print('\n START TEST 3!')
    inputs = iter(['mr.gn0m@yandex.ru', '1235789460578901', 'melitta'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    yield
    print('\nFINAL TEST 3!')

