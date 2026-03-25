import streamlit as st
import random

st.title("""Number Guest Game Let's Play!""")
st.write("1 100 Arasinda bir sayi tuttum.Hadi bulda gorim")

if "dogrusayi" not in st.session_state:
    st.session_state.dogrusayi= random.randint(1,100)
    st.session_state.hak=10
    st.session_state.mesaj=""

tahmin = st.number_input("Bulamayacagin Tahminini Gir",min_value=1,max_value=100,step=1)

if st.button("Tahmini Yolllaaaa"):
    if st.session_state.hak>0:
        if tahmin == st.session_state.dogrusayi:
            st.session_state.mesaj="TEBRIKLERRRR DOGRU BILDIN VAVAVAV"
        elif tahmin > st.session_state.dogrusayi:
            st.session_state.hak-=1
            st.session_state.mesaj=f"Daha kucuk bir sayi deneeeee.Kalan hakkin ise{st.session_state.hak}"
        else:
            st.session_state.hak-=1
            st.session_state.mesaj=f"Daha buyuk bir sayi deneeeee.Kalan hakkin ise{st.session_state.hak}"

    if st.session_state.hak==0 and tahmin != st.session_state.dogrusayi:
        st.session_state.mesaj=f"Bak ne dedim bilemedin ehehe.He bide sayi{st.session_state.dogrusayi}"

st.write(st.session_state.mesaj)
if st.button("Oyunu Yeniden Baslat"):
    st.balloons()
    st.session_state.dogrusayi=random.randint(1,100)
    st.session_state.hak=10
    st.session_state.mesaj=""

