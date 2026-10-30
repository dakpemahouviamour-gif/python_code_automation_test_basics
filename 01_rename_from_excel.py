import os
import pandas as pd
mon_dossier=r"D:\list_reading"#le chemin de mes fichiers pdf
#le programme qui me donne la liste des noms actuels des fichiers dans un tableau excel
#fichiers=os.listdir(mon_dossier)
#tableau=pd.DataFrame(fichiers, columns=["Nom actuel"])
#tableau.to_excel("liste_fichiers.xlsx", index=False)
#print("✅ Fichier Excel créé avec succès !")
tableau = pd.read_excel("liste_fichiers.xlsx")# lire excel 
for index, ligne in tableau.iterrows():
     # 3. Récupérer les noms
    ancien_nom = ligne["Nom actuel"]
    nouveau_nom = ligne["Nouveau nom"]
    
    # 4. Créer les chemins
    chemin_ancien = os.path.join(mon_dossier, ancien_nom)
    chemin_nouveau = os.path.join(mon_dossier, nouveau_nom)
    
    if os.path.exists(chemin_ancien):
        if os.path.exists(chemin_nouveau):
            print(f"⚠️ Attention : {nouveau_nom} existe déjà. On saute.")
        else:
            os.rename(chemin_ancien, chemin_nouveau)
            print(f"✅ Renommé : {ancien_nom} -> {nouveau_nom}")
    else:
        print(f"❌ Fichier introuvable : {ancien_nom}")