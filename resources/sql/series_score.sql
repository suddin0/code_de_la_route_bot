-- Create a table that will contain poll score
CREATE TABLE series_score (
   id INTEGER PRIMARY KEY NOT NULL,
   series_id TEXT, -- if part of a series then a unique id
   chat_id INTEGER NOT NULL, -- id of the chat
   user_id INTEGER NOT NULL, -- usager unique id
   score INTEGER NOT NULL, -- number of answere that are correct
   questions_answered INTEGER NOT NULL, -- number of question answered
   last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
