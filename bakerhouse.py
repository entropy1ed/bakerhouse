
import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_option_menu import option_menu
from streamlit_image_select import image_select


st.set_page_config(page_title="BakerHouse Ü",
                   page_icon=":doughnut:",
                   layout="centered"
                   )


def lluvia_donitas():
    rain(
        emoji="🍩",
        font_size=25,
        falling_speed=5,
        animation_length="infinite",
    )

def pag_inicio():
    inicio=st.container()
    
    col1,col2,col3=st.columns([1,2,1])
    
    with col2:
        st.title("  Baker House Ü", anchor=False,)
        st.subheader("  Te mereces unas donitas", anchor=False)
        st.video("bk_2.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=True)
        st.link_button("Pide tus donitas 😋", "https://wa.me/527531678466")
    
    
    
    
    
    
def pag_donitas():
    donitas=st.container()
    
    donitas.subheader("Dinámica de compra", anchor=False)
    donitas.divider()
    donitas.markdown("**Selecciona el tamaño de tu cajita 📦**")
    donitas.text("• 4 minidonitas \n• 9 minidonitas \n• 24 minidonitas\n\n\n\n\n\n")
    donitas.markdown("**Dinos el tipo de decoración y extras que te gustarían✨**")
    donitas.text("Puedes enviarnos fotos de referencia, también podemos agregar algunos extras \ncomo chispas, figuras, letras, etc.\n\n\n\n\n\n")
    donitas.markdown("**Métodos de entrega**🚚")
    donitas.text("Entregamos en el OXXO de la clínica Fátima o por mandadito con cargo al cliente\n\n\n\n\n\n")
    donitas.markdown("**❗IMPORTANTE pedir tus donitas con 3 días de anticipación❗💟**")
    donitas.markdown("**CONFIRMA TU PEDIDO CON EL 50% DE ANTICIPO✔️**")
    donitas.link_button("Pide tus donitas 😋", "https://wa.me/527531678466")
    

def pag_contacto():
    contacto=st.container()
    contacto.subheader("Contactanos por nuestras redes c:", anchor=False)
    contacto.link_button("visita nuestro instagram", "https://www.instagram.com/bakerhouselzc/")
    contacto.link_button("Pide tus donitas 😋", "https://wa.me/527531678466")
    img = image_select(
    label="Mira, ¡Donitas!",
    images=[
        "1.jpg",
        "2.jpg",
    ],
    captions=["Cliente agradecido", "Otro cliente c:"],
)
    st.image(img, width=500)
    

        
    



with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Inicio🏠", "Como comprar🍩", "Contacto📱"],
        icons=["dot", "dot", "dot"],
        menu_icon=["menu-button-wide-fill"]
    )

if selected == "Inicio🏠":
    pag_inicio()
if selected == "Como comprar🍩":
    pag_donitas()
if selected == "Contacto📱":
    pag_contacto()

lluvia_donitas()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)