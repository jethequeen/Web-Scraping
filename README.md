À PROPOS

Ceci est un melting pot des différents scripts que j'utilise afin d'automatiser au maximum les tâches manuelles de mon entreprise de vente en ligne.
Il ne représente pas un tout cohérent de prime abord, mélangeant du python et du javascript dans la même branche, mais ces scripts se parlent ensemble via des déclencheurs d'éditions et horaires.
Ensemble, ils effectuent l'ensemble de ma comptabilité et permettent la génération automatique des étiquettes clients, ainsi que l'enregistrement des données nécessaires au maintien propre et efficace de la fiscalité de l'entreprise.

LES DIFFÉRENTS FICHIERS

Fetch Order ID est écrit en python et utilise Selenium afin d'aller chercher de l'information sur une plateforme Web centralisant les commandes, écrite en Laravel (elle ne m'appartient pas).

Impression automatique des étiquettes.py, écrit aussi en python et utilisant Selenium, navigue sur Avery.com afin de générer le pdf des étiquettes en utilisant le csv retourné par Fetch Order ID. Il envoie ensuite ce pdf à l'imprimante et lance l'impression.

