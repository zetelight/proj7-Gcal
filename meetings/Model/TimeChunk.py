"""
A class for time chunk on google calendar
"""
######
#
# Under Construction.
# Be ready for project 8, 9
#
#######


class CalendarEvent:
    def __init__(self, start_time, end_time, date, timezone):
        """
        Initialization method for TimeChunk
        Args:
            start_time: a string, start time of one event
            end_time: a string, end time of one event
            date: a string, date of one event
            timezone: a string, indicates the timezone of event
        """
        self._start = start_time
        self._end = end_time
        self._date = date
        self._timezone = timezone

    def __repr__(self):
        return "start: " + self._start + \
               " end: " + self._end + \
               " on: " + self._date + \
               " timezone:" + self._timezone

    def __sub__(self, other):
        return

    def __cmp__(self, other):
        return

    def exclusive(self):
        return

    def overlap(self, other):
        
        return