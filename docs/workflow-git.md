# Workflow Git du projet

Le projet suit un workflow simple inspiré de Git Flow.

| Branche | Rôle |
| --- | --- |
| `main` | Version stable prête à être remise |
| `develop` | Intégration des fonctionnalités |
| `feature-ui` | Travail sur l'interface |
| `feature-auth` | Connexion de démonstration |
| `feature-dashboard` | Indicateurs et logique de tableau de bord |

Chaque fonctionnalité est développée dans une branche dédiée, validée par commits, puis fusionnée dans `develop`. La branche `main` reçoit uniquement la version finale stabilisée.
