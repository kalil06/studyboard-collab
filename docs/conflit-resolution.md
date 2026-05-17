# Résolution du conflit Git

## Situation

La branche `feature-auth` et la branche `develop` ont modifié la même phrase d'introduction dans `index.html`.

## Message Git obtenu

```text
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

## Extrait avec marqueurs de conflit

```html
<<<<<<< HEAD
        <p class="hero-copy">Suivez l'avancement du projet, les priorités et les responsabilités dans un tableau de bord clair.</p>
=======
        <p class="hero-copy">Connectez-vous à un espace sécurisé afin de suivre les tâches, les rôles et les décisions du binôme.</p>
>>>>>>> feature-auth
      </d
```

## Résolution retenue

Le binôme a fusionné les deux intentions : conserver l'idée de connexion ajoutée par Nadia et conserver la notion de suivi d'avancement précisée par Youssef.
