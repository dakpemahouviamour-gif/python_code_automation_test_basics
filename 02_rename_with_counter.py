import os

my_folder = r"D:\automation_test\Test_Compteur" # (Garde ton vrai chemin)
files = os.listdir(my_folder)
counter = 1

for filename in files:
    new_name = f"Plan_{counter:03d}.pdf"
    old_path= os.path.join(my_folder,filename)
    new_path= os.path.join(my_folder,new_name)
    if os.path.exists(old_path):
        if os.path.exists(new_path):
                print(f"⚠️ Warning: {new_name} already exists. Skipping.")
        else:
                os.rename(old_path,new_path)
                print(f"✅ Renamed: {filename} -> {new_name}")
    else:
           
        print(f"❌ File not found: {filename}")
    counter += 1