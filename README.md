À PROPOS

Ceci est un melting pot des différents scripts que j'utilise afin d'automatiser au maximum les tâches manuelles de mon entreprise de vente en ligne.
Il ne représente pas un tout cohérent de prime abord, mélangeant du python et du javascript dans la même branche, mais ces scripts se parlent ensemble via des déclencheurs d'éditions et horaires.
Ensemble, ils effectuent l'ensemble de ma comptabilité et permettent la génération automatique des étiquettes clients, ainsi que l'enregistrement des données nécessaires au maintien propre et efficace de la fiscalité de l'entreprise.

LES DIFFÉRENTS FICHIERS - Ils s'exécutent dans cette ordre grâce à un jeu complexe de déclencheurs

Fetch Order ID est écrit en python et utilise Selenium afin d'aller chercher de l'information sur une plateforme Web centralisant les commandes, écrite en Laravel (elle ne m'appartient pas).

Manipulation de la table Google Sheet, écrite en JavaScript dans le Appscript de Google, utilise l'information recueilli par Fetch Order ID en l'enregistrant au bon endroit dans la feuille. Il retourne ensuite deux csv contenant les informations nécessaires à la génération des étiquettes.

Impression automatique des étiquettes.py, écrit aussi en python et utilisant Selenium, navigue sur Avery.com afin de générer le pdf des étiquettes en utilisant les csv retourné par Manipulation de la table Google Sheet. Il envoie ensuite ce pdf à l'imprimante et lance l'impression.


Chacun de ces programmes efface les traces de son exécution derrière lui et/ou laisse les fichiers nécessaires à l'exécution du lendemain! Le taux de réussite du programme en entier est très élevé, 99%. Des miss se produisent lorsque l'ordinateur hébergeant les scripts python est en mise à jour ou s'est fermé pour une raison ou une autre. En effet, ces scripts sont pour l'instant exécuter localement.

Merci beaucoup!
