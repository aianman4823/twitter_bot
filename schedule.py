from apscheduler.schedulers.blocking import BlockingScheduler
import autolike
import autoretweet
import removefollow


def timed_job():
    autolike.liketweet()
    autoretweet.autoretweet()

def retweet_job():
    autoretweet.autoretweet()

def remove_job():
    removefollow.remove()


if __name__=="__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(timed_job, 'interval',days=1)
    scheduler.add_job(retweet_job,'interval',hour=12)
    scheduler.add_job(remove_job,'interval',weeks=1)

    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass


