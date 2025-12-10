import streamlit as st
import donnees_agricoles as db
from openai import OpenAI # L'outil pour parler à l'IA

# --- CONFIGURATION ---
st.set_page_config(page_title="Agri-Senegal IA", page_icon="🇸🇳", layout="centered")

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/fd/Flag_of_Senegal.svg", width=50)
    st.header("Paramètres")
    langue_choisie = st.radio("Langue", ["Français 🇫🇷", "Wolof 🇸🇳"])
    
    # Configuration des textes selon la langue
    if "Wolof" in langue_choisie:
        code_langue = "wo"
        txt_titre = "Samm Sa Tol - IA"
        txt_intro = "Tànnal sa meññent wala nga laaj IA bi."
        txt_choix = "Ban meññent nga soxla ?"
        txt_calcul = "🧮 Calculateur Semence"
        txt_surface = "Sa tol numu tollu ? (Hectares)"
        txt_res_sem = "Li ngay soxla ci jiwu :"
        txt_ia_titre = "🤖 Assistant IA (Doktör Tol)"
        txt_ia_intro = "Posez une question sur l'agriculture (Maladies, Climat...)"
        txt_ia_input = "Bindal sa laaj fi..."
        txt_ia_bouton = "Laaj (Demander)"
    else:
        code_langue = "fr"
        txt_titre = "Assistant Agricole Sénégal"
        txt_intro = "Sélectionnez une culture ou posez une question à l'IA."
        txt_choix = "Quelle culture vous intéresse ?"
        txt_calcul = "🧮 Calculateur de Semences"
        txt_surface = "Quelle est la surface de votre champ ? (Hectares)"
        txt_res_sem = "Quantité de semences nécessaire :"
        txt_ia_titre = "🤖 Assistant IA Intelligent"
        txt_ia_intro = "Posez n'importe quelle question technique (Maladie, Météo, Engrais...)"
        txt_ia_input = "Écrivez votre question ici..."
        txt_ia_bouton = "Demander à l'IA"

# --- CONTENU PRINCIPAL ---
st.title(f"🌾 {txt_titre}")
st.write(txt_intro)

# 1. SECTION CLASSIQUE (BASE DE DONNÉES)
st.divider()
liste_cles = list(db.cultures.keys())
options_menu = {db.cultures[cle][code_langue]['nom']: cle for cle in liste_cles}

choix_nom = st.selectbox(txt_choix, list(options_menu.keys()))
cle = options_menu[choix_nom]
info = db.cultures[cle]
txt = info[code_langue]

st.subheader(txt['nom'])
st.image(info['image'], use_container_width=True)

c1, c2 = st.columns(2)
with c1:
    st.info(f"**📅 Semis:**\n{txt['semis']}")
    st.warning(f"**🦠 Santé:**\n{txt['maladie']}")
with c2:
    st.info(f"**💧 Eau:**\n{txt['irrigation']}")
    st.success(f"**💡 Conseil:**\n{txt['conseil']}")

# 2. SECTION CALCULATEUR
st.divider()
st.subheader(txt_calcul)
surf = st.number_input(txt_surface, min_value=0.1, value=1.0, step=0.5)
if info['besoin_semence'] > 0:
    st.metric(txt_res_sem, f"{surf * info['besoin_semence']:.1f} kg")
else:
    st.write("Pas de calcul pour cette culture.")

# 3. SECTION INTELLIGENCE ARTIFICIELLE (CHATGPT)
st.divider()
st.header(txt_ia_titre)
st.write(txt_ia_intro)

# Zone de texte pour la question
question_user = st.text_area(txt_ia_input)

if st.button(txt_ia_bouton, type="primary"):
    if not question_user:
        st.error("Veuillez écrire une question.")
    else:
        # On vérifie si la clé existe (Sécurité)
        if "OPENAI_API_KEY" not in st.secrets:
            st.error("⚠️ La clé API OpenAI est manquante dans les paramètres.")
            st.info("Ajoutez votre clé dans les 'Secrets' de Streamlit Cloud.")
        else:
            with st.spinner("L'IA réfléchit... / IA bi ngi xalaat..."):
                try:
                    # Connexion à l'IA
                    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                    
                    # Le message envoyé à l'IA
                    reponse = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "Tu es un agronome expert du Sénégal. Tu réponds courtement et simplement. Si on te parle Wolof, réponds en Wolof."},
                            {"role": "user", "content": question_user}
                        ]
                    )
                    
                    # Affichage de la réponse
                    resultat = reponse.choices[0].message.content
                    st.success("Réponse de l'IA :")
                    st.write(resultat)
                    
                except Exception as e:
                    st.error(f"Erreur de connexion : {e}")