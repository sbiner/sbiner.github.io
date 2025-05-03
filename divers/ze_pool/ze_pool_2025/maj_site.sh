#! /bin/sh
echo '----------------------------------------------------------'
date

set -aex

# maj du site sur gitub

# copie du fichier .csv localement
mv ~/Downloads/ze_pool_2025\ -\ feuille1.csv .

# execution du code
/Users/sbiner/miniconda3/envs/py27/bin/python zp2025.py
git add .
git commit -m "maj"
git push


