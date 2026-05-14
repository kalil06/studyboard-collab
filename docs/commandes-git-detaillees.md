# Commandes Git détaillées

## git init

**Définition :** `git init` est utilisé pour initialiser un dépôt git local.

**Syntaxe :**

```bash
git init
```

**Exemple du projet :**

```bash
git init
```

**Résultat attendu :** Initialized empty Git repository in .../.git/

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git clone

**Définition :** `git clone` est utilisé pour copier un dépôt distant ou local.

**Syntaxe :**

```bash
git clone <url>
```

**Exemple du projet :**

```bash
git clone https://github.com/nadia-youssef/studyboard-collab.git
```

**Résultat attendu :** Cloning into 'studyboard-collab'...

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git status

**Définition :** `git status` est utilisé pour afficher l'état du répertoire de travail.

**Syntaxe :**

```bash
git status
```

**Exemple du projet :**

```bash
git status
```

**Résultat attendu :** On branch develop / nothing to commit, working tree clean

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git add

**Définition :** `git add` est utilisé pour ajouter des modifications à l'index.

**Syntaxe :**

```bash
git add <fichier|.>
```

**Exemple du projet :**

```bash
git add index.html css/styles.css
```

**Résultat attendu :** Les fichiers sont prêts pour le prochain commit.

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git commit

**Définition :** `git commit` est utilisé pour créer un point d'historique.

**Syntaxe :**

```bash
git commit -m "message"
```

**Exemple du projet :**

```bash
git commit -m "feat: add task dashboard"
```

**Résultat attendu :** [develop abc123] feat: add task dashboard

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git push

**Définition :** `git push` est utilisé pour envoyer les commits vers le dépôt distant.

**Syntaxe :**

```bash
git push origin <branche>
```

**Exemple du projet :**

```bash
git push origin develop
```

**Résultat attendu :** develop -> develop

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git pull

**Définition :** `git pull` est utilisé pour récupérer et intégrer les changements distants.

**Syntaxe :**

```bash
git pull origin develop
```

**Exemple du projet :**

```bash
git pull origin develop
```

**Résultat attendu :** Already up to date.

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git branch

**Définition :** `git branch` est utilisé pour lister ou créer des branches.

**Syntaxe :**

```bash
git branch / git branch <nom>
```

**Exemple du projet :**

```bash
git branch feature-ui
```

**Résultat attendu :** La branche est créée localement.

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git checkout

**Définition :** `git checkout` est utilisé pour changer de branche ou restaurer une version.

**Syntaxe :**

```bash
git checkout <branche>
```

**Exemple du projet :**

```bash
git checkout develop
```

**Résultat attendu :** Switched to branch 'develop'

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git switch

**Définition :** `git switch` est utilisé pour changer de branche avec une commande moderne.

**Syntaxe :**

```bash
git switch <branche>
```

**Exemple du projet :**

```bash
git switch -c feature-auth
```

**Résultat attendu :** Switched to a new branch 'feature-auth'

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git merge

**Définition :** `git merge` est utilisé pour fusionner une branche dans la branche active.

**Syntaxe :**

```bash
git merge <branche>
```

**Exemple du projet :**

```bash
git merge feature-ui
```

**Résultat attendu :** Merge made by the 'ort' strategy.

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git fetch

**Définition :** `git fetch` est utilisé pour télécharger les références distantes sans fusion.

**Syntaxe :**

```bash
git fetch origin
```

**Exemple du projet :**

```bash
git fetch origin
```

**Résultat attendu :** origin/feature-docs-student2 mis à jour.

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git stash

**Définition :** `git stash` est utilisé pour mettre temporairement de côté des changements.

**Syntaxe :**

```bash
git stash push -m <message>
```

**Exemple du projet :**

```bash
git stash push -m "wip notes reunion"
```

**Résultat attendu :** Saved working directory and index state.

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git log

**Définition :** `git log` est utilisé pour consulter l'historique.

**Syntaxe :**

```bash
git log --oneline --graph --all
```

**Exemple du projet :**

```bash
git log --oneline --graph --all --decorate
```

**Résultat attendu :** * abc123 feat: add dashboard

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git remote -v

**Définition :** `git remote -v` est utilisé pour lister les dépôts distants configurés.

**Syntaxe :**

```bash
git remote -v
```

**Exemple du projet :**

```bash
git remote -v
```

**Résultat attendu :** origin  https://github.com/... (fetch)

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git restore

**Définition :** `git restore` est utilisé pour annuler une modification locale.

**Syntaxe :**

```bash
git restore <fichier>
```

**Exemple du projet :**

```bash
git restore css/styles.css
```

**Résultat attendu :** Le fichier revient à la dernière version validée.

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git rm

**Définition :** `git rm` est utilisé pour supprimer un fichier suivi par git.

**Syntaxe :**

```bash
git rm <fichier>
```

**Exemple du projet :**

```bash
git rm docs/obsolete-plan.md
```

**Résultat attendu :** rm 'docs/obsolete-plan.md'

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

## git reset

**Définition :** `git reset` est utilisé pour désindexer ou déplacer head selon le mode choisi.

**Syntaxe :**

```bash
git reset [--soft|--mixed|--hard] <cible>
```

**Exemple du projet :**

```bash
git reset README.md
```

**Résultat attendu :** Un fichier staged redevient modifié non staged.

**Importance :** cette commande participe à la traçabilité du projet, réduit les pertes de travail et rend le développement collaboratif contrôlable.

**Erreurs possibles :** mauvaise branche active, fichier non suivi, conflit après synchronisation, remote absent ou droits insuffisants.

**Solution pratique :** vérifier `git status`, lire le message Git complet, synchroniser avec `git fetch` ou `git pull`, puis refaire la commande avec une branche propre.

