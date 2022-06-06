from sys import argv

from src.constants import (START_SUBSCRIPTION, ADD_SUBSCRIPTION, ADD_TOP_UP,
                           PRINT_RENEWAL_DETAILS, INVALID_DATE, ADD_TOP_UP_FAILED,
                           ADD_SUBSCRIPTION_FAILED, ARGUMENTS_LENGTH)
from src.utils import top_ups_dict, validate_date, add_top_up, print_renewal_details, add_sub


def process_Lines(Lines):
    subscriptions = {}
    top_ups = 0
    subscription_start_date = None
    for line in Lines:
        command, *args = line.strip().split(' ')

        if command == START_SUBSCRIPTION:
            subscription_start_date = validate_date(args[0])
            continue

        elif subscription_start_date is None and command == ADD_SUBSCRIPTION:
            print(f'{ADD_SUBSCRIPTION_FAILED} {INVALID_DATE}')

        elif subscription_start_date is None and command == ADD_TOP_UP:
            print(f'{ADD_TOP_UP_FAILED} {INVALID_DATE}')

        elif command == ADD_SUBSCRIPTION:
            category = args[0]
            plan = args[1]
            add_sub(category, plan, subscriptions, subscription_start_date)

        elif command == ADD_TOP_UP and subscription_start_date and top_ups:
            print("ADD_TOPUP_FAILED DUPLICATE_TOPUP")

        elif command == ADD_TOP_UP and subscription_start_date and not top_ups:
            top_ups += add_top_up(top_ups_dict[args[0]], int(args[1]), subscriptions)

        elif command == PRINT_RENEWAL_DETAILS:
            print_renewal_details(subscriptions, top_ups)


def main():
    # if len(argv) != ARGUMENTS_LENGTH:
    #     raise Exception("File path not entered")
    try:
        # file_path = argv[1]
        file_path = 'sample_input/input8.txt'
        f = open(file_path, 'r')
        Lines = f.readlines()
        process_Lines(Lines)
    except FileNotFoundError:
        print("File Not Found. please correct file path.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
