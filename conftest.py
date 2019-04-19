import pytest
from fixture.application import Application
import pandas

@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:\\Anna\AddressBook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


# def pytest_generate_tests(metafunc):
#     for fixture in metafunc.fixturenames:
#         data_from_excel = pandas.read_excel("D:\\Anna\python-gui-tests\\groups.xlsx")
#         metafunc.parametrize(fixture, data_from_excel, ids=[str(x) for x in data_from_excel])
#
#
