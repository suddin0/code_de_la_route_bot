-- Create a table that will contain information about users and their scores
CREATE TABLE exercice(
   id INTEGER PRIMARY KEY NOT NULL,
   is_series BOOLEAN NOT NULL, -- if it is part of a series
   series_id TEXT, -- if part of a series then a unique id
   question_id INTEGER NOT NULL, -- the id of the question from `code_de_la_route` table
   chat_id INTEGER NOT NULL, -- id of the chat
   message_id INTEGER NOT NULL, -- id of the specific message containing the question
   user_id INTEGER NOT NULL, -- usager unique id
   last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
