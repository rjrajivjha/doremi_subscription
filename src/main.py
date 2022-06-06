from dateutil.relativedelta import relativedelta

from .constants import (MUSIC, PODCAST, VIDEO,
                        RENEWAL_REMINDER, FREE, PERSONAL, PREMIUM, )


class Subscription:
    offset_days = 10

    def __init__(self, subscription_date, category, plan):
        self.subscription_date = subscription_date
        self.category = category
        self.plan = plan
        self.Amount()
        self.renewal_reminder()

    @staticmethod
    def get_reminder_date(date, month=1, day=offset_days):
        return date + relativedelta(months=month) - relativedelta(days=day)

    def renewal_reminder(self):
        self.reminder_date = self.get_reminder_date(self.subscription_date, self.month, self.offset_days)

    def Amount(self):
        self.amount = self.plans_dict[self.plan]['amount']
        self.month = self.plans_dict[self.plan]['month']

    def __repr__(self):
        return f"{RENEWAL_REMINDER} {self.category} {self.reminder_date.strftime('%d-%m-%Y')}"


class Music(Subscription):
    """Class for Music"""
    plans_dict = {
        FREE: {
            'amount': 0,
            'month': 1
        },
        PERSONAL: {
            'amount': 100,
            'month': 1
        },
        PREMIUM: {
            'amount': 250,
            'month': 3
        }
    }

    def __str__(self):
        return "Music"


class Video(Subscription):
    """Class for Video"""

    plans_dict = {
        FREE: {
            'amount': 0,
            'month': 1
        },
        PERSONAL: {
            'amount': 200,
            'month': 1
        },
        PREMIUM: {
            'amount': 500,
            'month': 3
        }
    }

    def __str__(self):
        return "Video"


class Podcast(Subscription):
    """Class for Podcasts"""

    plans_dict = {
            FREE: {
                'amount': 0,
                'month': 1
            },
            PERSONAL: {
                'amount': 100,
                'month': 1
            },
            PREMIUM: {
                'amount': 300,
                'month': 3
            }
        }

    def __str__(self):
        return "Podcast"


cls_dict = {
    MUSIC: Music,
    PODCAST: Podcast,
    VIDEO: Video
}
