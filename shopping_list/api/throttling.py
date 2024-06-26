# shopping_list/api/throttling.py


from rest_framework.throttling import UserRateThrottle


class MinuteRateThrottle(UserRateThrottle):
    scope = "user_minute"


class DailyRateThrottle(UserRateThrottle):
    scope = "user_day"
