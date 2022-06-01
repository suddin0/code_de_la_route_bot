#!/bin/python
import json
import sys
import telebot
import logging
from pprint import pprint
from utils import create_poll_element, send_poll
from constants import PATH_RESOURCE, HELP_TEXT
from db import Database
from pathlib import Path
import time
import secrets

bot=None

# Open the `token` file that contains the bot private token and feed the data to `telebot`
try:
    with open(Path(PATH_RESOURCE).joinpath("token"), "r") as token_file:
        TOKEN=token_file.readline()
        bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
except FileNotFoundError:
    logging.exception("While opening `token` file. File does not exists.")
    sys.exit(1)

@bot.message_handler(commands=['exercice'])
def exercice_handler(message):
    database = Database()
    quest = database.get_random_question()
    poll_element = create_poll_element(quest)
    poll = send_poll(bot, message, poll_element)
    database.add_poll(is_series=False, series_id="", question_id=quest['id'], chat_id=poll.chat.id, message_id=poll.message_id, poll_id=poll.poll.id)



@bot.message_handler(commands=['series'])
def series_handler(message):
    ## Parse the options

    ## If options then

    ### If NO options then use a random series
    # print((str(message)))
    # bot.send_chat_action(chat_id=message.chat.id, action="typing")

    database = Database()
    questions = database.get_random_series()
    series_id = secrets.token_hex(nbytes=32)
    for question in questions:
        pprint(question)
        poll_element = create_poll_element(question)
        poll=send_poll(bot, message, poll_element)
        database.add_poll(
            is_series=True,
            series_id=series_id,
            question_id=poll_element['question_db_entry'],
            chat_id=poll.chat.id,
            message_id=poll.message_id,
            poll_id=poll.poll.id)
        ## Sleep so we do not spam the server
        time.sleep(1)
        


@bot.message_handler(commands=['score'])
def score_handler(message):
    # Verify
    print((str(message)))
    bot.send_chat_action(chat_id=message.chat.id, action="typing")

@bot.poll_answer_handler()
def poll_amswere_handler(poll):
    database = Database()

    # Verify
    # print((str(message)))
    print("Poll Answere :")
    print(json.dumps(poll.option_ids))
    # bot.send_chat_action(chat_id=message.chat.id, action="typing")

    poll_data = database.get_poll_by_poll_id(poll.poll_id)
    poll_answere = database.get_poll_answere_by_user_id(poll.user.id, poll.poll_id)

    pprint(poll_data)
    # If the answere ware to a series then
    if (poll_data["is_series"] == True and len(poll_answere) == 0):
        # Add the answere to the DB
        print("|| The answere is part of a series --")
        database.add_poll_answere(poll.poll_id, poll.user.id, json.dumps(poll.option_ids))
        database.update_user_score(poll.user.id, poll_data["series_id"], poll_data['question_id'])
        # Manage the score depending on the correct answere

@bot.message_handler(commands=['help', 'aide'])
def help_handler(message):
    bot.send_message(chat_id=message.chat.id, text=HELP_TEXT, parse_mode="MARKDOWN",
        disable_web_page_preview=True, disable_notification=True, allow_sending_without_reply=True)

def main():
    # print(" --> ", QUERY_ADD_EXERCICE.format(exercice_table_name=DB_TABLE_EXERCICE, is_series="False", series_id="ABCD", question_id=123, chat_id=123, message_id=123, user_id=1233))
    database = Database()
    # pprint(database.get_question_by_id(2)['options'][0])
    print(database.get_question_by_id(2)['options'][2]['isAnswere'])
    # bot.infinity_polling()
    # pprint(["Random question : ", database.get_random_question()])
    

if __name__ == "__main__":
    main()