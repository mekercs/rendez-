import os
import shutil
from tkinter import*
from tkinter import filedialog

mappa=filedialog.askdirectory()

anyaaa = {
    'pdf': 'PDF-ek',
    'png': 'Képek',
    'jpg': 'Képek',
    'jpeg': 'Képek',
    'gif': 'Képek',
    'doc': 'Dokumentumok',
    'docx': 'Dokumentumok',
    'txt': 'Dokumentumok',
    'csv': 'Adatok',
    'xlsx': 'Adatok',
    'zip': 'Tömörítvények',
    'rar': 'Tömörítvények',
    'exe': 'Programok',
    'mp3': 'Zenék',
    'wav': 'Zenék',
    'mp4': 'Videók',
    'avi': 'Videók',
    'flv': 'Videók',
    'wmv': 'Videók',
    'c':'C-programok',
    'py':'Python-programok',
    'html':'html-weboldalak'
}

for fajl in os.listdir(mappa):
    faljirany = os.path.join(mappa, fajl)
    if os.path.isfile(faljirany):
        kiterjesztes = fajl.split('.')[-1].lower()
        if kiterjesztes in anyaaa:
            dikmappa = anyaaa[kiterjesztes]
            cel_mappa = os.path.join(mappa,dikmappa)
            if not os.path.exists(cel_mappa):
                os.makedirs(cel_mappa)
            cel = os.path.join(cel_mappa,fajl)
            shutil.move(faljirany,cel)

print("kész az elrendezés")
input()