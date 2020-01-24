# built-in
import re
from typing import Dict, Optional


rex_version = re.compile(r'[0-9]+\.[0-9]+\.[0-9]+')


def _get_version(line: str) -> Optional[str]:
    line = line.strip()
    if not (3 <= len(line) < 40):
        return None

    if ':release:`' in line:
        return line.split(':release:`')[1].split()[0]

    if line.startswith(('Version ', 'Release ', ':version:', '.. scm-version-title:: ')):
        version = line.lstrip('. ').split()[1].lstrip('Vv.')
        if version[0].isdigit():
            return version

    match = rex_version.fullmatch(line.strip('#=*-v '))
    if match:
        return match.group(0)

    line = line.lstrip('# =')
    if not line:
        return None
    if not (line[0].isdigit() or line[0].isalpha()):
        return None

    match = rex_version.search(line)
    if match:
        return match.group(0)

    version = line.lstrip('Vv. ')
    if version[0].isdigit():
        return version.split()[0]

    return None


def parse_changelog(content: str) -> Dict[str, str]:
    changelog = dict()

    version = None
    notes = []
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
            changelog[version] = '\n'.join(notes)
        version = new_version
        notes = []
        continue

    if notes:
        changelog[version] = '\n'.join(notes)

    return changelog
