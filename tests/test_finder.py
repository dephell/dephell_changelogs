# external
import pytest

# project
from dephell_changelogs._finder import get_changelog_url


@pytest.mark.parametrize('given, expected', [
    (
        'https://github.com/dephell/dephell',
        'https://raw.githubusercontent.com/dephell/dephell/master/docs/changelog.md',
    ),
    (
        'https://github.com/pypa/pip',
        'https://raw.githubusercontent.com/pypa/pip/master/NEWS.rst',
    ),
    (
        'https://github.com/SeleniumHQ/selenium/',
        'https://raw.githubusercontent.com/SeleniumHQ/selenium/master/py/CHANGES',
    ),
    (
        'https://github.com/sqlalchemy/sqlalchemy/',
        'https://raw.githubusercontent.com/sqlalchemy/sqlalchemy/master/CHANGES',
    ),
    (
        'https://pypi.org/project/websocket_client/',
        'https://raw.githubusercontent.com/websocket-client/websocket-client/master/ChangeLog',
    ),
    (
        'https://pypi.org/project/django-hijack/',
        'https://raw.githubusercontent.com/arteria/django-hijack/master/CHANGELOG.txt',
    ),
    (
        'https://github.com/linsomniac/python-memcached',
        'https://raw.githubusercontent.com/linsomniac/python-memcached/master/ChangeLog',
    ),
])
def test_get_changelog_url(given: str, expected: str):
    assert get_changelog_url(given) == expected
