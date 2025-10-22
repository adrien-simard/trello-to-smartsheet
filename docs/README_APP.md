# Trello to Smartsheet Migration Tool

Application graphique pour migrer vos boards Trello vers Smartsheet avec préservation complète de la structure Kanban.

## Fonctionnalités

✅ **Migration complète**:
- Listes Trello → Lanes Smartsheet (Card View)
- Cartes → Lignes Smartsheet
- Descriptions, dates, URLs
- Commentaires → Discussions Smartsheet

✅ **Gestion avancée**:
- **Labels**: Tags multi-sélection dans Smartsheet
- **Membres**: Contacts avec emails (MULTI_CONTACT_LIST)
- **Mapping d'emails**: Support fichier Excel pour emails réels
- **Dossiers**: Organisation automatique dans Smartsheet

## Installation

### Option 1: Fichier .EXE (Recommandé)

1. Téléchargez `TrelloToSmartsheet.exe`
2. Double-cliquez pour lancer l'application
3. Aucune installation requise!

### Option 2: Script Python

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'interface graphique
python trello_gui.py
```

## Utilisation

### 1. Exporter votre board Trello

1. Ouvrez votre board Trello
2. Menu → Plus → Imprimer et exporter
3. Exporter en JSON
4. Sauvegardez le fichier (ex: `mon_board.json`)

### 2. Obtenir votre token Smartsheet API

1. Connectez-vous à Smartsheet
2. Icône profil (en haut à droite) → Apps & Integrations
3. API Access → Generate new access token
4. Copiez le token (vous ne le verrez qu'une fois!)

### 3. Lancer la migration

1. **Trello JSON Export**: Sélectionnez votre fichier `.json`
2. **Smartsheet API Token**: Collez votre token
3. **Folder ID** (optionnel): ID du dossier Smartsheet de destination
4. **Email Mapping** (optionnel): Fichier Excel avec correspondance noms/emails
5. Cliquez sur **Start Migration**

### 4. Configurer Card View dans Smartsheet

Après la migration:
1. Ouvrez le sheet créé
2. Cliquez sur "Card View" (barre d'outils)
3. Sélectionnez "List" comme champ de lanes
4. Votre board Kanban est prêt!

## Email Mapping (Optionnel)

Créez un fichier Excel avec 2 colonnes:

| Members          | email                        |
|------------------|------------------------------|
| John Smith       | john.smith@example.com       |
| Roberto Garcia   | roberto.garcia@example.com   |
| Anna Miller      | anna.miller@example.com      |

**Format**:
- Colonne A: Nom complet (tel qu'il apparaît dans Trello)
- Colonne B: Email

Si un nom n'est pas dans le fichier, un email sera généré automatiquement au format `prenom.nom@epfl.ch`.

## Structure créée dans Smartsheet

| Colonne          | Type                  | Description                    |
|------------------|-----------------------|--------------------------------|
| Card Name        | Texte (Primary)       | Titre de la carte Trello      |
| List             | Dropdown              | Liste Trello (pour les lanes) |
| Description      | Texte                 | Description complète          |
| Due Date         | Date                  | Date d'échéance               |
| Members          | Multi-Contact List    | Assignations avec emails      |
| Labels           | Multi-Picklist        | Tags sélectionnables          |
| URL              | Texte                 | Lien vers carte Trello        |
| Created Date     | Date                  | Date de création              |

## Dépannage

### "API Token invalide"
- Vérifiez que vous avez copié le token complet
- Le token doit être celui de votre compte Smartsheet
- Regénérez un nouveau token si nécessaire

### "Fichier JSON non trouvé"
- Assurez-vous d'avoir sélectionné le bon fichier
- Le fichier doit être un export JSON valide de Trello

### "Folder ID invalide"
- Le Folder ID doit être un nombre
- Laissez vide pour créer dans votre Home Smartsheet
- Trouvez l'ID en ouvrant le dossier dans Smartsheet (URL)

### La migration est lente
- C'est normal pour les boards avec beaucoup de cartes/commentaires
- L'API Smartsheet a des limites de taux
- Attendez simplement que le processus se termine

## Limitations

- **Pièces jointes**: Non migrées (prévu pour version future)
- **Checklists**: Non migrées (prévu pour version future)
- **Images de couverture**: Non préservées
- **Champs personnalisés Trello**: Non supportés

## Support

Pour signaler un bug ou demander une fonctionnalité, contactez l'équipe de développement.

## Version

- **Version**: 1.0.0
- **Date**: Octobre 2025
- **Compatibilité**: Windows 10/11, macOS, Linux

## Licence

Outil interne - Utilisation EPFL uniquement.
