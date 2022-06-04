import datetime

from dateutil.relativedelta import relativedelta

from .constants import FOUR_DEVICE, TEN_DEVICE, INVALID_DATE

top_ups_dict = {
    FOUR_DEVICE: 50,
    TEN_DEVICE: 100,
}


def validate_date(date_text):
    try:
        date = datetime.datetime.strptime(date_text, '%d-%m-%Y')
        return date.date()
    except ValueError:
        raise ValueError(INVALID_DATE)


def add_top_up(cost, month, subscriptions):
    if len(subscriptions) >= 1:
        return cost * month
    else:
        print("ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND")
        return 0


def get_reminder_date(date, month=1, day=10):
    return date + relativedelta(months=month) - relativedelta(days=day)
