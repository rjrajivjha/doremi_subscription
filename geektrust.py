from sys import argv

from src.constants import (START_SUBSCRIPTION, ADD_SUBSCRIPTION, ADD_TOP_UP,
                           PRINT_RENEWAL_DETAILS, SUBSCRIPTIONS_NOT_FOUND,
                           RENEWAL_AMOUNT, INVALID_DATE, ADD_TOP_UP_FAILED,
                           ADD_SUBSCRIPTION_FAILED)
from src.main import (construct_subscription, cls_dict)
from src.utils import top_ups_dict, validate_date, add_top_up


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


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    try:
        subscriptions = {}
        top_ups = 0
        cost = 0
        file_path = argv[1]
        f = open(file_path, 'r')
        Lines = f.readlines()
        subscription_start_date = None

        for line in Lines:
            command, *args = line.strip().split(' ')

            if command == START_SUBSCRIPTION:
                subscription_start_date = validate_date(args[0])
                continue

            if subscription_start_date is None and command != PRINT_RENEWAL_DETAILS:
                if command == ADD_SUBSCRIPTION:
                    print(f'{ADD_SUBSCRIPTION_FAILED} {INVALID_DATE}')
                else:
                    print(f'{ADD_TOP_UP_FAILED} {INVALID_DATE}')
                continue

            if command == ADD_SUBSCRIPTION:
                add_sub(args[0], args[1], subscriptions, subscription_start_date)

            if command == ADD_TOP_UP and subscription_start_date:
                if top_ups:
                    print("ADD_TOPUP_FAILED DUPLICATE_TOPUP")
                else:
                    top_ups += add_top_up(top_ups_dict[args[0]], int(args[1]), subscriptions)

            if command == PRINT_RENEWAL_DETAILS:
                if subscriptions:
                    for key, subscription in subscriptions.items():
                        print(subscription.__repr__())
                        cost += subscription.fee
                    cost += top_ups
                    print(f'{RENEWAL_AMOUNT} {cost}')
                else:
                    print(f'{SUBSCRIPTIONS_NOT_FOUND}')

    except FileNotFoundError:
        print("File Not Found. please correct file path.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
