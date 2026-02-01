import streamlit as st
import random

# --- SETTINGS & STYLE ---
st.set_page_config(page_title="HACCP Hero", page_icon="🛡️", layout="wide")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stProgress > div > div > div > div { background-color: #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

# --- DATA ---
if 'm_data' not in st.session_state:
    st.session_state.m_data = [
        {"col": "Operation or process", "q": "What is the test object?", "detail": "Part of the process or operation to be checked"},
        {"col": "Verification activity", "q": "What to check?", "detail": "Actions to verify if hygienic practices are correct"},
        {"col": "Check procedure", "q": "How should verification be done?", "detail": "Time, conditions, place and procedure for checks"},
        {"col": "Frequency", "q": "How often?", "detail": "Planned periodicity of the checks"},
        {"col": "Person in charge", "q": "Who should do it?", "detail": "Person responsible for verification activities"},
        {"col": "Record", "q": "How are results recorded?", "detail": "Models to record results and incidents"}
    ]
    st.session_state.p_data = [
        {"p": "Principle 1", "desc": "Analyze hazards", "ex": "Growth of microorganisms"},
        {"p": "Principle 2", "desc": "Determine CCP", "ex": "Identifying steps to prevent hazards"},
        {"p": "Principle 3", "desc": "Set critical limits", "ex": "Additive: 2-2.5g/Kg"},
        {"p": "Principle 4", "desc": "Surveillance system", "ex": "Supervising weighing and adding"},
        {"p": "Principle 5", "desc": "Corrective measures", "ex": "Decide what to do if amount is wrong"},
        {"p": "Principle 6", "desc": "System verification", "ex": "Product samples, calibrated scales"},
        {"p": "Principle 7", "desc": "Documentation", "ex": "Register of additive weights"}
    ]
    st.session_state.t_data = [
        {"item": "Reception control record", "a": "INPUTS"}, {"item": "Save tags", "a": "INPUTS"},
        {"item": "Updated supplier list", "a": "INPUTS"}, {"item": "Daily production list", "a": "PROCESS"},
        {"item": "Exit sheet warehouse", "a": "PROCESS"}, {"item": "Recipes / Formulas", "a": "PROCESS"},
        {"item": "Production sheets", "a": "PROCESS"}, {"item": "Warehouse departures", "a": "OUTPUTS"},
        {"item": "Sales record", "a": "OUTPUTS"}, {"item": "Sales tickets", "a": "OUTPUTS"},
        {"item": "Transportation vouchers", "a": "OUTPUTS"}
    ]
    random.shuffle(st.session_state.m_data)
    random.shuffle(st.session_state.p_data)
    random.shuffle(st.session_state.t_data)
    st.session_state.hp = 3
    st.session_state.score = 0
    st.session_state.level = 1
    st.session_state.idx = 0

# --- GAME HEADER ---
st.title("🛡️ HACCP Exam Quest")
st.write("Complete the 3 missions using your course material!")

# --- VISUAL HEALTH BAR ---
hp_color = "green" if st.session_state.hp > 1 else "red"
st.subheader(f"Health Points: {st.session_state.hp}/3")
st.progress(st.session_state.hp / 3)

if st.session_state.hp <= 0:
    st.error("💀 GAME OVER! The health inspector closed the kitchen.")
    if st.button("Restart Exam"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()
else:
    # --- MISSION 1: METHODOLOGY ---
    if st.session_state.level == 1:
        st.header("Mission 1: The Methodology Table")
        item = st.session_state.m_data[st.session_state.idx]
        
        with st.expander("📖 Need Help? Click to see Table 1"):
            st.table(st.session_state.m_data)

        st.info(f"**Task:** {item['q']}\n\n**Details:** {item['detail']}")
        ans = st.selectbox("Which Column is this?", sorted(list(set([x['col'] for x in st.session_state.m_data]))))
        
        if st.button("Submit Answer"):
            if ans == item['col']:
                st.success("✨ Correct!")
                st.session_state.score += 10
                st.session_state.idx += 1
                if st.session_state.idx >= len(st.session_state.m_data):
                    st.session_state.level = 2
                    st.session_state.idx = 0
                st.rerun()
            else:
                st.error("❌ Wrong column. -1 HP")
                st.session_state.hp -= 1
                st.rerun()

    # --- MISSION 2: PRINCIPLES ---
    elif st.session_state.level == 2:
        st.header("Mission 2: The 7 Principles")
        item = st.session_state.p_data[st.session_state.idx]
        
        with st.expander("📖 Need Help? Click to see Principles"):
            st.table(st.session_state.p_data)

        st.warning(f"**Description:** {item['desc']}\n\n**Example:** {item['ex']}")
        ans = st.radio("Choose the correct Principle:", [f"Principle {i}" for i in range(1,8)])
        
        if st.button("Verify Principle"):
            if ans == item['p']:
                st.success("✅ Perfect!")
                st.session_state.score += 10
                st.session_state.idx += 1
                if st.session_state.idx >= len(st.session_state.p_data):
                    st.session_state.level = 3
                    st.session_state.idx = 0
                st.rerun()
            else:
                st.error("❌ Wrong Principle. -1 HP")
                st.session_state.hp -= 1
                st.rerun()

    # --- MISSION 3: TRACEABILITY ---
    elif st.session_state.level == 3:
        st.header("Mission 3: Traceability Documents")
        item = st.session_state.t_data[st.session_state.idx]
        
        st.write(f"### Document: `{item['item']}`")
        col1, col2, col3 = st.columns(3)
        
        if col1.button("⬅️ INPUTS"):
            move = "INPUTS"
        elif col2.button("🔄 PROCESS"):
            move = "PROCESS"
        elif col3.button("➡️ OUTPUTS"):
            move = "OUTPUTS"
        else: move = None

        if move:
            if move == item['a']:
                st.success("✅ Correct!")
                st.session_state.score += 10
                st.session_state.idx += 1
                if st.session_state.idx >= len(st.session_state.t_data):
                    st.session_state.level = 4
                st.rerun()
            else:
                st.error(f"❌ Incorrect. This belongs in {item['a']}")
                st.session_state.hp -= 1
                st.rerun()

    # --- VICTORY ---
    else:
        st.balloons()
        st.header("🏆 YOU PASSED THE EXAM!")
        st.write(f"Final Score: {st.session_state.score}")
        if st.button("Play Again"):
            for key in list(st.session_state.keys()): del st.session_state[key]
            st.rerun()
