import os
from pathlib import Path

DB_TABLE_QUESTION="code_de_la_route"
DB_TABLE_POLLS="polls"
DB_TABLE_POLL_ANSWERE="poll_answere"
DB_TABLE_SERIES_SCORE="series_score"
PATH_ROOT = Path(os.path.dirname(__file__)).parent
PATH_RESOURCE=Path(PATH_ROOT).joinpath("resources")
PATH_RESOURCE_DB=Path(PATH_RESOURCE).joinpath("db")
DB_NAME=Path(PATH_RESOURCE_DB).joinpath("data.db")



## Some predefined messages to send in command
HELP_TEXT="""
Je peux vous aider à apprendre le Code De La route

Vous pouvez utiliser les commandes suivantes:

**/aide ou /help** - Ce message
**/exercice** - Un test random de code de la route
**/series** - Debuter une serie de test
**/notes** - Voir votre notes

Pour plus d'information ou contribution visitez https://github.com/suddin0/code_de_la_route_bot
"""

## Query related
QUERY_RANDOM_QUESTION='SELECT * FROM {question_table_name} ORDER BY RANDOM() LIMIT 1;'.format(question_table_name=DB_TABLE_QUESTION)
QUERY_RANDOM_SERIES='SELECT * FROM {question_table_name} WHERE series IN (SELECT DISTINCT(series) FROM {question_table_name} ORDER BY RANDOM() LIMIT 1);'.format(question_table_name=DB_TABLE_QUESTION)

QUERY_ADD_POLL='INSERT INTO {table_name} (is_series, series_id, question_id, chat_id, message_id, poll_id) VALUES (?, ?, ?, ?, ?, ?)'.format(table_name=DB_TABLE_POLLS)
QUERY_ADD_POLL_ANSWERE='INSERT INTO {table_name} (poll_id, user_id, poll_answere_index) VALUES (?, ?, ?)'.format(table_name=DB_TABLE_POLL_ANSWERE)
QUERY_ADD_SERIES_SCORE='INSERT INTO {table_name} (series_id, chat_id, user_id, score, questions_answered) VALUES (?, ?, ?, ?, ?)'.format(table_name=DB_TABLE_SERIES_SCORE)

QUERY_GET_POLL_BY_ID='SELECT * FROM {table_name} WHERE poll_id=? LIMIT 1;'.format(table_name=DB_TABLE_POLLS)
QUERY_GET_QUESTION_BY_ID='SELECT * FROM {table_name} WHERE id=?;'.format(table_name=DB_TABLE_QUESTION)
QUERY_GET_POLL_ANSWERE_BY_USER_ID='SELECT * FROM {table_name} WHERE user_id=? AND poll_id=?;'.format(table_name=DB_TABLE_POLL_ANSWERE)

QUERY_UPDATE_SCORE='UPDATE ' + DB_TABLE_SERIES_SCORE + ' set score=' + DB_TABLE_SERIES_SCORE + '.score+{score_inc_val}, questions_answered=' + DB_TABLE_SERIES_SCORE + '.questions_answered+1 WHERE user_id=? AND chat_id=?;'

"""
SELECT * FROM code_de_la_route ORDER BY RANDOM() LIMIT 1;
SELECT * FROM code_de_la_route ORDER BY RANDOM() LIMIT 1;
SELECT DISTINCT(series) FROM code_de_la_route ORDER BY RANDOM() LIMIT 1;
SELECT * FROM code_de_la_route WHERE series IN (SELECT DISTINCT(series) FROM code_de_la_route ORDER BY RANDOM() LIMIT 1);
"""