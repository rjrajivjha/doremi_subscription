from sys import argv

from src.constants import (START_SUBSCRIPTION, ADD_SUBSCRIPTION, ADD_TOP_UP,
                           PRINT_RENEWAL_DETAILS, INVALID_DATE, ADD_TOP_UP_FAILED,
                           ADD_SUBSCRIPTION_FAILED, ARGUMENTS_LENGTH)
from src.utils import top_ups_dict, validate_date, add_top_up, print_renewal_details, add_sub


def process_add_subscription(category, plan, subscriptions, subscription_start_date):
    if not subscription_start_date:
        print(f'{ADD_SUBSCRIPTION_FAILED} {INVALID_DATE}')
        return
    add_sub(category, plan, subscriptions, subscription_start_date)


def process_add_top_up(name, month, subscriptions, top_ups, subscription_start_date):
    if subscription_start_date is None:
        print(f'{ADD_TOP_UP_FAILED} {INVALID_DATE}')
        return 0

    if top_ups:
        print("ADD_TOPUP_FAILED DUPLICATE_TOPUP")
        return 0

    top_ups += add_top_up(top_ups_dict[name], int(month), subscriptions)
    return top_ups


def process_Lines(Lines):
    subscriptions = {}
    top_ups = 0
    subscription_start_date = None
    for line in Lines:
        command, *args = line.strip().split(' ')

        if command == START_SUBSCRIPTION:
            subscription_start_date = validate_date(args[0])
            continue

        if command == ADD_SUBSCRIPTION:
            process_add_subscription(args[0], args[1], subscriptions, subscription_start_date)
            continue

        if command == ADD_TOP_UP:
            top_ups += process_add_top_up(args[0], args[1], subscriptions, top_ups, subscription_start_date)
            continue

        if command == PRINT_RENEWAL_DETAILS:
            print_renewal_details(subscriptions, top_ups)
            continue


def open_file(file_path='sample_input/input2.txt'):
    f = open(file_path, 'r')
    Lines = f.readlines()
    process_Lines(Lines)


def main():
    if len(argv) != ARGUMENTS_LENGTH:
        raise Exception("File path not entered")
    try:
        file_path = argv[1]
        open_file(file_path)
    except FileNotFoundError:
        print("File Not Found. please correct file path.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
