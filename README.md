# Présentation du projet
Bonjour, notre projet consiste à extraire des informations sur les offre d'emploi, notamment pour les postes d'alternance situés en île-de-france. Et notre projet est basé sur le sites d'emlpoi Indeed. Le but est de faciliter la recherche d'emploi, particulièrement pour l'étape de postuler. On vise à collecter les emails de RH selon des informations obtenues, à automatiser l'écrit du email selon la description du poste existant l'email de recrutement et l'envoi de notre CV pour effectuer la postulation.

## Le processus de réalisation
1. La première étape c'est bien sûr de collecter des informations que l'on a besoin en utilisant la méthode de scraping. Car le site d'emploi est un site de type dynamique, ainsi on utilise le module Selenium de python pour réaliser le scraping. D'abord on extraire tous les liens des offres d'emplois, puis on cherche les liens ayant l'email de recrutement dans son contenu, ensuite, on collecte la description de poste correspondante pour chaque email obeteu. Et on enregistre les informations collectés dans un fichier excel afin de mieux voir le résultat et faciliter notre prochaine étape.

2. Dans la deuxième étape, on vise à automatiser la génération du contenu de l'e-mail de candidature sur la base des descriptions de postes que nous collecté. Pour réaliser cela, on utilise l'outil AI (Chatgpt)

3. La dernière étape est de réaliser l'envoi automatique des emails de candidatures.
 
