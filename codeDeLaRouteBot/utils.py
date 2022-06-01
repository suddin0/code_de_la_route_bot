from importlib.resources import path
from pathlib import Path
from pprint import pprint
import urllib.parse
import json
from constants import PATH_RESOURCE_DB

def array_to_question_dict(tuple):
    ## Verify if the tuple contains the proper amount of values
    if(len(tuple) < 14):
        print("[-] Error in `array_to_question_dict` : array size is less then 14 : [" + str(len(tuple)) + "] : ", tuple)
        return None

    ## Deconstruct the tuple
    id, platforme, theme, series, question_number, question, contain_media, media_type, media_name, media_source, options, multiple_answeres,answere, explanation, last_update = tuple
    dic = {
        "id" :id,
        "platforme" : urllib.parse.unquote(platforme),
        "theme" :theme,
        "series" :series,
        "question_number" :question_number,
        "question" :urllib.parse.unquote(question),
        "contain_media" : True if contain_media == 1 else False,
        "media_type" :media_type,
        "media_name" : urllib.parse.unquote(media_name),
        "media_source" : urllib.parse.unquote(media_source),
        "options" : json.loads(urllib.parse.unquote(options)),
        "multiple_answeres" : True if multiple_answeres == 1 else False,
        "answere" : urllib.parse.unquote(answere),
        "explanation" : urllib.parse.unquote(explanation),
        "last_update" : last_update,
    }
    return(dic)

def data_to_poll_dict(tuple):
    if(len(tuple) < 8):
        print("[-] Error in `data_to_poll_dict` : array size is less then 8 : [" + str(len(tuple)) + "] : ", tuple)
        return None
    id, is_series, series_id, question_id, chat_id, message_id, poll_id, last_update = tuple
    dic = {
        "id" :id,
        "is_series" : True if is_series == 1 else False,
        "series_id" :series_id,
        "question_id" : question_id,
        "chat_id" : chat_id,
        "message_id" : message_id,
        "poll_id" : poll_id,
        "last_update" : last_update,
    }
    return(dic)

def create_poll_element(dict):
    opt_i = 0
    number_of_correct_options = 0
    correct_option_id = 0
    media_file=None

    poll_option = []
    for option in dict["options"]:
        poll_option.append(option['value'])
        if option['isAnswere'] == True:
            number_of_correct_options += 1
            correct_option_id = opt_i
        opt_i += 1

    if(dict["contain_media"] and len(dict["media_name"]) > 0):
        med_path=Path(PATH_RESOURCE_DB).joinpath(dict["platforme"]).joinpath("series").joinpath(str(dict["series"])).joinpath("media").joinpath(dict["media_name"])
        # print("Media path : ", med_path)
        with open(med_path , "rb") as file:
            media_file=file.read()
    
    poll = {
        "question_db_entry" : dict["id"],
        "question" : dict["question"],
        "options" : poll_option,
        "is_anonymous" : False,
        "type" : "quiz" if number_of_correct_options == 1 else "regular",
        "allows_multiple_answers" : dict["multiple_answeres"],
        "correct_option_id" : correct_option_id,
        "explanation" : "**" + dict["answere"] +  "**\n\n" + dict["explanation"],
        "explanation_parse_mode" : "MARKDOWN",
        "contain_media" : dict["contain_media"],
        "media" : media_file,
        "media_type" : dict["media_type"]
    }
    return poll

def compare_json_question_to_option_index():
    pass

def send_poll(bot, message, poll_question_element):
    media_message = None
    reply_to_media_chat = None

    ## If contains media then send the media first
    if(poll_question_element["contain_media"] == True and poll_question_element["media_type"] == 'image'):
        media_message = bot.send_photo( chat_id=message.chat.id, photo=poll_question_element['media'], disable_notification=True)
    elif(poll_question_element["contain_media"] and poll_question_element["media_type"] == 'video'):
        # media_message = bot.send_document(chat_id=chat_id, photo=poll_question_element['media'],
        media_message = bot.send_photo(chat_id=message.chat.id, photo=poll_question_element['media'], disable_notification=True)
    
    ## If a media was sent then reply to that media so the question belongs to that media
    if(media_message != None and media_message.message_id):
        reply_to_media_chat = media_message.message_id

    return bot.send_poll(
        chat_id=message.chat.id,
        question=poll_question_element["question"],
        options=poll_question_element["options"],
        is_anonymous= poll_question_element["is_anonymous"],
        type=poll_question_element["type"],
        correct_option_id=poll_question_element["correct_option_id"],
        allows_multiple_answers=poll_question_element["allows_multiple_answers"],
        explanation=poll_question_element["allows_multiple_answers"],
        explanation_parse_mode=poll_question_element["explanation_parse_mode"],
        reply_to_message_id=reply_to_media_chat,
        disable_notification=True
        )