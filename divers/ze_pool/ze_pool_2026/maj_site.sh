#! /bin/sh
echo '----------------------------------------------------------'
date

set -aex

# maj du site sur gitub

# copie du fichier .csv localement
mv ~/Downloads/ze_pool_2026\ -\ feuille1.csv .

# execution du code
/Users/sbiner/miniconda3/envs/py27/bin/python zp2026.py
git add .
git commit -m "maj"
git push


