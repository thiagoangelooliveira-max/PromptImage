import streamlit as st
from gerar_imagem import gerar_imagem
from editar_imagem import editar_imagem

st.set_page_config(page_title="PromptImage", page_icon="🎨")

if "imagem_gerada" not in st.session_state:
    st.session_state.imagem_gerada = None
if "imagem_editada" not in st.session_state:
    st.session_state.imagem_editada = None

st.markdown(
    '<style>'
    '.st-key-gerar_nova_versao button {background-color: #743bff; color: white; border-color: #743bff;}'
    '.st-key-gerar_nova_versao button:hover:not(:disabled) {background-color: #6026e6; border-color: #6026e6;}'
    '.st-key-gerar_nova_versao button:disabled {opacity: 0.5;}'
    '</style>'
    '<h1 style="text-align: center; color: #ffffff; padding-bottom: 0;">'
    'Prompt<span style="color: #007bff;">Image</span></h1>'
    '<p style="text-align: center; color: #94a3b8;">'
    'Crie e transforme imagens com IA.</p>',
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown('<h3 style="color: #FF4B4B;">1. Criar imagem</h3>', unsafe_allow_html=True)

    prompt = st.text_area(
        "Descreva como você quer a imagem.",
        placeholder="Ex.: Um cachorro brincando na praia ao pôr do sol...",
    )

    if st.button("✨ Criar imagem", type="primary"):
        if prompt.strip():
            try:
                with st.spinner("Gerando imagem..."):
                    st.session_state.imagem_gerada = gerar_imagem(prompt)
                    st.session_state.imagem_editada = None
            except Exception as erro:
                st.error(f"Não foi possível gerar a imagem: {erro}")
        else:
            st.warning("Descreva a imagem primeiro.")

    st.write("**Imagem gerada**")
    if st.session_state.imagem_gerada is not None:
        st.image(st.session_state.imagem_gerada)
    else:
        st.caption("A imagem gerada aparecerá aqui.")

with st.container(border=True):
    st.markdown('<h3 style="color: #A78BFA;">2. Editar imagem</h3>', unsafe_allow_html=True)

    edicao = st.text_area(
        "Descreva qual mudança você quer fazer na imagem.",
        placeholder="Ex.: Adicionar um chapéu no cachorro...",
    )

    if st.button(
        "✏️ Gerar nova versão",
        key="gerar_nova_versao",
        disabled=st.session_state.imagem_gerada is None,
    ):
        if edicao.strip():
            try:
                with st.spinner("Editando imagem..."):
                    st.session_state.imagem_editada = editar_imagem(edicao)
            except Exception as erro:
                st.error(f"Não foi possível editar a imagem: {erro}")
        else:
            st.warning("Descreva a mudança primeiro.")

    st.write("**Nova versão da imagem**")
    if st.session_state.imagem_editada is not None:
        st.image(st.session_state.imagem_editada)
    else:
        st.caption("A nova versão aparecerá aqui.")
