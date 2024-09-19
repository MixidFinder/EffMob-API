import time

import pytest

import github_api


@pytest.fixture(autouse=True)
def repo_name():
    return "test-repo"


def test_repo(repo_name):
    assert github_api.create_repo(repo_name)
    time.sleep(10)
    assert github_api.check_repo(repo_name)
    time.sleep(2)
    assert github_api.delete_repo(repo_name)
    time.sleep(20)
    assert not github_api.check_repo(repo_name)
