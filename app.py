import streamlit as st

# 1. КОНФИГУРАЦИЯ СТРАНИЦЫ
st.set_page_config(page_title="VibeFlow Premium", page_icon="🎵", layout="centered")

# 2. ДИЗАЙН (CSS) - СТЕКЛО, ГРАДИЕНТЫ И АНИМАЦИЯ
st.markdown("""
    <style>
    /* Глубокий космический фон */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }

    /* Эффект матового стекла для карточек */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }

    /* Стильные интерактивные кнопки */
    .stButton>button {
        width: 100%;
        border-radius: 18px;
        height: 3.8em;
        background: linear-gradient(90deg, #1DB954, #1ed760);
        color: white;
        border: none;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        transition: all 0.4s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 25px rgba(29, 185, 84, 0.7);
        color: white;
    }

    /* Заголовок с неоновым свечением */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: -1px;
        margin-bottom: 30px;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. БАЗА ПЛЕЙЛИСТОВ
DATA = {
    "Party": {"title": "ENERGY BOOST ⚡", "url": "https://www.youtube.com/watch?v=5qap5aO4i9A", "desc": "Взрывной ритм для тех, кто готов покорять мир прямо сейчас!"},
    "Focus": {"title": "DEEP FOCUS 🧠", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk", "desc": "Чистый поток звуков для максимальной концентрации на важном."},
    "Relax": {"title": "CHILL VIBES ☕", "url": "https://www.youtube.com/watch?v=lTRiuFIWV5k", "desc": "Медленные мелодии, которые окутывают уютом и спокойствием."},
    "Dream": {"title": "NIGHT DREAMS 🌙", "url": "https://www.youtube.com/watch?v=kgx4WGK0oNU", "desc": "Атмосферный саундтрек для погружения в глубокие сновидения."}
}

# 4. ИНИЦИАЛИЗАЦИЯ СОСТОЯНИЯ
if 'step' not in st.session_state: st.session_state.step = 1
if 'favs' not in st.session_state: st.session_state.favs = []

st.markdown("<div class='main-title'>VIBEFLOW</div>", unsafe_allow_html=True)

# 5. САЙДБАР (ИЗБРАННОЕ)
with st.sidebar:
    st.markdown("### ⭐ Твои Сохранения")
    if not st.session_state.favs:
        st.write("Пока здесь пусто...")
    else:
        for f in st.session_state.favs:
            st.markdown(f"<div style='background:rgba(255,255,255,0.05); padding:10px; border-radius:12px; margin-bottom:8px; border-left: 4px solid #1DB954;'>{f}</div>", unsafe_allow_html=True)
    if st.button("Очистить историю"):
        st.session_state.favs = []
        st.rerun()

# 6. КОНТЕНТ ПРИЛОЖЕНИЯ
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

if st.session_state.step == 1:
    st.subheader("Как ты себя чувствуешь сейчас?")
    if st.button("🚀 ЗАРЯЖЕН ЭНЕРГИЕЙ"):
        st.session_state.energy = "high"
        st.session_state.step = 2
        st.rerun()
    if st.button("☁️ ХОЧУ ПОКОЯ"):
        st.session_state.energy = "low"
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.subheader("Что у тебя в планах?")
    if st.session_state.energy == "high":
        if st.button("ДВИГАТЬСЯ / ГУЛЯТЬ"): st.session_state.res = "Party"; st.session_state.step = 3; st.rerun()
        if st.button("РАБОТАТЬ / УЧИТЬСЯ"): st.session_state.res = "Focus"; st.session_state.step = 3; st.rerun()
    else:
        if st.button("ПРОСТО ОТДЫХАТЬ"): st.session_state.res = "Relax"; st.session_state.step = 3; st.rerun()
        if st.button("ГОТОВИТЬСЯ КО СНУ"): st.session_state.res = "Dream"; st.session_state.step = 3; st.rerun()elif st.session_state.step == 3:
    item = DATA[st.session_state.res]
    st.markdown(f"<h2 style='color:#1DB954;'>{item['title']}</h2>", unsafe_allow_html=True)
    st.write(item['desc'])
    st.video(item['url'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("❤️ СОХРАНИТЬ"):
            if item['title'] not in st.session_state.favs:
                st.session_state.favs.append(item['title'])
                st.toast("Добавлено в Избранное!")
    with col2:
        if st.button("🔄 ЗАНОВО"):
            st.session_state.step = 1
            st.rerun()

st.markdown("</div>", unsafe_allow_html=True)