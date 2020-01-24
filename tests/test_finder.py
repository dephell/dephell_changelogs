# external
import pytest

# project
from dephell_changelogs._finder import get_changelog_url


@pytest.mark.parametrize('given, expected', [
    # test different resources for one project
    (
        'dephell',
        'https://raw.githubusercontent.com/dephell/dephell/master/docs/changelog.md',
    ),
    (
        'https://dephell.readthedocs.io/',
        'https://raw.githubusercontent.com/dephell/dephell/master/docs/changelog.md',
    ),
    (
        'https://github.com/dephell/dephell/',
        'https://raw.githubusercontent.com/dephell/dephell/master/docs/changelog.md',
    ),

    # test different projects
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
    (
        'attrs',
        'https://raw.githubusercontent.com/python-attrs/attrs/master/CHANGELOG.rst',
    ),
])
def test_get_changelog_url(given: str, expected: str):
    assert get_changelog_url(given) == expected
