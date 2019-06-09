from unittest import TestCase
from .calc_dts import get_hundred_days_end_date, \
    get_days_between_pb_start_first_joint_pycon


class TestGet_hundred_days_end_date(TestCase):
    def test_get_hundred_days_end_date(self):
        assert get_hundred_days_end_date() == '2017-07-08'

    def test_get_days_till_pycon_meetup(self):
        assert get_days_between_pb_start_first_joint_pycon() == 505
