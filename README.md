# StudyBoard Collab

StudyBoard Collab est une mini application web universitaire conçue pour simuler un projet collaboratif complet entre deux étudiants. L'application permet à un binôme de centraliser les tâches, suivre l'avancement, documenter les responsabilités et conserver une trace claire des étapes du travail.

Projet réalisé par Med Khalil Milliti et Amen Alah ELHaj, étudiants à l'IHEC Carthage, classe 1LIG6.

## Fonctionnalités

- Tableau de bord avec nombre de tâches, tâches terminées et taux de progression.
- Formulaire d'ajout de tâche avec responsable et priorité.
- Filtres rapides : toutes les tâches, tâches ouvertes, tâches terminées.
- Persistance locale via `localStorage`.
- Connexion de démonstration pour simuler l'accès de chaque membre du binôme.
- Journal de collaboration intégré à l'interface.
- Documentation Git détaillée avec historique, branches, conflit et commandes.

## Technologies utilisées

| Technologie | Rôle |
| --- | --- |
| HTML5 | Structure sémantique de l'application |
| CSS3 | Mise en page responsive et identité visuelle |
| JavaScript | Logique métier, filtres, stockage local |
| Git | Versionnement, branches, merges, résolution de conflits |
| GitHub | Hébergement distant simulé dans le rapport |

## Installation

```bash
git clone https://github.com/med-khalil-milliti/studyboard-collab.git
cd studyboard-collab
```

Pour ouvrir l'application, lancer directement `index.html` dans un navigateur moderne.

## Utilisation

1. Ouvrir `index.html`.
2. Se connecter avec Med Khalil ou Amen Alah dans la section Connexion.
3. Ajouter une tâche avec un responsable et une priorité.
4. Filtrer les tâches selon leur état.
5. Observer la mise à jour automatique des indicateurs du tableau de bord.

## Commandes Git importantes

```bash
git status
git add .
git commit -m "feat: add task dashboard"
git switch -c feature-dashboard
git merge feature-dashboard
git push origin develop
```

## Organisation du binôme

| Étudiant | Responsabilités principales |
| --- | --- |
| Med Khalil Milliti | Interface, expérience utilisateur, structure HTML/CSS, page de connexion |
| Amen Alah ELHaj | JavaScript, logique des tâches, documentation Git, rapport technique |

## Captures prévues

--------------------------------------------------
[CAPTURE D'ÉCRAN ICI]
Description : Page GitHub du repository `studyboard-collab`, affichant le nom du dépôt, la branche principale et le bouton Code.
--------------------------------------------------

--------------------------------------------------
[CAPTURE D'ÉCRAN ICI]
Description : Terminal montrant `git status` après modification de fichiers dans la branche `develop`.
--------------------------------------------------

--------------------------------------------------
[CAPTURE D'ÉCRAN ICI]
Description : Interface de l'application avec tableau de bord, formulaire d'ajout de tâche et liste filtrable.
--------------------------------------------------

## Licence

Projet publié sous licence MIT dans un contexte pédagogique.
