# built-in
import re
from typing import Dict, List, Optional

# external
import requests


rex_version = re.compile(r'[0-9]+\.[0-9]+\.[0-9]+')

_VERSION_REX = r'(?:[vV]\.?)?([0-9\.]+)'
rexes = (
    # `Version 1.2.3 ...`
    re.compile(r'(?:Version|Release) {}.*'.format(_VERSION_REX)),
    # `## 2.3.4 ...`
    re.compile(r'(?:\#|\=)+ {}.*'.format(_VERSION_REX)),
    # `v.2.3.4`
    re.compile(_VERSION_REX),
    # `v.2.3.4 (2019-01-02)`
    re.compile(r'{} \([0-9-]+\)'.format(_VERSION_REX)),
    # `* 1.2.3`
    re.compile(r'[\+\-\*] {}'.format(_VERSION_REX)),
    # `...:release:`1.11.0 <2018-03-19>`...`
    re.compile(r'.*\:release\:\`{}.*'.format(_VERSION_REX)),
    # `What's new in psycopg 2.8.4`
    re.compile(r'What\'s new in.* {}'.format(_VERSION_REX)),
    # `= 2.0.1 ...`
    re.compile(r'= {} .*'.format(_VERSION_REX)),
)


def _get_version(line: str) -> Optional[str]:
    line = line.strip()
    if not (3 <= len(line) < 60):
        return None

    for rex in rexes:
        match = rex.fullmatch(line)
        if match:
            return match.groups()[-1]

    if line.startswith('.. scm-version-title:: '):
        return line.lstrip('. ').split()[1].lstrip('v. ')

    words = line.split()
    if len(words) == 2 and rex_version.fullmatch(words[1]):
        return words[1]

    return None


def parse_changelog(content: str) -> Dict[str, str]:
    if content.startswith('https://') and len(content.split()) == 1:
        response = requests.get(url=content)
        response.raise_for_status()
        content = response.text

    changelog = dict()  # type: Dict[str, str]
    version = 'unknown'
    notes = []  # type: List[str]
    for line in content.splitlines():
        # drop rst-like header from the section beginning
        if not notes:
            symbols = ''.join(set(line.strip()))
            if len(symbols) == 1 and symbols in '+-=':
                continue

        new_version = _get_version(line=line)
        if not new_version:
            notes.append(line)
            continue

        # save old section and start new one
        if notes:
            text = '\n'.join(notes).strip('\n')
            if text:
                changelog[version] = text
        version = new_version
        notes = []
        continue

    if notes:
        text = '\n'.join(notes).strip('\n')
        if text:
            changelog[version] = text

    return changelog
