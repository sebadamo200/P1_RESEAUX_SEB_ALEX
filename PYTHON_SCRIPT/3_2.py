import pandas as pd
import sys


arg = sys.argv[1]
# Charger le fichier CSV
df = pd.read_csv(arg, delimiter=",")


# Compter le nombre de connexions distinctes vers chaque destination
conn_counts = df.groupby("Destination").nunique()["Source"]

# Afficher les connexions distinctes par destination
print(conn_counts)
