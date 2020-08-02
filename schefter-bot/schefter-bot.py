import requests
import json
import os
import random
from apscheduler.schedulers.blocking import BlockingScheduler
# from ff_espn_api import League

class GroupMeException(Exception):
    pass

class SlackException(Exception):
    pass

class DiscordException(Exception):
    pass

class GroupMeBot(object):
    #Creates GroupMe Bot to send messages
    def __init__(self, bot_id):
        self.bot_id = bot_id

    def __repr__(self):
        return "GroupMeBot(%s)" % self.bot_id

    def send_message(self, text):
        #Sends a message to the chatroom
        template = {
                    "bot_id": self.bot_id,
                    "text": text,
                    "attachments": []
                    }

        headers = {'content-type': 'application/json'}

        if self.bot_id not in (1, "1", ''):
            r = requests.post("https://api.groupme.com/v3/bots/post",
                              data=json.dumps(template), headers=headers)
            if r.status_code != 202:
                raise GroupMeException('Invalid BOT_ID')

            return r

def random_phrase():
    phrases = ['Well, Ive got a few things for you',
                'reporting',
                '*looks down at phone*'
              ]
    return random.choice(phrases)


def bot_main(function):
    try:
        bot_id = os.environ["BOT_ID"]
    except KeyError:
        bot_id = 1

    league_id = os.environ["LEAGUE_ID"]

    try:
        year = int(os.environ["LEAGUE_YEAR"])
    except KeyError:
        year=2020

    try:
        swid = os.environ["SWID"]
    except KeyError:
        swid='{1}'

    if swid.find("{",0) == -1:
        swid = "{" + swid
    if swid.find("}",-1) == -1:
        swid = swid + "}"

    try:
        espn_s2 = os.environ["ESPN_S2"]
    except KeyError:
        espn_s2 = '1'

    bot = GroupMeBot(bot_id)
    # if swid == '{1}' and espn_s2 == '1':
    #     league = League(league_id, year)
    # else:
    #     league = League(league_id, year, espn_s2=espn_s2, swid=swid)

    test = False
    if test:
        bot.send_message("Testing")
        bot.send_message("" + random_phrase())

    # text = ''
    # if function=="get_matchups":
    #     text = get_matchups(league)
    #     text = text + "\n\n" + get_projected_scoreboard(league)
    # elif function=="get_scoreboard_short":
    #     text = get_scoreboard_short(league)
    #     text = text + "\n\n" + get_projected_scoreboard(league)
    # elif function=="get_projected_scoreboard":
    #     text = get_projected_scoreboard(league)
    # elif function=="get_close_scores":
    #     text = get_close_scores(league)
    # elif function=="get_power_rankings":
    #     text = get_power_rankings(league)
    # elif function=="get_trophies":
    #     text = get_trophies(league)
    # elif function=="get_final":
    #     # on Tuesday we need to get the scores of last week
    #     week = league.current_week - 1
    #     text = "Final " + get_scoreboard_short(league, week=week)
    #     text = text + "\n\n" + get_trophies(league, week=week)
    if function=="init":
        try:
            text = os.environ["INIT_MSG"]
        except KeyError:
            #do nothing here, empty init message
            pass
    else:
        text = "Something happened. HALP"

    if text != '' and not test:
        bot.send_message(text)

    if test:
        #print "get_final" function
        print(text)


if __name__ == '__main__':
    try:
        ff_start_date = os.environ["START_DATE"]
    except KeyError:
        ff_start_date='2020-09-04'

    try:
        ff_end_date = os.environ["END_DATE"]
    except KeyError:
        ff_end_date='2020-12-30'

    try:
        my_timezone = os.environ["TIMEZONE"]
    except KeyError:
        my_timezone='America/New_York'

    game_timezone='America/New_York'
    bot_main("init")
    sched = BlockingScheduler(job_defaults={'misfire_grace_time': 15*60})

    # #power rankings:                     tuesday evening at 6:30pm local time.
    # #matchups:                           thursday evening at 7:30pm east coast time.
    # #close scores (within 15.99 points): monday evening at 6:30pm east coast time.
    # #trophies:                           tuesday morning at 7:30am local time.
    # #score update:                       friday, monday, and tuesday morning at 7:30am local time.
    # #score update:                       sunday at 4pm, 8pm east coast time.

    # sched.add_job(bot_main, 'cron', ['get_power_rankings'], id='power_rankings',
    #     day_of_week='tue', hour=18, minute=30, start_date=ff_start_date, end_date=ff_end_date,
    #     timezone=my_timezone, replace_existing=True)
    # sched.add_job(bot_main, 'cron', ['get_matchups'], id='matchups',
    #     day_of_week='thu', hour=19, minute=30, start_date=ff_start_date, end_date=ff_end_date,
    #     timezone=game_timezone, replace_existing=True)
    # sched.add_job(bot_main, 'cron', ['get_close_scores'], id='close_scores',
    #     day_of_week='mon', hour=18, minute=30, start_date=ff_start_date, end_date=ff_end_date,
    #     timezone=game_timezone, replace_existing=True)
    # sched.add_job(bot_main, 'cron', ['get_final'], id='final',
    #     day_of_week='tue', hour=7, minute=30, start_date=ff_start_date, end_date=ff_end_date,
    #     timezone=my_timezone, replace_existing=True)
    # sched.add_job(bot_main, 'cron', ['get_scoreboard_short'], id='scoreboard1',
    #     day_of_week='fri,mon', hour=7, minute=30, start_date=ff_start_date, end_date=ff_end_date,
    #     timezone=my_timezone, replace_existing=True)
    # sched.add_job(bot_main, 'cron', ['random_phrase'], id='random_phrase',
    #     day_of_week='sun', hour='15,42', start_date=ff_start_date, end_date=ff_end_date,
    #     timezone=game_timezone, replace_existing=True)

    print("Ready!")
    sched.start()
