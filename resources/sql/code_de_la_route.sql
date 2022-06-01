-- Create a table that will contain information about all the tests
CREATE TABLE IF NOT EXISTS code_de_la_route (
   id INTEGER PRIMARY KEY NOT NULL,
   platforme TEXT NOT NULL, -- envoituresimone.com , codedelaroute.fr, etc
   theme TEXT,
   series INTEGER, -- usager , securite, etc
   question_number INTEGER,
   question TEXT NOT NULL,
   contain_media BOOLEAN NOT NULL, -- true or false
   media_type TEXT, -- IMAGE, AUDIO, VIDEO
   media_name TEXT, -- Name of the media (ex: 1.1.jpeg, 3.10.mp4, etc)
   media_source TEXT, -- The name of the resource that will be searched in the computer
   options TEXT NOT NULL, -- The option that the user must choose
   multiple_answeres BOOLEAN, -- True if there are multiple answeres
   answere TEXT NOT NULL, -- A Text that answere the question
   explanation TEXT, -- the explanation of the answere
   last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP);