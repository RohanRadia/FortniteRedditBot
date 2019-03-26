import praw
import configparser
# import requests
import json
from FortniteAPI import Stats
from FortniteAPI import User

config = configparser.ConfigParser()
config.read('config.ini')

reddit = praw.Reddit(client_id = config['REDDIT']['CLIENT_ID'],
                     client_secret = config['REDDIT']['CLIENT_SECRET'],
                     username = config['REDDIT']['USERNAME'],
                     password = config['REDDIT']['PASSWORD'],
                     user_agent = config['REDDIT']['USER_AGENT'])

subreddit = reddit.subreddit('FortNiteBR')
keyphrase = '!fnbot '

# username = 'ARK LootReaper'
# print(Stats(User(username).id).keyboard.overall.kd)

for comment in subreddit.stream.comments():
    if comment.body[:7] == '!fnbot ':
        query = comment.body.replace(keyphrase, '')
        try:
            input, gamemode, username = query.split(' ', 2)

            if input.lower() == 'keyboard':
                if gamemode.lower() == 'overall':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).keyboard.overall.wins}\nKills|{Stats(User(username).id).keyboard.overall.kills}\nWinrate|{format(Stats(User(username).id).keyboard.overall.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).keyboard.overall.kd, '.2f')}")
                elif gamemode.lower() == 'solos' or gamemode.lower() == 'solo':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).keyboard.solo.wins}\nKills|{Stats(User(username).id).keyboard.solo.kills}\nWinrate|{format(Stats(User(username).id).keyboard.solo.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).keyboard.solo.kd, '.2f')}")
                elif gamemode.lower() == 'duos' or gamemode.lower() == 'duo':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).keyboard.duo.wins}\nKills|{Stats(User(username).id).keyboard.duo.kills}\nWinrate|{format(Stats(User(username).id).keyboard.duo.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).keyboard.duo.kd, '.2f')}")
                elif gamemode.lower() == 'squads' or gamemode.lower() == 'squad':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).keyboard.squad.wins}\nKills|{Stats(User(username).id).keyboard.squad.kills}\nWinrate|{format(Stats(User(username).id).keyboard.squad.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).keyboard.squad.kd, '.2f')}")
            elif input.lower() == 'controller':
                if gamemode.lower() == 'overall':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).controller.overall.wins}\nKills|{Stats(User(username).id).controller.overall.kills}\nWinrate|{format(Stats(User(username).id).controller.overall.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).controller.overall.kd, '.2f')}")
                elif gamemode.lower() == 'solos' or gamemode.lower() == 'solo':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).controller.solo.wins}\nKills|{Stats(User(username).id).controller.solo.kills}\nWinrate|{format(Stats(User(username).id).controller.solo.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).controller.solo.kd, '.2f')}")
                elif gamemode.lower() == 'duos' or gamemode.lower() == 'duo':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).controller.duo.wins}\nKills|{Stats(User(username).id).controller.duo.kills}\nWinrate|{format(Stats(User(username).id).controller.duo.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).controller.duo.kd, '.2f')}")
                elif gamemode.lower() == 'squads' or gamemode.lower() == 'squad':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).controller.squad.wins}\nKills|{Stats(User(username).id).controller.squad.kills}\nWinrate|{format(Stats(User(username).id).controller.squad.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).controller.squad.kd, '.2f')}")
            elif input.lower() == 'touch':
                if gamemode.lower() == 'overall':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).touch.overall.wins}\nKills|{Stats(User(username).id).touch.overall.kills}\nWinrate|{format(Stats(User(username).id).touch.overall.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).touch.overall.kd, '.2f')}")
                elif gamemode.lower() == 'solos' or gamemode.lower() == 'solo':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).touch.solo.wins}\nKills|{Stats(User(username).id).touch.solo.kills}\nWinrate|{format(Stats(User(username).id).touch.solo.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).touch.solo.kd, '.2f')}")
                elif gamemode.lower() == 'duos' or gamemode.lower() == 'duo':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).touch.duo.wins}\nKills|{Stats(User(username).id).touch.duo.kills}\nWinrate|{format(Stats(User(username).id).touch.duo.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).touch.duo.kd, '.2f')}")
                elif gamemode.lower() == 'squads' or gamemode.lower() == 'squad':
                    comment.reply(f"Username|{username}\n-|-|-\nInput Type|{input.title()}\nGamemode|{gamemode.title()}\nWins|{Stats(User(username).id).touch.squad.wins}\nKills|{Stats(User(username).id).touch.squad.kills}\nWinrate|{format(Stats(User(username).id).touch.squad.winrate, '.2f')}%\nKD|{format(Stats(User(username).id).touch.squad.kd, '.2f')}")
                else:
                    comment.reply(f"We have hit an error - You have incorrectly entered the gamemode. To see lifetime stats choose `overall` as the gamemode option!\n Command Format: `!fnbot <keyboard/controller/touch> <solo/duo/squad/overall> <username>`\nPlease choose one of the options in each of the `<>` and for the final bracker input your `Fortnite Username`!")
            else:
                comment.reply(f"We have hit an error - You have incorrectly entered your platform/input device!\n Command Format: `!fnbot <keyboard/controller/touch> <solo/duo/squad/overall> <username>`\nPlease choose one of the options in each of the `<>` and for the final bracker input your `Fortnite Username`!")
        except:
            comment.reply(f"We have hit an error - this could be caused by many different problems, the most likley is that you have run the command wrong or incorrectly entered the text!\n Command Format: `!fnbot <keyboard/controller/touch> <solo/duo/squad/overall> <username>`\nPlease choose one of the options in each of the `<>` and for the final bracker input your `Fortnite Username`!")
            print('Error!')
