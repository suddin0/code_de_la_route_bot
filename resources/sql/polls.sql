-- Create a table that will contain newly created polls
CREATE TABLE polls(
   id INTEGER PRIMARY KEY NOT NULL,
   is_series BOOLEAN NOT NULL, -- if it is part of a series
   series_id TEXT, -- if part of a series then a unique id
   question_id INTEGER NOT NULL, -- the id of the question from `code_de_la_route` table
   chat_id INTEGER NOT NULL, -- id of the chat
   message_id INTEGER NOT NULL, -- id of the specific message containing the question
   poll_id INTEGER NOT NULL, -- unique id of poll
   last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
