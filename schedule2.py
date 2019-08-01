from apscheduler.schedulers.blocking import BlockingScheduler

import autoretweet




def retweet_job():
    autoretweet.autoretweet()



if __name__=="__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(retweet_job,'interval',hour=12)

    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass

