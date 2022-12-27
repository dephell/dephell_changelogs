from textwrap import dedent

# external
import pytest

# project
from dephell_changelogs._parser import _get_version, parse_changelog


@pytest.mark.parametrize('given, expected', [
    ('Version 1.1.2',               '1.1.2'),   # flask
    ('Version 0.2',                 '0.2'),     # flask
    ('## v.0.8.0 (2019-12-19)',     '0.8.0'),   # dephell
    ('0.14.0 (2018-01-9)',          '0.14.0'),  # changelogs
    ('Mayavi 4.5.0',                '4.5.0'),   # mayavi
    ('v0.16.0',                     '0.16.0'),  # py-trello
    ('1.11.7',                      '1.11.7'),  # boto3
    ('2.2.2 (2019-12-26)',          '2.2.2'),   # dynaconf
    ('20.0.1 (2020-01-21)',         '20.0.1'),  # pip
    ('0.2',                         '0.2'),     # pip
    ('1.0.0b3',                    '1.0.0b3'),  # pytest
    ('pytest 5.3.3 (2020-01-16)',   '5.3.3'),   # pytest
    ('* 2.2.1',                     '2.2.1'),   # pyyaml
    ('- v0.5.1',                    '0.5.1'),   # websocket-client

    ('.. scm-version-title:: v5.5.1', '5.5.1'),             # cheroot
    ('= 2.0.0 "Who cares for fish?" (20050410)', '2.0.0'),  # bs4
    ('* :release:`1.11.0 <2018-03-19>`', '1.11.0'),         # twine
    ("What's new in psycopg 2.8.4", '2.8.4'),               # psycopg2-binary
])
def test_get_version(given: str, expected: str):
    assert _get_version(given) == expected


def test_parse_changelog():
    given = dedent("""
        # v.2.3.1

        - do this
        - do that

        # v.2.3.0

        - do something
    """)
    expected = {
        '2.3.1': '- do this\n- do that',
        '2.3.0': '- do something',
    }
    assert parse_changelog(given) == expected
