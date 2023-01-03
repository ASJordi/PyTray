from pytray.utils import test_speed


def test_speed_success():
  assert test_speed() is not None


def test_speed_returns_tuple():
  assert isinstance(test_speed(), tuple)
  assert len(test_speed()) == 3


def test_speed_returns_number():
  assert isinstance(test_speed()[0], (int, float))


def test_speed_returns_expected_values():
  assert test_speed()[0] > 0
  assert test_speed()[1] > 0
  assert test_speed()[2] > 0
