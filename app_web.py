import streamlit as st
import donnees_agricoles as db

# 1. Configuration de la page (Doit toujours être la première ligne)
st.set_page_config(
    page_title="Agri-Senegal IA", 
    page_icon="🇸🇳",
    layout="centered" # Centre le contenu comme sur un mobile
)

# 2. Barre latérale (Menu de gauche)
with st.sidebar:
    st.header("🇸🇳 Agri-Senegal")
    st.write("Votre assistant agricole de poche.")
    st.write("---")
    st.info("💡 Astuce : Utilisez ce menu pour changer rapidement de culture.")

# 3. Titre principal avec un style
st.title("🌾 Assistant Agricole")
st.markdown("Bienvenue. Sélectionnez une culture pour voir **le calendrier**, **l'irrigation** et **les conseils santé**.")

# 4. Le choix de la culture (avec des icônes)
# On crée un dictionnaire pour lier le nom affiché à la clé de la base de données
options_affichage = {
    "🥜 Arachide": "arachide",
    "🌾 Mil": "mil",
    "🧅 Oignon": "oignon",
    "🍚 Riz": "riz",
    "🥭 Mangue": "mangue"
}

# L'utilisateur choisit dans la liste avec les icônes
choix_utilisateur = st.selectbox("Je veux des infos sur :", list(options_affichage.keys()))

# On récupère la vraie clé (ex: "🥜 Arachide" devient "arachide")
cle_culture = options_affichage[choix_utilisateur]

# 5. Dictionnaire des images (Liens internet)
images = {
    "arachide": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Arachis_hypogaea_-_Köhler–s_Medizinal-Pflanzen-013.jpg/433px-Arachis_hypogaea_-_Köhler–s_Medizinal-Pflanzen-013.jpg",
    "mil": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Pearl_millet_close_up.jpg/440px-Pearl_millet_close_up.jpg",
    "oignon": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Onion_on_White.JPG/480px-Onion_on_White.JPG",
    "riz": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Oryza_sativa_-_Köhler–s_Medizinal-Pflanzen-104.jpg/407px-Oryza_sativa_-_Köhler–s_Medizinal-Pflanzen-104.jpg",
    "mangue": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Hapus_Mango.jpg/440px-Hapus_Mango.jpg"
}

# 6. Affichage des résultats
if st.button("🔍 Analyser la culture"):
    
    st.divider() # Ligne de séparation
    
    # Récupération des données
    info = db.cultures[cle_culture]
    
    # Affichage de l'image centrée
    if cle_culture in images:
        st.image(images[cle_culture], caption=f"Culture : {choix_utilisateur}", use_container_width=True)

    # Affichage des informations dans des "onglets" (Tabs)
    # C'est très moderne et facile à lire
    tab1, tab2, tab3 = st.tabs(["📅 Semis & Eau", "🦠 Santé & Maladies", "💡 Conseil Expert"])
    
    with tab1:
        st.subheader("Calendrier Agricole")
        st.success(f"**Période de semis :** {info['semis']}")
        st.info(f"**Besoins en eau :** {info['irrigation']}")
        
    with tab2:
        st.subheader("Prévention des maladies")
        st.warning(f"**Attention à :** {info['maladie']}")
        
    with tab3:
        st.subheader("Le conseil du technicien")
        st.write(info['conseil'])

# Pied de page
st.write("---")
st.caption("Développé pour l'agriculture sénégalaise. Version 2.0")