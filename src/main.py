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

    def Amount(self):
        raise NotImplementedError

    def renewal_reminder(self):
        if self.plan == FREE:
            self.reminder_date = self.get_reminder_date(self.subscription_date, self.month, self.offset_days)
        if self.plan == PERSONAL:
            self.reminder_date = self.get_reminder_date(self.subscription_date, self.month, self.offset_days)
        if self.plan == PREMIUM:
            self.reminder_date = self.get_reminder_date(self.subscription_date, self.month, self.offset_days)

    def __repr__(self):
        return f"{RENEWAL_REMINDER} {self.category} {self.reminder_date.strftime('%d-%m-%Y')}"


class Music(Subscription):
    """Class for Music"""

    def Amount(self):
        if self.plan == FREE:
            self.amount = 0
            self.month = 1
        if self.plan == PERSONAL:
            self.amount = 100
            self.month = 1
        if self.plan == PREMIUM:
            self.amount = 250
            self.month = 3

    def __str__(self):
        return "Music"


class Video(Subscription):
    """Class for Video"""

    def Amount(self):
        if self.plan == FREE:
            self.amount = 0
            self.month = 1
        if self.plan == PERSONAL:
            self.amount = 200
            self.month = 1
        if self.plan == PREMIUM:
            self.amount = 500
            self.month = 3

    def __str__(self):
        return "Video"


class Podcast(Subscription):
    """Class for Podcasts"""

    def Amount(self):
        if self.plan == FREE:
            self.amount = 0
            self.month = 1
        if self.plan == PERSONAL:
            self.amount = 100
            self.month = 1
        if self.plan == PREMIUM:
            self.amount = 300
            self.month = 3

    def __str__(self):
        return "Podcast"


cls_dict = {
    MUSIC: Music,
    PODCAST: Podcast,
    VIDEO: Video
}
