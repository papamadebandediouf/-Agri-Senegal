# Fichier: donnees_agricoles.py

cultures = {
    "arachide": {
        "semis": "Juin - Juillet (dès les premières pluies utiles)",
        "irrigation": "Pluvial (Hivernage). Besoins critiques à la floraison.",
        "maladie": "Attention à la Rosette et l'Aflatoxine. Séchez bien les gousses.",
        "conseil": "Utilisez des variétés comme la Fleur 11 pour le bassin arachidier."
    },
    "mil": {
        "semis": "Après la première bonne pluie (juillet).",
        "irrigation": "Résistant à la sécheresse, culture pluviale.",
        "maladie": "Surveillez le Mildiou et les insectes foreurs de tiges.",
        "conseil": "Associez le mil avec le niébé pour enrichir le sol."
    },
    "oignon": {
        "semis": "Pépinière : Octobre à Décembre. Repiquage 45 jours après.",
        "irrigation": "Régulière. Arrêter 2 semaines avant la récolte.",
        "maladie": "Attention aux thrips et à la pourriture du collet.",
        "conseil": "Zone des Niayes : privilégiez la variété Violet de Galmi."
    },
    "riz": {
        "semis": "Vallée du fleuve : Juin/Juillet (Hivernage) ou Février (Contre-saison).",
        "irrigation": "Irrigation par submersion contrôlée.",
        "maladie": "Attention à la pyriculariose (taches sur les feuilles).",
        "conseil": "Utilisez des semences certifiées (Sahel 108, Nerica)."
    },
    "mangue": {
        "semis": "Plantation des greffons en début d'hivernage.",
        "irrigation": "Arrosage régulier les 2 premières années.",
        "maladie": "Mouche des fruits : utilisez des pièges à phéromones.",
        "conseil": "La variété Kent est très prisée pour l'exportation."
    }
}

def obtenir_info(culture):
    culture = culture.lower()
    if culture in cultures:
        return cultures[culture]
    else:
        return None