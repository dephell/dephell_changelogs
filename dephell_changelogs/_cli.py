import sys

from ._finder import get_changelog_url


def main(argv) -> int:
    if not argv:
        raise ValueError('project name or URL required')
    url = get_changelog_url(argv[0])
    if not url:
        return 1
    print(url)
    return 0


def entrypoint():
    sys.exit(main(sys.argv[1:]))
