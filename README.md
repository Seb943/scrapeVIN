# scrapeVIN <br />
:new::new::new:A python package for scraping vinted.fr :new::new::new:<br />
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
unofficial VINTED API for Python 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For the moment, the package is only working on the French website, international versions coming soon. :soon: <br /><br />
:uk: <br />
Vinted is a Lithuanian online marketplace and community that allows its users to sell, buy, and swap secondhand clothing items and accessories [1]. Due to its large and increasing amount of users accross multiple countries, it is also a tremendous source of information concerning reselling prices according to multiple factors such as items condition, colors, sizes, and so on. One could be interested in data analysis towards this database for multiple reasons, such as educational purposes, buy/resell strategies, or even just to appreciate the correct price for buying or selling any specific article. This python package was developed in order to being able to make research on the website, to collect the research pages and finally store the data in a comprehensive csv format. 
Functionalities : 
- Research by query (e.g. 'Air Force One')
- Add multiple filters : size, color, catalog, order the research (most recent first, increasing price, decreasing price, relevance)
- Decide where to stop the research. One can decide until which page you want the program to collect data 
- The package was designed for the french website, however the website architecture is the same for all countries, so one can easily adapt the existing code for any specific language (just need to change a few words in the functions.py code) ---> international versions coming soon!
- Interactive version : just let the program ask you the filter you want to input <br />

:fr: <br />
Vinted est un marché en ligne communautaire qui permet à ses utilisateurs de vendre, d'acheter, et d'échanger des vêtements et accessoires d'occasion [2]. Grâce à son large et croissant nombre d'utilisateurs à travers de nombreux pays, le site recense une quantité fantastique d'information concernant les prix de reventes de milliers d'articles et de vêtements, en fonction de facteurs divers tels que l'état, le coloris, la taille, etc... Nous pourrions être intéressés par l'analyse de ces données dans différents cadres, tels que les travaux académiques (études du comportement, étude de marché, analyse de données brutes), la mise en place de stratégies d'achat/revente, ou encore simplement pour déterminer le prix juste pour acheter ou bien revendre un article. Ce package python a été développé pour faire des recherches sur le site, collecter les données des items de la recherche, et finalement ranger les données dans un format csv facilement exploitable. 
Fonctionnalités : 
- Recherche par requête textuelle (e.g. 'Air Force One')
- Ajout de filtres de recherche : taille, couleur, catalogue, ordre d'apparition (le plus récent d'abord, prix croissant, prix décroissant, pertinence) 
- Choix de la page maximale de recherche (e.g. collecter les données jusqu'à la page 40) 
- Le package a été développé pour la version française du site, toutefois l'architecture du site reste la même pour les autres versions, et il est facile d'adapter le code à ces versions en modifiant quelques passages dans le fichier functions.py. -----> Versions internationales à venir!
- Version interactive : l'utilisateur peut simplement répondre aux questions du programme pour faire la recherche à travers l'API

[1] Vinted Wikipedia EN : https://en.wikipedia.org/wiki/Vinted <br />
[2] Vinted Wikipedia FR : https://fr.wikipedia.org/wiki/Vinted
