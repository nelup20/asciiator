import sys

import pytest


@pytest.fixture
def handle_sys_args(request):
    sys.argv.append(request.param)
    yield
    sys.argv.remove(request.param)
