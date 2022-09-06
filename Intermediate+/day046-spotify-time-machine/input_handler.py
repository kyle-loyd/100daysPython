import datetime as dt

DATE_PROMPT_TEXT = "Enter the date you wish to travel to (YYYY-MM-DD): "


def prompt_for_date():
    while True:
        input_string = input(DATE_PROMPT_TEXT)
        try:
            split_input_string = input_string.split('-')
            year = int(split_input_string[0])
            month = int(split_input_string[1])
            day = int(split_input_string[2])
            input_date = dt.date(year, month, day)
            if input_date > dt.datetime.now().date():
                raise InvalidFutureDateError()
            return input_date
        except ValueError:
            print("Value entered was not valid.  Please try again.")
        except InvalidFutureDateError:
            print("Value entered was in the future.  Please try again.")


class InvalidFutureDateError(Exception):
    pass
