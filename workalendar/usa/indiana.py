# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import warnings
from datetime import date
from workalendar.core import MON, TUE, WED, THU, FRI, SAT
from .core import UnitedStates


class Indiana(UnitedStates):
    """Indiana"""
    include_good_friday = True
    include_thanksgiving_friday = True
    include_federal_presidents_day = False
    label_washington_birthday_december = "Washington's Birthday (Observed)"

    def get_washington_birthday_december(self, year):
        """
        Washington birthday observance
        Similar to Christmas Eve, but with special rules.
        It's only observed in Georgia.
        """
        warnings.warn(
            "Washington birthday rules for Indiana State are confusing. "
            "Use this calendar with care")
        christmas_day = date(year, 12, 25).weekday()
        if christmas_day == MON:
            day = date(year, 12, 26)  # TUE
        elif christmas_day == TUE:
            day = date(year, 12, 24)  # MON
        elif christmas_day == WED:
            day = date(year, 12, 26)  # TUE
        elif christmas_day == THU:
            day = date(year, 12, 26)  # FRI
        elif christmas_day == FRI:
            day = date(year, 12, 24)  # THU
        elif christmas_day == SAT:
            day = date(year, 12, 23)  # THU
        else:  # christmas_day == SUN:
            day = date(year, 12, 23)  # FRI
        return (day, self.label_washington_birthday_december)

    def get_variable_days(self, year):
        days = super(Indiana, self).get_variable_days(year)
        days.extend([
            self.get_washington_birthday_december(year),
        ])
        return days