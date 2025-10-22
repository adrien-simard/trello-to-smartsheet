# Instructions de Setup - Environnement Léger

Ce guide explique comment créer un environnement conda minimal pour générer un .exe léger.

## Étape 1 : Créer l'environnement conda

```bash
# Créer l'environnement à partir du fichier environment.yml
conda env create -f environment.yml

# Activer l'environnement
conda activate trello-smartsheet
```

## Étape 2 : Installer PyInstaller

```bash
# Installer PyInstaller dans l'environnement
pip install pyinstaller
```

## Étape 3 : Construire l'exécutable

```bash
# Option 1 : Utiliser le script de build optimisé (RECOMMANDÉ)
python build_lightweight.py

# Option 2 : Build manuel avec PyInstaller
pyinstaller --onefile --windowed --name=TrelloToSmartsheet ^
    --exclude-module=matplotlib --exclude-module=numpy ^
    --exclude-module=pandas --exclude-module=scipy ^
    --clean --noconfirm trello_gui.py
```

## Étape 4 : Tester l'exécutable

```bash
# L'exe se trouve dans le dossier dist/
.\dist\TrelloToSmartsheet.exe
```

## Bibliothèques incluses (minimal)

L'environnement ne contient que les bibliothèques strictement nécessaires :
- **Python 3.11** (version stable et légère)
- **smartsheet-python-sdk** (API Smartsheet)
- **openpyxl** (lecture fichiers Excel pour mapping emails)
- **tkinter** (GUI - inclus avec Python)
- **PyInstaller** (pour créer l'exe)

## Optimisations appliquées

1. **Exclusion de modules volumineux** : numpy, pandas, matplotlib, scipy, etc.
2. **Python 3.11** : version optimisée et plus légère
3. **Pas de dépendances inutiles** : environnement minimal
4. **Strip des symboles** : réduction de la taille binaire

## Taille estimée de l'exe

- **Sans optimisation** : ~50-80 MB
- **Avec optimisations** : ~20-30 MB

## Nettoyage après build

```bash
# Supprimer les fichiers temporaires
rmdir /s /q build
del TrelloToSmartsheet.spec

# Garder seulement dist/TrelloToSmartsheet.exe
```

## Désactiver/Supprimer l'environnement

```bash
# Désactiver
conda deactivate

# Supprimer l'environnement (si besoin)
conda env remove -n trello-smartsheet
```

## Troubleshooting

### L'exe est encore trop gros
- Vérifier qu'aucune bibliothèque inutile n'est installée : `pip list`
- Utiliser `--strip` pour réduire la taille
- Considérer l'utilisation de UPX (compression) : retirer `--noupx`

### Erreur au lancement de l'exe
- Tester d'abord le script Python : `python trello_gui.py`
- Vérifier les dépendances : `pip check`
- Regarder les logs PyInstaller dans le dossier `build/`

### Import errors
- Assurez-vous d'être dans l'environnement conda : `conda activate trello-smartsheet`
- Réinstaller les dépendances : `pip install -r requirements.txt`
