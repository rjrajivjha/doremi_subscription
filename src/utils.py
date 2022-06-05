import datetime
from .constants import (FOUR_DEVICE, TEN_DEVICE, INVALID_DATE,
                        RENEWAL_AMOUNT, SUBSCRIPTIONS_NOT_FOUND,
                        CHARGE_FOUR_DEVICE, CHARGE_TEN_DEVICE,
                        MIN_SUB_REQD_FOR_TOP_UP)
from .main import cls_dict

top_ups_dict = {
    FOUR_DEVICE: CHARGE_FOUR_DEVICE,
    TEN_DEVICE: CHARGE_TEN_DEVICE,
}


def validate_date(date_text):
    try:
        date = datetime.datetime.strptime(date_text, '%d-%m-%Y')
        return date.date()
    except ValueError:
        print(INVALID_DATE)


def add_top_up(cost, month, subscriptions):
    if len(subscriptions) >= MIN_SUB_REQD_FOR_TOP_UP:
        return cost * month
    else:
        print("ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND")


# construct Subscription
def construct_subscription(cls, sub_date, category, plan):
    sub = cls(sub_date, category, plan)
    sub.Amount()
    sub.renewal_reminder()

    return sub


def add_sub(category, plan, subscriptions, subscription_start_date):
    category = category
    plan = plan
    if category not in subscriptions:
        subscriptions[category] = construct_subscription(
            cls_dict[category],
            subscription_start_date,
            category, plan)
    else:
        print("ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY ")


def print_renewal_details(subscriptions, top_ups, cost=0):
    if subscriptions:
        for key, subscription in subscriptions.items():
            print(subscription.__repr__())
            cost += subscription.amount
        cost += top_ups
        print(f'{RENEWAL_AMOUNT} {cost}')
    else:
        print(f'{SUBSCRIPTIONS_NOT_FOUND}')
