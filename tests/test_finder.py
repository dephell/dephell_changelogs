# external
import pytest

# project
from dephell_changelogs._finder import get_changelog_url


@pytest.mark.parametrize('given, expected', [
    (
        'dephell',
        'https://raw.githubusercontent.com/dephell/dephell/master/docs/changelog.md',
    ),
    (
        'pip',
        'https://raw.githubusercontent.com/pypa/pip/master/NEWS.rst',
    ),
    (
        'selenium',
        'https://raw.githubusercontent.com/SeleniumHQ/selenium/master/py/CHANGES',
    ),
    (
        'sqlalchemy',
        'https://raw.githubusercontent.com/sqlalchemy/sqlalchemy/master/CHANGES',
    ),
    (
        'django-hijack',
        'https://raw.githubusercontent.com/arteria/django-hijack/master/CHANGELOG.txt',
    ),
    (
        'python-memcached',
        'https://raw.githubusercontent.com/linsomniac/python-memcached/master/ChangeLog',
    ),
    (
        'Alabaster',
        'https://raw.githubusercontent.com/bitprophet/alabaster/master/docs/changelog.rst',
    ),
    (
        'websocket-client',
        'https://raw.githubusercontent.com/websocket-client/websocket-client/master/ChangeLog',
    ),
])
def test_get_changelog_url(given: str, expected: str):
    assert get_changelog_url(given) == expected
