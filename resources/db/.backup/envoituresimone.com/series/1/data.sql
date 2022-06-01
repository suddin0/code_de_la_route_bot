CREATE TABLE IF NOT EXISTS code_de_la_route(
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

--
-- Series : 1
--

INSERT INTO code_de_la_route (platforme, theme, series, question_number, question, contain_media, media_type, media_name, media_source, options, multiple_answeres, answere, explanation)
VALUES
('envoituresimone.com', '', 1, 1, 'Des pneus sous-gonflés tiennent mieux la route', true, 'image', '1.1.jpeg', 'https://evs-profilepics.s3.amazonaws.com/production/cdr/images/attachments/000/000/097/medium/00032qA.jpg?1534254365', '[{%22isAnswere%22:false,%22value%22:%22sur sol mouillé%22},{%22isAnswere%22:false,%22value%22:%22lorsque la route est enneigée%22},{%22isAnswere%22:true,%22value%22:%22aucun%22}]', false, 'Les pneus sous-gonflés n%27ont aucun intérêt sur route. Que celle-ci soit sèche, humide ou enneigée. Ils dégradent la tenue de route, et surtout ils subissent plus de déformations. Conséquence : ils s%27échauffent et risquent d%27éclater.', ''),
('envoituresimone.com', '', 1, 2, 'Titulaire du seul permis BEA (boîte de vitesse automatique) uniquement, je suis autorisé à conduire une voiture à boîte de vitesse manuelle', true, 'image', '1.2.jpeg', 'https://evs-profilepics.s3.amazonaws.com/production/cdr/images/attachments/000/000/100/medium/00033qA.jpg?1534254380', '[{%22isAnswere%22:false,%22value%22:%22si je suis en période probatoire%22},{%22isAnswere%22:false,%22value%22:%22si j%27ai 10 ans de permis%22},{%22isAnswere%22:true,%22value%22:%22aucun%22}]', false, 'Le permis B (voitures à embrayage manuel et boîte de vitesse manuelle) permet de conduire une voiture automatique sans condition et sans formalité', 'Mais l%27inverse n%27est pas vrai. Si je suis titulaire du permis BEA, je peux conduire uniquement des voitures à boîtes de vitesses automatiques.

Pour conduire une voiture manuelle, je devrai passer une épreuve supplémentaire du permis de conduire. Même si j%27ai mon permis depuis plus de 10 ans !'),
('envoituresimone.com', '', 1, 3, 'La vitesse est limitée à 30 km/h', true, 'video', '1.3.mp4', 'https://evs-profilepics.s3.amazonaws.com/production/cdr/videos/attachments/000/000/501/large-mp4/00163qA.mp4?1534256887', '[{%22isAnswere%22:true,%22value%22:%22parce que l%27endroit est dangereux%22},{%22isAnswere%22:false,%22value%22:%22parce qu%27il y a des ralentisseurs%22}]', false, 'Ce n%27est pas parce qu%27il y a des ralentisseurs que la vitesse est limitée à 30 km/h ! Il ne faut pas prendre le problème à l%27envers...', 'Si la vitesse est limitée à 30 km/h, c%27est que l%27endroit est dangereux. Il y a certainement très souvent des piétons, et en particulier des enfants dans cette zone. Et s%27il y a des ralentisseurs, c%27est pour s%27assurer que les automobilistes les moins respectueux ralentiront effectivement.'),
('envoituresimone.com', '', 1, 4, 'Après un certain nombre d%27heures éveillé, le jugement, la concentration et les réflexes d%27un conducteur diminuent', true, 'image', '1.4.jpeg', 'https://evs-profilepics.s3.amazonaws.com/production/cdr/images/attachments/000/000/106/medium/00035qA.jpg?1534254407', '[{%22isAnswere%22:true,%22value%22:%22Oui%22},{%22isAnswere%22:false,%22value%22:%22Uniquement s%27il a consommé de l%27alcool%22},{%22isAnswere%22:false,%22value%22:%22Non%22}]', false, 'Tout individu qui a consommé de l%27alcool voit son jugement, sa concentration et ses réflexes diminuer.', 'Mais c%27est aussi le cas avec la fatigue ! Alcool ou non !!!

Voilà pourquoi il est recommandé de prendre le volant uniquement si on est reposé (et pas après une nuit courte ou une longue et difficile journée de travail), surtout pour faire un long trajet, et de faire des pauses. Toutes les 2 heures grand maximum.'),
('envoituresimone.com', '', 1, 5, 'En ville, les piétons les plus touchés dans les accidents mortels sont', true, 'image', '1.5.jpeg', 'https://evs-profilepics.s3.amazonaws.com/production/cdr/images/attachments/000/000/109/medium/00036qA.jpg?1534254421', '[{%22isAnswere%22:false,%22value%22:%22les enfants%22},{%22isAnswere%22:false,%22value%22:%22les 16-25 ans%22},{%22isAnswere%22:true,%22value%22:%22les personnes âgées%22}]', false, 'as', 'as'),
('envoituresimone.com', '', 1, 6, 'Lors d%27une marche arrière, une caméra de recul dispense:', true, 'image', '1.6.jpeg', 'https://evs-profilepics.s3.amazonaws.com/production/cdr/images/attachments/000/000/112/medium/00037qA.jpg?1534254435', '[{%22isAnswere%22:false,%22value%22:%22de regarder dans les rétroviseurs%22},{%22isAnswere%22:false,%22value%22:%22de se retourner%22},{%22isAnswere%22:true,%22value%22:%22Aucun%22}]', false, 'Certains véhicules disposent d%27une caméra de recul. C%27est très pratique : cela permet au conducteur de voir ce qui se passe derrière la voiture, y compris très près. Ce qui est impossible à voir en se retournant ou dans les rétroviseurs', 'Mais attention : le champ de vision d%27une caméra de recul est étroit. Et l%27image, déformée, ne permet pas de bien estimer les distances ou les vitesses.

Ce dispositif complète la vision directe (en se retournant) et dans les rétroviseurs, mais il ne les remplace pas.'),
('envoituresimone.com', '', 1, 7, 'J%27ai plus de risque de rencontrer rapidement une plaque de verglas si:', true, 'image', '1.7.jpeg', 'https://evs-profilepics.s3.amazonaws.com/production/cdr/images/attachments/000/000/115/medium/00038qA.jpg?1534254453', '[{%22isAnswere%22:false,%22value%22:%22je tourne à droite%22},{%22isAnswere%22:true,%22value%22:%22je tourne à gauche%22}]', false, 'Sur le panneau, je remarque un symbole qui concerne uniquement la route qui tourne à gauche. De quoi s%27agit-il ?', 'Il s%27agit de la représentation d%27un pont. Et un pont est l%27endroit idéal pour la formation de verglas puisqu%27il peut se refroidir par le dessus et par le dessous. Et s%27il y a un cours d%27eau à proximité, l%27humidité se transforme rapidement en glace.

Voilà pourquoi, même si la route ne semble pas glissante, il est plus probable de trouver une plaque de verglas si je vais vers ARUDY et OLORON (mais ça n%27exclut pas totalement le risque si je vais à droite !).'),
('envoituresimone.com', '', 1, 8, 'Pour réanimer une victime, je suis autorisé à utiliser un défibrillateur automatique:', true, 'image', '1.8.jpeg', 'https://evs-profilepics.s3.amazonaws.com/production/cdr/images/attachments/000/000/118/medium/00039qA.jpg?1534254470', '[{%22isAnswere%22:true,%22value%22:%22si j%27ai suivi une formation de secouriste%22},{%22isAnswere%22:true,%22value%22:%22si je n%27ai pas suivi cette formation%22}]', true, 'Toute personne est en mesure d%27utiliser un défibrillateur automatique. Inutile d%27être secouriste ou d%27avoir suivi une formation, même si on ne peut que la recommander.', 'L%27utilisation est relativement simple : il suffit de lire la notice (généralement illustrée) et de respecter les consignes... ou d%27écouter. En effet, certains défibrillateurs parlent !

Quand utiliser ce type d%27appareil ? Dès que l%27on pense qu%27une personne est en détresse cardiaque. Il suffit de le mettre en place, et il se charge tout seul du diagnostic et essaie de relancer le coeur si besoin.

Ne pas oublier d%27alerter les secours malgré tout !'),
('envoituresimone.com', '', 1, 9, 'Un conducteur novice est capable', true, 'image', '1.9.jpeg', 'https://evs-profilepics.s3.amazonaws.com/production/cdr/images/attachments/000/000/121/medium/00040qA.jpg?1534254485', '[{%22isAnswere%22:false,%22value%22:%22de déceler tous ces indices en mêmes temps%22},{%22isAnswere%22:false,%22value%22:%22de réagir immédiatement%22},{%22isAnswere%22:true,%22value%22:%22Aucun%22}]', false, 'Entre les panneaux de direction, les voitures qui changent de files, celui qui me suit de trop près et la voiture devant moi qui freine... cela fait beaucoup de choses à surveiller !', 'Personne n%27est capable de traiter instantanément toutes ces informations et de bien réagir à tous les coups.

C%27est d%27autant plus vrai si la vitesse est élevée, que je suis fatigué (ou alcoolisé !), ou que je suis conducteur novice.

La solution ? Ralentir un peu, augmenter les intervalles de sécurité, et anticiper. Les choses deviennent alors beaucoup plus simples.');

