"""
Script pour créer un .exe léger avec PyInstaller
Utilise des options d'optimisation pour réduire la taille
"""

import subprocess
import sys
import os

def build_exe():
    """Build un .exe optimisé et léger"""

    print("=" * 60)
    print("BUILD LIGHTWEIGHT EXE - Trello to Smartsheet")
    print("=" * 60)

    # Options PyInstaller pour réduire la taille
    pyinstaller_cmd = [
        'pyinstaller',
        '--onefile',                    # Un seul fichier exe
        '--windowed',                   # Pas de console (GUI seulement)
        '--name=TrelloToSmartsheet',    # Nom de l'exe
        '--clean',                      # Nettoyer le cache
        '--noconfirm',                  # Pas de confirmation

        # Exclusions pour réduire la taille
        '--exclude-module=matplotlib',
        '--exclude-module=numpy',
        '--exclude-module=pandas',
        '--exclude-module=scipy',
        '--exclude-module=PIL',
        '--exclude-module=pytest',
        '--exclude-module=setuptools',
        '--exclude-module=wheel',
        '--exclude-module=IPython',
        '--exclude-module=notebook',

        # Optimisations
        '--noupx',                      # Ne pas utiliser UPX (évite des problèmes)

        # Fichier principal
        'trello_gui.py'
    ]

    print("\n[*] Exécution de PyInstaller avec options optimisées...")
    print(f"    Commande: {' '.join(pyinstaller_cmd)}")

    try:
        subprocess.run(pyinstaller_cmd, check=True)
        print("\n" + "=" * 60)
        print("[SUCCESS] Build terminé !")
        print("=" * 60)
        print(f"\nFichier .exe créé dans: dist\\TrelloToSmartsheet.exe")

        # Afficher la taille du fichier
        exe_path = os.path.join('dist', 'TrelloToSmartsheet.exe')
        if os.path.exists(exe_path):
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print(f"Taille du fichier: {size_mb:.2f} MB")

    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Le build a échoué: {e}")
        sys.exit(1)

if __name__ == '__main__':
    build_exe()
