from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")

        today = datetime.today()

        delta = today - given_date
        return delta.days
    except ValueError:
        return "Невірний формат дати"

result = get_days_from_today("2021-10-09")
print(result)
