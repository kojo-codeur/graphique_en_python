# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt  # Pour créer des graphiques
import numpy as np  # Pour les opérations mathématiques

# Configuration de l'affichage pour les caractères spéciaux
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']  # Police qui supporte les caractères français
plt.rcParams['axes.unicode_minus'] = False  # Pour afficher correctement le signe moins

# Données pour les graphiques
mois = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']  # Liste des mois abrégés
ventes_2023 = [45, 52, 48, 55, 62, 75, 82, 78, 65, 58, 68, 85]  # Ventes mensuelles 2023 (en milliers d'euros)
ventes_2024 = [50, 55, 52, 60, 68, 80, 88, 85, 72, 65, 75, 92]  # Ventes mensuelles 2024 (en milliers d'euros) et ajouter d'autre années si vous voulaiz comme on a vue

categories = ['Électronique', 'Vêtements', 'Livres', 'Sport', 'Maison']  # Catégories de produits
pourcentages = [30, 25, 15, 20, 10]  # Pourcentage des ventes par catégorie
couleurs = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']  # Codes couleur pour chaque catégorie

# =============================================================================
# 1. GRAPHIQUE LINÉAIRE - Comparaison des ventes 2023 vs 2024
# =============================================================================

plt.figure(figsize=(12, 6))  # Crée une nouvelle figure de 12 pouces de large par 6 de haut

# Trace la ligne des ventes 2023
plt.plot(mois, ventes_2023,  # Données : mois en X, ventes_2023 en Y
         marker='o',         # Marqueur rond pour chaque point de données
         linewidth=2,        # Épaisseur de la ligne
         label='2023',       # Étiquette pour la légende
         color='blue')       # Couleur de la ligne

# Trace la ligne des ventes 2024
plt.plot(mois, ventes_2024,  # Données : mois en X, ventes_2024 en Y
         marker='s',         # Marqueur carré pour chaque point de données
         linewidth=2,        # Épaisseur de la ligne
         label='2024',       # Étiquette pour la légende
         color='red')        # Couleur de la ligne

plt.title('Évolution des ventes mensuelles 2023 vs 2024', fontsize=14, fontweight='bold')  # Titre du graphique
plt.xlabel('Mois')                    # Étiquette de l'axe horizontal
plt.ylabel('Ventes (milliers d\'euros)')  # Étiquette de l'axe vertical
plt.grid(True, alpha=0.3)             # Affiche une grille avec transparence de 30%
plt.legend()                          # Affiche la légende
plt.tight_layout()                    # Ajuste automatiquement l'espacement
plt.show()                            # Affiche le graphique

# =============================================================================
# 2. DIAGRAMME EN BARRES - Répartition par catégorie
# =============================================================================

plt.figure(figsize=(10, 6))  # Nouvelle figure de 10x6 pouces

# Crée les barres pour chaque catégorie
bars = plt.bar(categories,          # Noms des catégories
               pourcentages,        # Hauteur des barres (pourcentages)
               color=couleurs,      # Couleurs personnalisées
               edgecolor='black',   # Couleur des bordures
               linewidth=1.2)       # Épaisseur des bordures

plt.title('Répartition des ventes par catégorie', fontsize=14, fontweight='bold')  # Titre
plt.ylabel('Pourcentage (%)')       # Étiquette axe vertical
plt.xticks(rotation=45)             # Rotation des étiquettes de l'axe X à 45 degrés

# Ajoute les valeurs au-dessus de chaque barre
for bar, valeur in zip(bars, pourcentages):  # Parcourt chaque barre et sa valeur
    plt.text(bar.get_x() + bar.get_width()/2,  # Position X : centre de la barre
             bar.get_height() + 0.5,           # Position Y : juste au-dessus de la barre
             f'{valeur}%',                     # Texte à afficher
             ha='center',                      # Alignement horizontal au centre
             va='bottom',                      # Alignement vertical en bas
             fontweight='bold')                # Texte en gras

plt.tight_layout()  # Ajuste l'espacement
plt.show()          # Affiche le graphique

# =============================================================================
# 3. DIAGRAMME EN SECTEURS (Camembert) - Répartition par catégorie
# =============================================================================

plt.figure(figsize=(8, 8))  # Nouvelle figure carrée de 8x8 pouces

# Crée le diagramme circulaire
plt.pie(pourcentages,                    # Données des pourcentages
        labels=categories,               # Étiquettes pour chaque secteur
        autopct='%1.1f%%',               # Format d'affichage des pourcentages (1 décimale)
        startangle=90,                   # Angle de départ (en haut)
        colors=couleurs,                 # Couleurs personnalisées
        shadow=True,                     # Ajoute une ombre pour l'effet 3D
        explode=(0.1, 0, 0, 0, 0))      # Détache le premier secteur (Électronique) de 10%

plt.title('Répartition des ventes par catégorie', fontsize=14, fontweight='bold')  # Titre
plt.axis('equal')  # Assure que le cercle est parfaitement rond
plt.show()         # Affiche le graphique

# =============================================================================
# 4. GRAPHIQUE COMBINÉ - Deux sous-graphiques côte à côte
# =============================================================================

# Crée une figure avec 2 sous-graphiques horizontaux
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))  # 1 ligne, 2 colonnes, taille 15x6

# ==================== SOUS-GRAPHIQUE 1 ====================
# Graphique combiné ligne + barres

# Trace la ligne des ventes 2023
ax1.plot(mois, ventes_2023, 
         marker='o', 
         linewidth=2, 
         label='Ventes 2023', 
         color='navy')  # Bleu marine

ax1.set_xlabel('Mois')                              # Étiquette axe X
ax1.set_ylabel('Ventes 2023 (milliers €)', color='navy')  # Étiquette axe Y gauche
ax1.tick_params(axis='y', labelcolor='navy')        # Couleur des ticks de l'axe Y
ax1.grid(True, alpha=0.3)                           # Grille avec transparence

# Crée un deuxième axe Y pour les barres (partage le même axe X)
ax2_bar = ax1.twinx()  # twinx() crée un axe Y jumeau (partage l'axe X)

# Trace les barres des ventes 2024
ax2_bar.bar(mois, ventes_2024, 
            alpha=0.7,           # Transparence à 70%
            label='Ventes 2024', 
            color='orange')      # Couleur orange

ax2_bar.set_ylabel('Ventes 2024 (milliers €)', color='orange')  # Étiquette axe Y droit
ax2_bar.tick_params(axis='y', labelcolor='orange')              # Couleur des ticks

ax1.set_title('Comparaison des ventes 2023 (ligne) et 2024 (barres)')  # Titre

# Combine les légendes des deux axes
lines1, labels1 = ax1.get_legend_handles_labels()    # Légende de l'axe gauche
lines2, labels2 = ax2_bar.get_legend_handles_labels() # Légende de l'axe droit
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')  # Légende combinée

# ==================== SOUS-GRAPHIQUE 2 ====================
# Diagramme en barres horizontales

ax2.barh(categories,          # Barres horizontales (catégories en Y)
         pourcentages,        # Longueur des barres (pourcentages en X)
         color=couleurs,      # Couleurs personnalisées
         edgecolor='black')   # Bordures noires

ax2.set_xlabel('Pourcentage (%)')    # Étiquette axe X
ax2.set_title('Ventes par catégorie (horizontal)')  # Titre
ax2.grid(True, alpha=0.3, axis='x')  # Grille uniquement sur l'axe X

# Ajoute les valeurs à droite de chaque barre
for i, (cat, val) in enumerate(zip(categories, pourcentages)):
    ax2.text(val + 1,        # Position X : valeur + 1 (pour décaler)
             i,              # Position Y : index de la catégorie
             f'{val}%',      # Texte à afficher
             va='center',    # Alignement vertical au centre
             fontweight='bold')  # Texte en gras

plt.tight_layout()  # Ajuste l'espacement entre les sous-graphiques
plt.show()          # Affiche la figure complète

# =============================================================================
# STATISTIQUES SUPPLÉMENTAIRES - Calculs et affichage dans la console
# =============================================================================

print(f"Ventes totales 2023: {sum(ventes_2023):.0f}K €")  # Somme arrondie sans décimale
print(f"Ventes totales 2024: {sum(ventes_2024):.0f}K €")  # Somme arrondie sans décimale

# Calcul du pourcentage d'augmentation
augmentation = ((sum(ventes_2024) - sum(ventes_2023)) / sum(ventes_2023) * 100)
print(f"Augmentation: {augmentation:.1f}%")  # Affichage avec 1 décimale
