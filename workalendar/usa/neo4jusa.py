from workalendar.core import WesternCalendar

class Neo4jUSA(WesternCalendar):
    # Fixed Holidays gives you NY Day
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 20, "President's Day"),
        (5, 29, "Memorial Day"),
        (6, 23, "Mid-Summer Holiday (Observed)"),
        (7, 4, "Independence Day"),
        (9, 4, "Labor Day"),
        (11, 23, "Thanksgiving Day"),
        (11, 24, "Day After Thanksgiving Day"),
        (12, 22, "Christmas Eve Day (Observed)"),
        (12, 25, "Christmas Day"),
        (12, 29, "New Year's Eve Day (Observed)"),

    )
