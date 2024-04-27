
import streamlit as st
from typing import Union
from streamlit_extras.stylable_container import stylable_container
from st_clickable_images import clickable_images
import webbrowser
import base64


#82fff5
st.set_page_config(page_title="BakerHouse Ü",
                   page_icon=":doughnut:",
                   layout="centered"
                   )

with open('./olas.css') as f:
    css_bg = f.read()

st.markdown(f'<style>{css_bg}</style>', unsafe_allow_html=True)



def rain(
    emoji: str,
    font_size: int = 12,
    falling_speed: int = 5,
    animation_length: Union[int, str] = "infinite",
):
    """
    Creates a CSS animation where input emoji falls from top to bottom of the screen.

    Args:
        emoji (str): Emoji
        font_size (int, optional): Font size. Defaults to 64.
        falling_speed (int, optional): Speed at which the emoji 'falls'. Defaults to 5.
        animation_length (Union[int, str], optional): Length of the animation. Defaults to "infinite".
    """

    if isinstance(animation_length, int):
        animation_length = f"{animation_length}"

    st.write(
        f"""
    <style>

    body {{
    background: gray;
    }}

    .emoji {{
    color: #777;
    font-size: {font_size}px;
    font-family: Arial;
    // text-shadow: 0 0 5px #000;
    }}

    ///*delete for no hover-effect*/
    //.emoji:hover {{
    //  font-size: 60px;
    //  text-shadow: 5px 5px 5px white;
    //}}

    @-webkit-keyframes emojis-fall {{
    0% {{
        top: -10%;
    }}
    100% {{
        top: 100%;
    }}
    }}
    @-webkit-keyframes emojis-shake {{
    0% {{
        -webkit-transform: translateX(0px);
        transform: translateX(0px);
    }}
    50% {{
        -webkit-transform: translateX(20px);
        transform: translateX(20px);
    }}
    100% {{
        -webkit-transform: translateX(0px);
        transform: translateX(0px);
    }}
    }}
    @keyframes emojis-fall {{
    0% {{
        top: -10%;
    }}
    100% {{
        top: 100%;
    }}
    }}
    @keyframes emojis-shake {{
    0% {{
        transform: translateX(0px);
    }}
    25% {{
        transform: translateX(15px);
    }}
    50% {{
        transform: translateX(-15px);
    }}
    100% {{
        transform: translateX(0px);
    }}
    }}

    .emoji {{
    position: fixed;
    top: -10%;
    z-index: 99999;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    cursor: default;
    -webkit-animation-name: emojis-fall, emojis-shake;
    -webkit-animation-duration: 5s, 3s;
    -webkit-animation-timing-function: linear, ease-in-out;
    -webkit-animation-iteration-count: {animation_length}, {animation_length}; // overall length
    -webkit-animation-play-state: running, running;
    animation-name: emojis-fall, emojis-shake;
    animation-duration: {falling_speed}s, 3s;  // fall speed
    animation-timing-function: linear, ease-in-out;
    animation-iteration-count: {animation_length}, {animation_length}; // overall length
    animation-play-state: running, running;
    }}
    .emoji:nth-of-type(0) {{
    left: 1%;
    -webkit-animation-delay: 0s, 0s;
    animation-delay: 0s, 0s;
    }}
    .emoji:nth-of-type(1) {{
    left: 10%;
    -webkit-animation-delay: 1s, 1s;
    animation-delay: 1s, 1s;
    }}
    .emoji:nth-of-type(2) {{
    left: 20%;
    -webkit-animation-delay: 6s, 0.5s;
    animation-delay: 6s, 0.5s;
    }}
    .emoji:nth-of-type(3) {{
    left: 30%;
    -webkit-animation-delay: 4s, 2s;
    animation-delay: 4s, 2s;
    }}
    .emoji:nth-of-type(4) {{
    left: 40%;
    -webkit-animation-delay: 2s, 2s;
    animation-delay: 2s, 2s;
    }}
    .emoji:nth-of-type(5) {{
    left: 50%;
    -webkit-animation-delay: 8s, 3s;
    animation-delay: 8s, 3s;
    }}
    .emoji:nth-of-type(6) {{
    left: 60%;
    -webkit-animation-delay: 6s, 2s;
    animation-delay: 6s, 2s;
    }}
    .emoji:nth-of-type(7) {{
    left: 70%;
    -webkit-animation-delay: 2.5s, 1s;
    animation-delay: 2.5s, 1s;
    }}
    .emoji:nth-of-type(8) {{
    left: 80%;
    -webkit-animation-delay: 1s, 0s;
    animation-delay: 1s, 0s;
    }}
    .emoji:nth-of-type(9) {{
    left: 90%;
    -webkit-animation-delay: 3s, 1.5s;
    animation-delay: 3s, 1.5s;
    }}

    </style>
    """,
        unsafe_allow_html=True,
    )

    st.write(
        f"""
    <!--get emojis from https://getemoji.com-->
    <div class="emojis">
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

def lluvia_donitas():
    rain(
        emoji="🍩",
        font_size=25,
        falling_speed=5,
        animation_length="infinite",
    )


   
   
    colb1, colb2, colb3 =st.columns([1,1,1])
    
    with colb2:
            with stylable_container(
        key="bnt_nuevo",
        css_styles="""
            button {
                background-image: linear-gradient(to right, #C9FFBF 0%, #FFAFBD  51%, #C9FFBF  100%);
                margin: 10px;
                padding: 5px 10px;
                text-align: center;
                text-transform: uppercase;
                transition: 0.5s;
                background-size: 200% auto;
                color: black;            
                box-shadow: 0 0 10px #eee;
                border-radius: 5px;
                display: block;
            }
            
            button:hover {
                background-position: right center; /* change the direction of the change here */
                color: #fff;
                text-decoration: none;
            }   
            """,
    ):
                
                def link_btn_():
                    webbrowser.open_new("https://wa.me/527531678466")
                
                st.button("Pide tus donitas 😋", on_click=link_btn_)
     
       
    st.title("  Baker House Ü", anchor=False,)
    st.subheader("  Te mereces unas donitas", anchor=False)
    
    images = []
    for file in ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"]:
        with open(file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images.append(f"data:image/jpeg;base64,{encoded}")

    clicked = clickable_images(
        images,
        titles=[f"Image #{str(i)}" for i in range(len(images))],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "1px", "height": "210px"},
    )

    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
    
    
    
    
    st.subheader("Dinámica de compra 👇", anchor=False)
    exp1=st.expander("VER DINÁMICA")
    
    exp1.write("**Selecciona el tamaño de tu cajita 📦**")
    exp1.write("""• 4 minidonitas 
               \n• 9 minidonitas 
               \n• 24 minidonitas\n\n\n\n\n\n""")
    exp1.write("**Dinos el tipo de decoración y extras que te gustarían✨**")

    exp1.write("Puedes enviarnos fotos de referencia, también podemos agregar algunos extras \ncomo chispas, figuras, letras, etc.\n\n\n\n\n\n")
    exp1.markdown("**Métodos de entrega**🚚")
    exp1.write("Entregamos en el OXXO de la clínica Fátima o por mandadito con cargo al cliente\n\n\n\n\n\n")
    exp1.markdown("**❗IMPORTANTE pedir tus donitas con 3 días de anticipación❗💟**")
    exp1.markdown("**CONFIRMA TU PEDIDO CON EL 50% DE ANTICIPO✔️**")
    
    colb1, colb2, colb3 =st.columns([1,1,1])
    with colb2:
        with stylable_container(
            key="bnt_nuevo2",
            css_styles="""
                button {
                    background-image: linear-gradient(to right, #C9FFBF 0%, #FFAFBD  51%, #C9FFBF  100%);
                    margin: 10px;
                    padding: 5px 10px;
                    text-align: center;
                    text-transform: uppercase;
                    transition: 0.5s;
                    background-size: 200% auto;
                    color: black;            
                    box-shadow: 0 0 10px #eee;
                    border-radius: 5px;
                    display: block;
                }
                
                button:hover {
                    background-position: right center; /* change the direction of the change here */
                    color: #fff;
                    text-decoration: none;
                }   
                """,
        ):
                    
                    def link_btn_():
                        webbrowser.open_new("https://wa.me/527531678466")
                    
                    st.button("Pide tus donitas 😋", on_click=link_btn_, key="bnt_nuevo2")

        
        

    

    
    
    
    
    





lluvia_donitas()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)