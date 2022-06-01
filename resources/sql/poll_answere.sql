-- Create a table that will contain poll answeres
CREATE TABLE poll_answere (
   id INTEGER PRIMARY KEY NOT NULL,
   poll_id INTEGER NOT NULL, -- id of the chat
   user_id INTEGER NOT NULL, -- usager unique id
   poll_answere_index TEXT NOT NULL, -- The index number of the answered provided
   last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);