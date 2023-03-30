#Projekt Nr. 5
#Ich wäre Ihnen sehr dankbar, wenn Sie mir eine kurze Mail schreiben, ob alles funktioniert, oder ob ein Problem aufgetreten ist. 

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('global_data_50mLC2.txt', header=None)
#Read a comma-separated values (csv) file into DataFrame
#15 Spalten sollten vorhanden sein

#Bennenung der Spalten mit Hilfe des Abstracts
elevation = data[0]
local_relief = data[1]
slope = data[2]
precipitation = data[3]
temperature = data[4]
NDVI_average = data[5]
NDVI_maximum = data[6]
latitude = data[7]
ksn = data[8]
tetrapod_species_richness = data[9]
amphibian_species_richness = data[10]
mammal_species_richness = data[11]
KöppenGeiger_Climate_Zone = data[12]
Landcover = data[13]
strain_rate = data[14] 

# Liste aus den Spalten, die die X-Achse bilden
remaining_columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14]

colnames= ("elevation","local_relief","slope","precipitation","temperature","NDVI_average","NDVI_maximum","latitude","ksn","tetrapod_species_richness","amphibian_species_richness","mammal_species_richness","KöppenGeiger_Climate_Zone","Landcover","strain_rate",)

#Alle x werte gegen einen y wert
for i in remaining_columns:
    # data.iloc wählt die Spalten nach ihren Indexpositionen 9,10,11 aus. 
    #ge(0)= nur werte größer als 0 werden ausgewählt
    #all(axis=1)Nur true werte auswählen
    #1.data:Nur die true values werden in einen neuen df übernommen
    filtered_data = data[data.iloc[:, [i, 9, 10, 11]].ge(0).all(axis=1)]
    
    # Die Summe aller Spezies werte für einen x wert wird berechnet und gruppiert
    grouped_data = filtered_data.groupby(i)[[9, 10, 11]].sum()
    #.index ruft die übrigen Spalten auf und plottet 9,10,11 gegen diese.
    plt.scatter(grouped_data.index, grouped_data[9], label='tetrapod_species_richness')
    plt.scatter(grouped_data.index, grouped_data[10], label='amphibian_species_richness')
    plt.scatter(grouped_data.index, grouped_data[11], label='mammal_species_richness')
    plt.legend()
    plt.xlabel(colnames[i])
    plt.ylabel('Number of animals')
    filename = 'First_Scatterplot_' + str(i) + '_KilianKlages.png'
    plt.savefig(filename)
    plt.show()
    
#Alle x werte gegen einen y wert als subplots
for i in remaining_columns:
    # data.iloc wählt die Spalten nach ihren Indexpositionen 9,10,11 aus. 
    #ge(0)= nur werte größer als 0 werden ausgewählt
    #all(axis=1)Nur true werte auswählen
    #1.data:Nur die true values werden in einen neuen df übernommen
    # Filter the input data to only include rows where the relevant columns have non-negative values
    filtered_data = data[data.iloc[:, [i, 9, 10, 11]].ge(0).all(axis=1)]
    
    # Die Summe aller Spezies werte für einen x wert wird berechnet und gruppiert
    grouped_data = filtered_data.groupby(i)[[9, 10, 11]].sum()
    
    # Subplot wird erstellt 
    fig, axs = plt.subplots(3, 1, figsize=(8, 8))
    
    # Scatter plot für tetrapod_species_richness
    axs[0].scatter(grouped_data.index, grouped_data[9], c='black', label='tetrapod_species_richness')
    axs[0].set_ylabel('Number of animals')
    axs[0].legend()
    
    # Scatter plot für amphibian_species_richness
    axs[1].scatter(grouped_data.index, grouped_data[10], c='green', label='amphibian_species_richness')
    axs[1].set_ylabel('Number of animals')
    axs[1].legend()
    
    # Scatter plot für mammal_species_richness
    axs[2].scatter(grouped_data.index, grouped_data[11], c='brown', label='mammal_species_richness')
    axs[2].set_xlabel(colnames[i])
    axs[2].set_ylabel('Number of animals')
    axs[2].legend()
    
    # Subplot Titel
    fig.suptitle(f"Relationship between {colnames[i]} and number of individual animals")
    filename = 'Second_Scatterplot_' + str(i) + '_KilianKlages.png'
    plt.savefig(filename)
    plt.show()
