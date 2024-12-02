Dépôt pour le cours de Modélisation du TAL (2023_2024) - Master PluriTAL

# Description du projet  
› Ce projet a été réalisé dans le cadre du cours "De la Modélisation au traitement automatique des données linguistiques" (2024_2025) - Master PluriTAL  
› **Objectifs** : sélectionner un article de recherche en TAL, le lire, le comprendre en profondeur puis essayer de reproduire les résultats de l'article en modifiant certains aspects du travail original (le corpus, la méthode, les algorithmes etc.).  
› Nous avons choisi de nous baser sur cet article : *AJAO, Seun, BHOWMIK, Deepayan and ZARGARI, Shahrzad (2019). Sentiment aware fake news detection on online social networks. 2019* (disponible ici http://shura.shu.ac.uk/24009/) et de modifier la méthode.

# Article étudié

## Hypothèse de l'article   
› Hypothèse : Il existe une relation significative entre les sentiments/émotions exprimés dans un texte posté sur les réseaux sociaux et la probabilité que ce texte soit une fausse information/rumeur.  
› Utiliser l'**analyse des sentiments dans un contexte de détection de fake news sur les réseaux sociaux**.  
› Si l'hypothèse est vérifiée, alors l'analyse des sentiments pourrait jouer un rôle crucial dans l'amélioration des performances des classificateurs de fake news.

## Corpus utilisé
› **PHEME dataset of rumours and non-rumours**. Il contient des tweets divisés en rumeurs et non-rumeurs, liés à 5 événements.

# Notre travail

## Corpus   
› **PHEME dataset for Rumour Detection and Veracity Classification**  
› Les données sont structurées de cette manière : Chaque événement a un répertoire, avec deux sous-dossiers : rumeurs et non-rumeurs. Ces deux dossiers contiennent des dossiers nommés avec un ID de tweet. Le tweet lui-même se trouve dans le répertoire 'source-tweet' du tweet en question, et le répertoire 'reactions' contient l'ensemble des tweets répondant à ce tweet source. De plus, chaque dossier contient un fichier 'annotation.json' qui contient des informations sur la véracité de la rumeur et un fichier 'structure.json' qui contient des informations sur la structure de la conversation.  
› Ce dataset est une extension du dataset **PHEME dataset of rumours and non-rumours**. Il contient des rumeurs liées à 9 événements et chaque rumeur est annotée avec notamment des valeurs de véracité / désinformation.


## Pré-traitement
› Récupération des annotations
› Calcul du score de véracité et étiquetage (ID du tweet + contenu textuel + score de véracité (True, False, Unverified)
› Stockage dans un nouveau dictionnaire

## Méthode
› Augmentation des données avec SMOTE
› Analyse de sentiments avec Vader et TextBlob
› Classification avec SVM, Decision Tree et Random Forest
› Analyse de sentiments après classification

