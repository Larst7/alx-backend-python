# 0x03-Unittests and Integration Tests

This project introduces learners to writing unittests and integration tests in Python 3.

## Learning Objectives

By the end of this project, you should be able to explain:

- The difference between unit and integration tests.
- Common testing patterns such as mocking, parameterizations, and fixtures.

## Tasks

### 0. Parameterize a unit test

- **File**: `test_utils.py`
- **Description**:
  - Familiarize yourself with the `utils.access_nested_map` function.
  - Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.
  - Implement `TestAccessNestedMap.test_access_nested_map` to test the function using the following parameterized inputs:
    - `nested_map={"a": 1}, path=("a",)`
    - `nested_map={"a": {"b": 2}}, path=("a",)`
    - `nested_map={"a": {"b": 2}}, path=("a", "b")`
  - Ensure the function returns the expected result using `assertEqual`.

### 1. Parameterize a unit test for exceptions

- **File**: `test_utils.py`
- **Description**:
  - Implement `TestAccessNestedMap.test_access_nested_map_exception` to test for `KeyError` exceptions using the following parameterized inputs:
    - `nested_map={}, path=("a",)`
    - `nested_map={"a": 1}, path=("a", "b")`
  - Ensure the exception message is as expected using `assertRaises`.

### 2. Mock HTTP calls

- **File**: `test_utils.py`
- **Description**:
  - Familiarize yourself with the `utils.get_json` function.
  - Define the `TestGetJson` class and implement `TestGetJson.test_get_json`.
  - Use `unittest.mock.patch` to patch `requests.get` and return a mock object with a `json` method that returns `test_payload`.
  - Test the function with the following parameterized inputs:
    - `test_url="http://example.com", test_payload={"payload": True}`
    - `test_url="http://holberton.io", test_payload={"payload": False}`
  - Ensure the `get` method is called exactly once with the `test_url` and the output matches `test_payload`.

### 3. Parameterize and patch

- **File**: `test_utils.py`
- **Description**:
  - Familiarize yourself with the `utils.memoize` decorator.
  - Implement the `TestMemoize` class with a `test_memoize` method.
  - Define the following class inside `test_memoize`:
    ```python
    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()
    ```
  - Use `unittest.mock.patch` to mock `a_method` and ensure it is called only once when accessing `a_property` twice.

### 4. Parameterize and patch as decorators

- **File**: `test_client.py`
- **Description**:
  - Familiarize yourself with the `client.GithubOrgClient` class.
  - Implement the `TestGithubOrgClient` class with a `test_org` method.
  - Use `@patch` to mock `get_json` and ensure it is called once with the expected argument.
  - Use `@parameterized.expand` to test the method with different `org` examples (`google`, `abc`).

### 5. Mocking a property

- **File**: `test_client.py`
- **Description**:
  - Implement `test_public_repos_url` to unit-test `GithubOrgClient._public_repos_url`.
  - Use `patch` as a context manager to mock `GithubOrgClient.org` and return a known payload.
  - Ensure the result of `_public_repos_url` matches the expected value based on the mocked payload.

### 6. More patching

- **File**: `test_client.py`
- **Description**:
  - Implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`.
  - Use `@patch` to mock `get_json` and return a chosen payload.
  - Use `patch` as a context manager to mock `GithubOrgClient._public_repos_url` and return a chosen value.
  - Ensure the list of repos matches the expected payload and both mocks are called once.

### 7. Parameterize

- **File**: `test_client.py`
- **Description**:
  - Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`.
  - Use `@parameterized.expand` to test the method with the following inputs:
    - `repo={"license": {"key": "bsd-3-clause"}}, license_key="bsd-3-clause"`
    - `repo={"license": {"key": "bsl-1.0"}}, license_key="bsd-3-clause"`
  - Parameterize the expected return value.

### 8. Integration test: fixtures

- **File**: `test_client.py`
- **Description**:
  - Implement the `TestIntegrationGithubOrgClient` class and the `setUpClass` and `tearDownClass` methods.
  - Use `@parameterized_class` to decorate and parameterize the class with fixtures from `fixtures.py`.
  - Mock `requests.get` in `setUpClass` to return example payloads found in the fixtures.
  - Implement `tearDownClass` to stop the patcher.

### 9. Integration tests

- **File**: `test_client.py`
- **Description**:
  - Implement `test_public_repos` to test `GithubOrgClient.public_repos` using fixtures.
  - Ensure the method returns the expected results.
  - Implement `test_public_repos_with_license` to test `public_repos` with `license="apache-2.0"` and match the expected value from the fixtures.

## Usage

To run the tests, use the following command:

```bash
$ python -m unittest discover

