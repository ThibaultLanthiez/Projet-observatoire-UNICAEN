[:arrow_left: Retour vers le portfolio](https://github.com/ThibaultLanthiez/Portfolio)

<img src="https://borea.mnhn.fr/sites/default/files/styles/large/public/Logo%20UNICAEN%20V1-noir.png?itok=J3rUaLBD" width="40%" and height="40%"/>

# Projet tutoré pour l'observatoire UNICAEN

L'observatoire UNICAEN réalise des enquêtes sur les parcours de formation et l'insertion professionnelle des étudiants de l'université de Caen. Ils avaient besoin de 4 étudiants pour les aider sur une de leurs missions. Ils ont donc contacté mon IUT pour savoir si des étudiants pouvait les aider. Mon professeur principal a directement pensé à moi étant donné que j'étais le major de la promotion. J'ai accepté et j'ai demandé à certains de mes camarades de m'accompagné sur ce projet. 

Le projet consisté à afficher sur une carte le lieu de travail des personnes diplômées d'un master et d'une licence de l'université de Caen en 2018. 

Pour cela, l'observatoire UNICAEN nous a donné les réponses (sous format csv) d'une enquête d'insertion professionnelle qu'ils avaient envoyé aux diplômés. La difficulté principale de ce projet résidait dans le fait que les réponses étaient très hétérogènes et souvent soit erronées soit manquantes. Parmi ces données erronées, on retrouve le nom de la ville, du département et de l'entreprise dans lesquelles travaillent les diplômés.

Pour afficher chaque diplômé sur une carte en fonction de la localisation de son lieu de travail, il fallait connaître la latitude et la longitude de chaque entreprise. Pour cela, nous avons trouvé sur le site de l'[INSEE](https://www.insee.fr/fr/information/3591226) le fichier de données SIRENE. Ce fichier regroupe de nombreuses informations sur chacune des entreprises de France. Les informations qui nous intéresse étaient le nom de chacune des entreprises ainsi que la ville et le département dans lesquelles elles étaient implantées. 

Avec ces trois informations, nous avons pu corriger les réponses des diplômes en faisant correspondre les triplets (entreprise, ville, département). Pour maximiser les correspondances entre le fichier de réponses et le fichier SIRENE, nous avons utilisé le langage python et la distance de Levenshtein. Cette distance correspond au nombre de caractères qu'il faut supprimer, insérer ou remplacer pour passer d’une chaîne de caractères à une autre. Nous avons donc appliqué cette distance aux triplets (entreprise, ville, département) pour corriger les erreurs de frappe et les fautes d'orthographe. 

À la fin de cette étape, nous avons pour chaque diplômé le lieu de travail (ville et département), le nom de l'entreprise ainsi que son secteur d'activité (présent dans le fichier SIRENE). Evidemment, si dans les réponses le nom de l'entreprise n'était pas renseigné, nous ne pouvons rien faire. En effet, la ville et le département ne permettent pas à eux seuls de retrouver l'entreprise.

L'observatoire UNICAEN souhaitait aussi que l'on représente à l'aide de graphiques la répartition de chacun des secteurs d'activité dans lesquels travaillent les diplômés.

Maintenant que l'on avait bien tous les noms de ville, de département et d'entreprise, il nous restait plus qu'à trouver les latitudes et la longitudes correspondantes. Pour cela, nous avons téléchargé sur le site [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/listes-des-communes-geolocalisees-par-regions-departements-circonscriptions-nd/) un fichier avec les latitudes et la longitudes de toutes les communes de France (identifiées par leur nom et celui de leur département). En utilisant à nouveau la distance de Levenshtein, nous avons pu maximiser le nombre des correspondances entre le fichier des communes et les données des diplômés précédemment corrigées.

Enfin, nous avons représenté sur une carte au format html avec du code [JavaScript](https://leafletjs.com/) la grande majorité des lieux de travail des diplômés et le nom des entreprises correspondantes.

### À noter

Nous avons inséré toutes les données dans une base de données relationnelle pour accélérer le temps de calcul et de comparaison entre les différents fichiers de données.

# Code 

Pour des raisons de confidentialité, les deux cartes (des diplômés de Master et de Licence) ne vous sont pas montrées. 

En revanche, voici les codes Python et SQL utilisés dans ce projet :

* [DDL des tables SQL](https://github.com/ThibaultLanthiez/Projet-observatoire-UNICAEN/blob/main/Codes/DDL-SQL.sql)

* [Insertion des données des fichiers sur les tables SQL](https://github.com/ThibaultLanthiez/Projet-observatoire-UNICAEN/tree/main/Codes/Files%20to%20SQL)

* [Correction des données avec la distance de Levenshtein](https://github.com/ThibaultLanthiez/Projet-observatoire-UNICAEN/blob/main/Codes/Algorithme_Levenshtein.py)

* [Création des cartes](https://github.com/ThibaultLanthiez/Projet-observatoire-UNICAEN/tree/main/Codes/Cr%C3%A9ation%20des%20cartes)
