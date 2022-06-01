
from socket import create_connection
import sqlite3
import logging
from constants import DB_NAME, QUERY_ADD_POLL, QUERY_ADD_POLL_ANSWERE, QUERY_GET_POLL_ANSWERE_BY_USER_ID, QUERY_GET_POLL_BY_ID, QUERY_GET_QUESTION_BY_ID, QUERY_RANDOM_QUESTION, QUERY_RANDOM_SERIES
from utils import array_to_question_dict, data_to_poll_dict


class Database:
    def __init__(self) -> None:
        self.con = None
        self.cur = None
    
    def create_connection(self):
        if(self.con !=  None and self.cur != None):
            self.close_connection()
        
        try:
            self.con = sqlite3.connect(DB_NAME)
            self.cur = self.con.cursor()
            return True
        except Exception as error:
            logging.exception("While connecting to Database : ", error)
            self.con = None
            self.cur = None
            return False
    
    def close_connection(self):
        if (self.con == None):
            return
        self.con.close()
        self.con = None
        self.cur = None
    
    def get_random_question(self):
        if(self.create_connection() == False):
            return None
        
        res = self.cur.execute(QUERY_RANDOM_QUESTION).fetchall()

        ## Verify the number of object retrieved
        if (len(res) != 1):
            logging.error("Error recovering `random question`, the size is not 1 : ", len(res))
            return None

        question = array_to_question_dict(res[0])
        if(question == None):
            logging.error("Could not convert the question `tuple` to `array`")
            return None
        
        self.con.commit()
        self.close_connection()
        return question
    
    def get_question_by_id(self, id):
        if(self.create_connection() == False):
            return None
        
        res = self.cur.execute(QUERY_GET_QUESTION_BY_ID, (id,)).fetchall()

        ## Verify the number of object retrieved
        if (len(res) != 1):
            logging.error("Error recovering `random question`, the size is not 1 : ", len(res))
            return None

        question = array_to_question_dict(res[0])
        if(question == None):
            logging.error("Could not convert the question `tuple` to `array`")
            return None
        
        self.con.commit()
        self.close_connection()
        return question


    def get_series(self, series_number):
        if(self.create_connection() == False):
            return None

    def get_random_series(self):
        if(self.create_connection() == False):
            return None
        
        question_list = []
        
        ## Get the list of question for a random series
        res = self.cur.execute(QUERY_RANDOM_SERIES).fetchall()
        # print("Resilt for a random series : ", len(res))

        ## Verify the number of object retrieved
        if (len(res) < 1):
            logging.error("Error recovering `random question`, the size is not greater then 0 : ", len(res))
            return None
        
        ## Parse all the question from the `res` list and put in a list
        for question in res:
            parsed_question = array_to_question_dict(question)
            if(question == None):
                logging.error("Could not convert the question `tuple` to `array`")
                return None
            else:
                question_list.append(parsed_question)

        self.con.commit()
        self.close_connection()
        # return question
        return question_list

    def add_poll(self, is_series=None, series_id=None, question_id=None, chat_id=None, message_id=None, poll_id=None):
        query = ""
        
        if(is_series==None or series_id==None or question_id==None or chat_id==None or message_id==None or poll_id==None):
            logging.error("Error : add_poll : one or more of the parameters are of type `None`!")
            return (None)

        if(self.create_connection() == False):
            return None
        
        ## Build the query and execute it
        self.cur.execute(QUERY_ADD_POLL, (is_series, series_id, question_id, chat_id, message_id, poll_id))
        self.con.commit()

        lastrowid = self.cur.lastrowid
        self.close_connection()
        # return question
        return lastrowid

    def add_poll_answere(self, poll_id=None, user_id=None, poll_answere_index=None):
        query = ""
        
        if(poll_id==None or user_id==None or poll_answere_index==None):
            logging.error("Error : add_poll_answere : one or more of the parameters are of type `None`!")
            return (None)

        if(self.create_connection() == False):
            return None
        
        ## Build the query and execute it
        self.cur.execute(QUERY_ADD_POLL_ANSWERE, (poll_id, user_id, poll_answere_index))
        self.con.commit()

        lastrowid = self.cur.lastrowid
        self.close_connection()
        # return question
        return lastrowid

    def get_poll_by_poll_id(self, poll_id=None):
        query = ""
        
        if(poll_id==None):
            logging.error("Error : poll_id : is of type `None`!")
            return (None)

        if(self.create_connection() == False):
            return None
        
        ## Build the query and execute it
        self.cur.execute(QUERY_GET_POLL_BY_ID, (poll_id,))
        res = self.cur.fetchall()

        ## Verify the number of object retrieved
        if (len(res) != 1):
            logging.error("Error recovering `poll by id {poll_id}`, the size is not 1 : ".format(poll_id=poll_id), len(res))
            return None

        self.close_connection()
        # return question
        return data_to_poll_dict(res[0])
    
    def get_poll_answere_by_user_id(self, user_id=None, poll_id=None):
        query = ""
        
        if(user_id==None or poll_id==None):
            logging.error("Error : user_id or poll_id : is of type `None`!")
            return (None)

        if(self.create_connection() == False):
            return None
        
        ## Build the query and execute it
        self.cur.execute(QUERY_GET_POLL_ANSWERE_BY_USER_ID, (user_id, poll_id))
        res = self.cur.fetchall()

        ## Verify the number of object retrieved
        if (len(res) != 1):
            logging.error("Error recovering `poll answere by id {poll_id}`, the size is not 1 : ".format(poll_id=poll_id), len(res))
            return None

        self.close_connection()
        # return question
        return res

    def update_user_score(self, user_id=None, poll_id=None, option_ids=None):
        query = ""
        
        if(user_id==None or poll_id==None or option_ids==None):
            logging.error("Error : user_id or poll_id or option_ids : is of type `None`!")
            return (None)

        if(self.create_connection() == False):
            return None
        
        ## Build the query and execute it
        self.cur.execute(QUERY_GET_POLL_ANSWERE_BY_USER_ID, (user_id, poll_id))
        res = self.cur.fetchall()

        ## Verify the number of object retrieved
        if (len(res) != 1):
            logging.error("Error recovering `poll answere by id {poll_id}`, the size is not 1 : ".format(poll_id=poll_id), len(res))
            return None

        self.close_connection()
        # return question
        return res