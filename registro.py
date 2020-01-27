import random
import time

def check_follow_limit(followed, limit):
    if followed >= limit:
        return True
    return False


def wait_random_time():
    i = random.randint(3,6)
    time.sleep(i)


def printSessionSummary(followed, liked):
    print("Se han seguido {} usuarios y likeado {} tweets durante esta sesion".format(followed, liked))
