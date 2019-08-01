from apscheduler.schedulers.blocking import BlockingScheduler

import removefollow


def remove_job():
    removefollow.remove()


if __name__=="__main__":
    scheduler = BlockingScheduler()

    scheduler.add_job(remove_job,'interval',weeks=1)

    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass

