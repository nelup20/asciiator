import sys

import pytest


@pytest.fixture
def handle_sys_args(request):
    for arg in request.param:
        sys.argv.append(arg)

    yield

    for arg in request.param:
        sys.argv.remove(arg)


def clean_up_sys_argv():
    # Remove pytest & pytest-cov args
    del sys.argv[1:]
