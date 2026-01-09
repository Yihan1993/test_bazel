import pytest
from tools.cli_help import dummy_function

def test_should_fail():
    """This test will FAIL to demonstrate assertions work"""
    assert 1 + 1 == 3, "This assertion should fail!"

def test_cli_help_function():
    """Test that dummy_function runs without error"""
    result = dummy_function()
    assert result is None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])