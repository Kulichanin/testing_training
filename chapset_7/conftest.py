import pytest

@pytest.fixture()
def set_up():
    """
    Выполняется действие в начале каждой функции и завершается в конце каждой функции.
    """
    print('START TEST !')
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
