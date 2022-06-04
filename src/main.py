from .constants import (MUSIC, PODCAST, VIDEO,
                        RENEWAL_REMINDER, FREE, PERSONAL, PREMIUM, )

from .utils import get_reminder_date


class Subscription:

    def __init__(self, subscription_date, category, plan):
        self.subscription_date = subscription_date
        self.category = category
        self.plan = plan
        self.Fee()
        self.renewal_reminder()

    def Fee(self):
        raise NotImplementedError

    def renewal_reminder(self):
        if self.plan == FREE:
            self.reminder_date = get_reminder_date(self.subscription_date, 1, 10)
        if self.plan == PERSONAL:
            self.reminder_date = get_reminder_date(self.subscription_date, 1, 10)
        if self.plan == PREMIUM:
            self.reminder_date = get_reminder_date(self.subscription_date, 3, 10)

    def __repr__(self):
        return f"{RENEWAL_REMINDER} {self.category} {self.reminder_date}"


class Music(Subscription):
    """Class for Music"""

    def Fee(self):
        if self.plan == FREE:
            self.fee = 0
        if self.plan == PERSONAL:
            self.fee = 100
        if self.plan == PREMIUM:
            self.fee = 250

    def __str__(self):
        return "Music"


class Video(Subscription):
    """Class for Video"""

    def Fee(self):
        if self.plan == FREE:
            self.fee = 0
        if self.plan == PERSONAL:
            self.fee = 200
        if self.plan == PREMIUM:
            self.fee = 500

    def __str__(self):
        return "Video"


class Podcast(Subscription):
    """Class for Podcasts"""

    def Fee(self):
        if self.plan == FREE:
            self.fee = 0
        if self.plan == PERSONAL:
            self.fee = 100
        if self.plan == PREMIUM:
            self.fee = 300

    def __str__(self):
        return "Podcast"


# construct Subscription
def construct_subscription(cls, sub_date, category, plan):
    sub = cls(sub_date, category, plan)
    sub.Fee()
    sub.renewal_reminder()

    return sub


cls_dict = {
    MUSIC: Music,
    PODCAST: Podcast,
    VIDEO: Video
}