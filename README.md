[:arrow_left: Retour vers le portfolio](https://github.com/ThibaultLanthiez/Portfolio)

# Projet tutoré pour l'Université de Caen

L'observatoire UNICAEN réalise des enquêtes sur les parcours de formation et l'insertion professionnelle des étudiants de l'université de Caen. Ils avaient besoin de 4 étudiants pour les aider sur une de leurs missions. Ils ont donc contacté mon IUT pour savoir si des étudiants pouvait les aider. Mon professeur principal a directement pensé à moi étant donné que j'étais le major de la promotion. J'ai accepté et j'ai demandé à certains de mes camarades de m'accompagné sur ce projet. 

Le projet consité à afficher sur une carte le lieu de travail des personnes diplomées d'un master et d'une licence de l'université de Caen en 2018. 

Pour cela, l'observatoire UNICAEN nous a donné les réponses (sous format csv) d'une enquête d'insertion professionnelle qu'ils avaient envoyés aux diplômés. La difficulté principale de ce projet résidait dans le fait que les réponses était très hétérogènes et souvent soit erronées soit manquantes. Parmi ces données erronées, on retrouve le nom de la ville, du département et de l'entreprise dans lesquelles travaille les diplômés.

Pour afficher chaque diplômés sur une carte en fonction de la localisation de son lieu de travail, il fallait connaître la latitude et la longitude de chaque entreprise. Pour cela, nous avait trouvé sur le site de l'[INSEE](https://www.insee.fr/fr/information/3591226) le fichier de données SIRENE. Ce fichier regroupe de nombreuses informations sur chacune des entreprises de France. Les informations qui nous intéressées étaient le nom de chacune des entreprises ainsi que la ville et le département dans lesquelles elles été implantées. Avec ces trois informations, nous avons pu corriger les réponses des diplômes en faisant correspondre les triplets (entreprise, ville, département). Pour maximiser les correspondances entre le fichier de réponses et le fichier SIRENE, nous avons utilisé le langage python et la distance de Levenshtein. Cette distance correspond au nombre de caractères qu'il faut supprimer, insérer ou remplacer pour passer d’une chaîne de caractères à une autre. Nous avons donc appliquer cette distance aux triplets (entreprise, ville, département) pour corriger les erreurs de frappe et les fautes d'orthographe. 

À la fin de cette étape, nous avons pour chaque diplômés le lieu de travail (ville et département), le nom de l'entreprise ainsi que son secteur d'activité (présent dans le fichier SIRENE). Évidement, si dans les réponses le nom de l'entreprise n'était pas renseigné, nous n'avons rien pu faire. En effet, la ville et le département ne permettent pas à eux seuls de retrouver l'entreprise.

L'observatoire UNICAEN souhaite aussi que l'on représente à l'aide de graphique la répartition de chacun des secteur d'activité dans lesquels travaille le diplômés.

Maintenant que l'on avait bien tous les noms de ville, de département et d'entreprise, il nous restait plus qu'à trouver les latitudes et la longitudes correspondantes. Pour cela, nous avons télécharger sur le site [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/listes-des-communes-geolocalisees-par-regions-departements-circonscriptions-nd/) un fichier avec les latitudes et la longitudes de toutes les communes de France (identifiées par leur noms et celui dans leur département). En utilisant à novueau la distance de Levenshtein, nous avons pu maximiser le nombre des correspondances entre le fichier des communes et les données des diplomés précédemment corrigées.

Enfin, nous avons représenté sur une carte au format html avec du code [JavaScript](https://leafletjs.com/) la grande majorité des lieux de travail des diplomés et le nom de l'entreprise correspondante.

### À noter

Nous avons inséré toutes les données dans une base de données relationnelle pour accélérer le temps de calcul et de comparaison entre les différents fichier de données.

# Code 

Pour des raisons de confidentialité, les deux cartes (pour les diplômes de master et de licence), ne vous sont pas montrées. 

En revanche, voici les codes python et sql utilisé dans ce projet.



[Lien Google Drive](https://drive.google.com/drive/u/0/folders/1Bxr0rauNXz7VsVXgN70zaj1dnx60WF-8)
