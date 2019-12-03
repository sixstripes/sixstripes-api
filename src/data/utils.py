import datetime
from calendar import monthrange


class DatetimeParser:
    def __init__(self, date_str):
        self.date_str = date_str

    def date_range(self):
        date_dict = self._split_date()
        if "day" in date_dict.keys():
            return (
                datetime.date(date_dict["year"], date_dict["month"], date_dict["day"]),
                datetime.date(date_dict["year"], date_dict["month"], date_dict["day"]),
            )

        if "month" in date_dict.keys():
            _, last_day = monthrange(date_dict["year"], date_dict["month"])
            return (
                datetime.date(date_dict["year"], date_dict["month"], 1),
                datetime.date(date_dict["year"], date_dict["month"], last_day),
            )

        return (datetime.date(date_dict["year"], 1, 1), datetime.date(date_dict["year"], 12, 31))

    def _split_date(self):
        splitted_date = self.date_str.split("/")
        date_parts = ["day", "month", "year"]
        date_dict = {
            date_parts[idx + (len(date_parts) - len(splitted_date))]: int(value)
            for idx, value in enumerate(splitted_date)
        }

        return date_dict
