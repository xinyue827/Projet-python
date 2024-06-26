# Présentation du projet
Bonjour, notre projet consiste à extraire des informations sur les offre d'emploi, notamment pour les postes d'alternance situés en île-de-france. Et notre projet est basé sur le sites d'emlpoi Indeed. Le but est de faciliter la recherche d'emploi, particulièrement pour l'étape de postuler. On vise à collecter les emails de RH selon des informations obtenues, à automatiser la rédaction du email selon la description du poste existant l'email de recrutement et notre information personnelle pour personaliser le contenu du mail. Enfin, on automatise l'envoi de notre CV par email pour effectuer la postulation.

## Le processus de réalisation
**1. Collecte d'informations via le scraping**  

La première étape c'est bien sûr de collecter des informations que l'on a besoin en utilisant la méthode de scraping. Car le site d'emploi est un site de type dynamique, ainsi on utilise le module Selenium de python pour réaliser le scraping.  

D'abord on extraire tous les liens des offres d'emplois, puis on cherche les liens ayant l'email de recrutement dans son contenu, ensuite, on collecte la description de poste correspondante pour chaque email obeteu. Et on enregistre les informations collectés dans un fichier excel afin de mieux voir le résultat et faciliter notre prochaine étape.

**2. Automatisation de la génération du contenu de l'e-mail de candidature**  

Dans la deuxième étape, nous visons à automatiser la génération du contenu de l'e-mail de candidature en fonction des descriptions de poste que nous avons collectées et certaines nos informations personnelles comme notre parcours et compétences. Pour cela, nous utilisons l'outil d'intelligence artificielle (IA) ChatGPT, et on l'ajoute dans notre processus à l'aide du package openai.

**3. Envoi automatique des emails de candidatures**  

La dernière étape consiste à réaliser l'envoi automatique des emails de candidature à l'aide de Resend. Nous automatisons ce processus pour optimiser notre efficacité dans la postulation aux offres d'emploi.

## Fichier  
&bull; Collecte_info.py contient des fonctions particulièrement à collecter des informations (email, description de poste) sur le site Indeed.   
&bull; Package.py contitent tous les packages que l'on utilise     
&bull; Emaile_envoi_resend.py contient des fonctions pour la génération automatique des contenu du email et l'envoi automatique du email.  
&bull; Projet final.rmd est l'intégralité de notre projet réalisé dans Rmarkdown  
&bull; présentation.pptx et Projet python.html sont des slides de notre projet, on a fait 2 type de slides différentes en raison de la besuté.


## Difficultés rencontrée  
&bull; La première difficulté rencontrée est liée à l'extraction des données à partir du site d'emploi Indeed qui utilise une structure dynamique.  
&bull; L'envoi automatique d'emails a posé des difficulés, il existe des problèmes de sécurité comme le problème de l'authentification. Et comment réaliser exactement cet envoi automatique nous pose de nombreuse difficultés.

 
