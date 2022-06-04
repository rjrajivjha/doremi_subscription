import datetime
from .constants import FOUR_DEVICE, TEN_DEVICE, INVALID_DATE, RENEWAL_AMOUNT, SUBSCRIPTIONS_NOT_FOUND
from .main import cls_dict

top_ups_dict = {
    FOUR_DEVICE: 50,
    TEN_DEVICE: 100,
}


def validate_date(date_text):
    try:
        date = datetime.datetime.strptime(date_text, '%d-%m-%Y')
        return date.date()
    except ValueError:
        print(INVALID_DATE)


def add_top_up(cost, month, subscriptions):
    if len(subscriptions) >= 1:
        return cost * month
    else:
        print("ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND")
        return 0


# construct Subscription
def construct_subscription(cls, sub_date, category, plan):
    sub = cls(sub_date, category, plan)
    sub.Fee()
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
            cost += subscription.fee
        cost += top_ups
        print(f'{RENEWAL_AMOUNT} {cost}')
    else:
        print(f'{SUBSCRIPTIONS_NOT_FOUND}')
