# Fichier : donnees_agricoles.py

# On stocke les infos avec une clé pour l'image, et des sous-clés pour les langues
cultures = {
    "arachide": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Arachis_hypogaea_-_Köhler–s_Medizinal-Pflanzen-013.jpg/433px-Arachis_hypogaea_-_Köhler–s_Medizinal-Pflanzen-013.jpg",
        "besoin_semence": 100, # kg par hectare (exemple)
        "fr": {
            "nom": "Arachide",
            "semis": "Juin - Juillet (dès les premières pluies utiles)",
            "irrigation": "Pluvial (Hivernage). Besoins critiques à la floraison.",
            "maladie": "Attention à la Rosette et l'Aflatoxine.",
            "conseil": "Utilisez des variétés comme la Fleur 11."
        },
        "wo": {
            "nom": "Gerté",
            "semis": "Nawet (Juin - Juillet), sou tawé ba souff toy.",
            "irrigation": "Nawet rek la soxla. Bumu manqué ndox buy meñ.",
            "maladie": "Moytul fébarou Rosette ak Aflatoxine.",
            "conseil": "Dieufeundikol jiwu Fleur 11."
        }
    },
    "mil": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Pearl_millet_close_up.jpg/440px-Pearl_millet_close_up.jpg",
        "besoin_semence": 8, # kg par hectare
        "fr": {
            "nom": "Mil",
            "semis": "Après la première bonne pluie (juillet).",
            "irrigation": "Résistant à la sécheresse.",
            "maladie": "Surveillez le Mildiou et les insectes.",
            "conseil": "Associez le mil avec le niébé."
        },
        "wo": {
            "nom": "Dugub",
            "semis": "Bu tawé ba souff toy (Juillet).",
            "irrigation": "Dafay muñ coono, du soxla ndox bu barri.",
            "maladie": "Moytul Mildiou ak yoo yi.",
            "conseil": "Boxalel Dugub ak Niébé, dayaral souff."
        }
    },
    "oignon": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Onion_on_White.JPG/480px-Onion_on_White.JPG",
        "besoin_semence": 4, # kg par hectare
        "fr": {
            "nom": "Oignon",
            "semis": "Octobre à Décembre (Pépinière).",
            "irrigation": "Arrosage régulier matin et soir.",
            "maladie": "Attention aux thrips.",
            "conseil": "Variété Violet de Galmi recommandée."
        },
        "wo": {
            "nom": "Soablé",
            "semis": "Octobre ba Décembre ci pépinière.",
            "irrigation": "Roso suba ak ngoon.",
            "maladie": "Moytul thrips (gunóor).",
            "conseil": "Jiwu Violet de Galmi mo gueun."
        }
    },
    "riz": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Oryza_sativa_-_Köhler–s_Medizinal-Pflanzen-104.jpg/407px-Oryza_sativa_-_Köhler–s_Medizinal-Pflanzen-104.jpg",
        "besoin_semence": 80, 
        "fr": {
            "nom": "Riz",
            "semis": "Hivernage ou Contre-saison.",
            "irrigation": "Submersion contrôlée.",
            "maladie": "Pyriculariose.",
            "conseil": "Utilisez Sahel 108."
        },
        "wo": {
            "nom": "Maalo",
            "semis": "Nawet wala Contre-saison.",
            "irrigation": "Na nek ci biir ndox.",
            "maladie": "Fébaru Pyriculariose.",
            "conseil": "Jiwu Sahel 108 mo gueun."
        }
    },
    "mangue": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Hapus_Mango.jpg/440px-Hapus_Mango.jpg",
        "besoin_semence": 0, # Pas pertinent
        "fr": {
            "nom": "Mangue",
            "semis": "Début hivernage (Greffage).",
            "irrigation": "Régulier au début.",
            "maladie": "Mouche des fruits.",
            "conseil": "Variété Kent pour l'export."
        },
        "wo": {
            "nom": "Mango",
            "semis": "Bu nawet commencé (Greffage).",
            "irrigation": "Roso bu bax bu ndawé.",
            "maladie": "Gunóorou mango yi.",
            "conseil": "Variété Kent mo bakh ci export."
        }
    }
}