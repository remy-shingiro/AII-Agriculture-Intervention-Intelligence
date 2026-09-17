"""Smoke tests for the project environment."""

import agri_intelligence


def test_package_is_importable() -> None:
    """The source package is available to the test environment."""
    assert agri_intelligence.__version__ == "0.1.0"
