# Transcription terminal

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe init
Initialized empty Git repository in C:/Users/8RABB/Desktop/New folder/StudyBoard-Collab/.git/
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe branch -M main
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe config user.name Nadia Ben Salem
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe config user.email nadia.bensalem@example.edu
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe init --bare C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git
Initialized empty Git repository in C:/Users/8RABB/Desktop/New folder/StudyBoard-Collab-origin.git/
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe remote add origin C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'LICENSE', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m chore: initialiser le depot et les metadonnees
[main (root-commit) 86728a9] chore: initialiser le depot et les metadonnees
 3 files changed, 28 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 LICENSE
 create mode 100644 README.md
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe push -u origin main
branch 'main' set up to track 'origin/main'.
To C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git
 * [new branch]      main -> main
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch -c develop
Switched to a new branch 'develop'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'LICENSE', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'css/styles.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/captures.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/notes-de-reunion.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/obsolete-plan.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/workflow-git.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'js/app.js', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m chore: creer la structure du projet web
[develop 053c98a] chore: creer la structure du projet web
 8 files changed, 242 insertions(+)
 create mode 100644 assets/.gitkeep
 create mode 100644 css/styles.css
 create mode 100644 docs/captures.md
 create mode 100644 docs/notes-de-reunion.md
 create mode 100644 docs/obsolete-plan.md
 create mode 100644 docs/workflow-git.md
 create mode 100644 index.html
 create mode 100644 js/app.js
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'LICENSE', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'css/styles.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/captures.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/notes-de-reunion.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/obsolete-plan.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/workflow-git.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'js/app.js', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m feat: ajouter la page d'accueil et les sections principales
[develop 08a37ef] feat: ajouter la page d'accueil et les sections principales
 1 file changed, 79 insertions(+)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'css/styles.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m style: ajouter la mise en page responsive principale
[develop 8d74c74] style: ajouter la mise en page responsive principale
 1 file changed, 201 insertions(+), 8 deletions(-)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'css/styles.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'js/app.js', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m feat: implementer la gestion locale des taches
[develop aa808fe] feat: implementer la gestion locale des taches
 1 file changed, 140 insertions(+), 3 deletions(-)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'css/styles.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'js/app.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/commandes-git-detaillees.md', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m docs: documenter le workflow et les commandes Git
[develop cbad997] docs: documenter le workflow et les commandes Git
 1 file changed, 434 insertions(+)
 create mode 100644 docs/commandes-git-detaillees.md
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe push -u origin develop
branch 'develop' set up to track 'origin/develop'.
To C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git
 * [new branch]      develop -> develop
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch -c feature-ui
Switched to a new branch 'feature-ui'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'css/styles.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/commandes-git-detaillees.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'js/app.js', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m style: ameliorer les etats visuels des taches
[feature-ui 3ebb339] style: ameliorer les etats visuels des taches
 1 file changed, 5 insertions(+)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch develop
Your branch is up to date with 'origin/develop'.
Switched to branch 'develop'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe merge --no-ff feature-ui -m merge: integrer feature-ui dans develop
Merge made by the 'ort' strategy.
 css/styles.css | 5 +++++
 1 file changed, 5 insertions(+)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch -c feature-auth
Switched to a new branch 'feature-auth'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'css/styles.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'js/app.js', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m feat: ajouter une connexion locale de demonstration
[feature-auth 6f269b9] feat: ajouter une connexion locale de demonstration
 3 files changed, 29 insertions(+), 3 deletions(-)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch develop
Your branch is ahead of 'origin/develop' by 2 commits.
  (use "git push" to publish your local commits)
Switched to branch 'develop'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m feat: preciser le message du tableau de bord
[develop 8bba4d1] feat: preciser le message du tableau de bord
 1 file changed, 1 insertion(+), 1 deletion(-)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe merge --no-ff feature-auth
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'css/styles.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'js/app.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'docs/conflit-resolution.md', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m merge: resoudre le conflit entre develop et feature-auth
[develop 09f2ba6] merge: resoudre le conflit entre develop et feature-auth
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch -c feature-dashboard
Switched to a new branch 'feature-dashboard'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'css/styles.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'js/app.js', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m feat: exposer l'etat du tableau de bord pour validation
[feature-dashboard 609abe0] feat: exposer l'etat du tableau de bord pour validation
 2 files changed, 10 insertions(+)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch develop
Your branch is ahead of 'origin/develop' by 5 commits.
  (use "git push" to publish your local commits)
Switched to branch 'develop'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe merge --no-ff feature-dashboard -m merge: integrer feature-dashboard
Merge made by the 'ort' strategy.
 css/styles.css | 6 ++++++
 js/app.js      | 4 ++++
 2 files changed, 10 insertions(+)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe rm docs/obsolete-plan.md
rm 'docs/obsolete-plan.md'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m chore: supprimer le brouillon obsolete avec git rm
[develop 1e7e884] chore: supprimer le brouillon obsolete avec git rm
 1 file changed, 3 deletions(-)
 delete mode 100644 docs/obsolete-plan.md
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m docs: enrichir le README professionnel
[develop 3895802] docs: enrichir le README professionnel
 1 file changed, 76 insertions(+), 2 deletions(-)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe push origin develop
To C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git
   cbad997..3895802  develop -> develop
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe clone C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-Etudiant2
Cloning into 'C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-Etudiant2'...
done.
warning: remote HEAD refers to nonexistent ref, unable to checkout
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch develop
branch 'develop' set up to track 'origin/develop'.
Switched to a new branch 'develop'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe config user.name Youssef Mansouri
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe config user.email youssef.mansouri@example.edu
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch -c feature-docs-student2
Switched to a new branch 'feature-docs-student2'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add -A
warning: in the working copy of 'docs/captures.md', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe commit -m docs: ajouter une capture de pull request
[feature-docs-student2 7cecb18] docs: ajouter une capture de pull request
 1 file changed, 5 insertions(+)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe push -u origin feature-docs-student2
branch 'feature-docs-student2' set up to track 'origin/feature-docs-student2'.
To C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git
 * [new branch]      feature-docs-student2 -> feature-docs-student2
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe fetch origin
From C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin
 * [new branch]      feature-docs-student2 -> origin/feature-docs-student2
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch develop
Your branch is up to date with 'origin/develop'.
Already on 'develop'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe merge --no-ff origin/feature-docs-student2 -m merge: integrer la documentation etudiant 2
Merge made by the 'ort' strategy.
 docs/captures.md | 5 +++++
 1 file changed, 5 insertions(+)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe pull origin develop
Already up to date.
From C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin
 * branch            develop    -> FETCH_HEAD
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe stash push -m wip: note temporaire README
Saved working directory and index state On develop: wip: note temporaire README
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe stash pop
On branch develop
Your branch is ahead of 'origin/develop' by 2 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (1bba1352cdc5a96e4e3994fbcd7f1dff6a490fff)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe restore README.md
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe restore css/styles.css
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe add README.md
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe reset README.md
Unstaged changes after reset:
M	README.md
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe restore README.md
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe switch main
Your branch is up to date with 'origin/main'.
Switched to branch 'main'
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe merge --no-ff develop -m release: fusionner develop dans main
Merge made by the 'ort' strategy.
 README.md                        |  78 ++++++-
 assets/.gitkeep                  |   0
 css/styles.css                   | 313 ++++++++++++++++++++++++++++
 docs/captures.md                 |  87 ++++++++
 docs/commandes-git-detaillees.md | 434 +++++++++++++++++++++++++++++++++++++++
 docs/conflit-resolution.md       |  28 +++
 docs/notes-de-reunion.md         |  13 ++
 docs/workflow-git.md             |  13 ++
 index.html                       | 135 ++++++++++++
 js/app.js                        | 156 ++++++++++++++
 10 files changed, 1255 insertions(+), 2 deletions(-)
 create mode 100644 assets/.gitkeep
 create mode 100644 css/styles.css
 create mode 100644 docs/captures.md
 create mode 100644 docs/commandes-git-detaillees.md
 create mode 100644 docs/conflit-resolution.md
 create mode 100644 docs/notes-de-reunion.md
 create mode 100644 docs/workflow-git.md
 create mode 100644 index.html
 create mode 100644 js/app.js
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe push origin main
To C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git
   86728a9..1d2bba2  main -> main
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe status --short
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe log --oneline --graph --all --decorate --date=short
*   1d2bba2 (HEAD -> main, origin/main) release: fusionner develop dans main
|\  
| *   89dd91f (develop) merge: integrer la documentation etudiant 2
| |\  
| | * 7cecb18 (origin/feature-docs-student2) docs: ajouter une capture de pull request
| |/  
| * 3895802 (origin/develop) docs: enrichir le README professionnel
| * 1e7e884 chore: supprimer le brouillon obsolete avec git rm
| *   86843b3 merge: integrer feature-dashboard
| |\  
| | * 609abe0 (feature-dashboard) feat: exposer l'etat du tableau de bord pour validation
| |/  
| *   09f2ba6 merge: resoudre le conflit entre develop et feature-auth
| |\  
| | * 6f269b9 (feature-auth) feat: ajouter une connexion locale de demonstration
| * | 8bba4d1 feat: preciser le message du tableau de bord
| |/  
| *   f6b206e merge: integrer feature-ui dans develop
| |\  
| | * 3ebb339 (feature-ui) style: ameliorer les etats visuels des taches
| |/  
| * cbad997 docs: documenter le workflow et les commandes Git
| * aa808fe feat: implementer la gestion locale des taches
| * 8d74c74 style: ajouter la mise en page responsive principale
| * 08a37ef feat: ajouter la page d'accueil et les sections principales
| * 053c98a chore: creer la structure du projet web
|/  
* 86728a9 chore: initialiser le depot et les metadonnees
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe branch -a
  develop
  feature-auth
  feature-dashboard
  feature-ui
* main
  remotes/origin/develop
  remotes/origin/feature-docs-student2
  remotes/origin/main
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe remote -v
origin	C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git (fetch)
origin	C:\Users\8RABB\Desktop\New folder\StudyBoard-Collab-origin.git (push)
```

---

```text
$ C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```