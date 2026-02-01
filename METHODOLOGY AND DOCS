import streamlit as st
import random

# --- PAGE SETUP ---
st.set_page_config(page_title="HACCP Exam Trainer", page_icon="🛡️")

# --- DATA EXTRACTION FROM TABLES ---

# Table 1: Methodology (Page 3) - Full Content Included
methodology_data = [
    {"q": "Operation or process", "detail": "What is the test object? / Part of the process or operation to be checked", "a": "Operation or process"},
    {"q": "Verification activity", "detail": "What to check? / Planned actions to verify if practices follow correct hygiene", "a": "Verification activity"},
    {"q": "Check procedure", "detail": "How should the verification be done? / Time, conditions, place and procedure for checks", "a": "Check procedure"},
    {"q": "Frequency", "detail": "How often do you have to do it? / Planned periodicity of the checks", "a": "Frequency"},
    {"q": "Person in charge", "detail": "Who should do it? / Person responsible for carrying out verification activities", "a": "Person in charge"},
    {"q": "Record", "detail": "How are the results recorded? / Design of registration models to record results and incidents", "a": "Record"}
]

# Table 2: The 7 Principles (Pages 3-4) - Full Content Included
principles_data = [
    {"p": "Principle 1", "desc": "Analyze possible physical, chemical and microbiological hazards", "ex": "Growth of microorganisms"},
    {"p": "Principle 2", "desc": "Determination of critical control points (CCP)", "ex": "Identifying the step to prevent/eliminate hazards"},
    {"p": "Principle 3", "desc": "Setting critical limits", "ex": "Adding preservative additive 2-2.5g/Kg"},
    {"p": "Principle 4", "desc": "Establishment of a surveillance system", "ex": "Supervision of the weighing and addition of the additive"},
    {"p": "Principle 5", "desc": "Formulation of corrective measures", "ex": "Determine in advance what to do with food with wrong additive amount"},
    {"p": "Principle 6", "desc": "System verification", "ex": "Samples of finished product, calibrated scales, etc."},
    {"p": "Principle 7", "desc": "Documentation and registration", "ex": "Register of additive weights"}
]

# Table 3: Traceability Documents (Page 5) - Full Content Included
traceability_data = [
    {"item": "Reception control record", "a": "INPUTS"},
    {"item": "Save tags", "a": "INPUTS"},
    {"item": "Updated list of suppliers and raw materials", "a": "INPUTS"},
    {"item": "Daily production list", "a": "PRODUCTION PROCESS"},
    {"item": "Exit sheet of product from the warehouse", "a": "PRODUCTION PROCESS"},
    {"item": "Recipes or formulas", "a": "PRODUCTION PROCESS"},
    {"item": "Production sheets", "a": "PRODUCTION PROCESS"},
    {"item": "Record of warehouse departures", "a": "OUTPUTS"},
    {"item": "Sales record", "a": "OUTPUTS"},
    {"item": "Sales tickets", "a": "OUTPUTS"},
    {"item": "Transportation vouchers", "a": "OUTPUTS"}
]

# --- SESSION STATE ---
if 'init' not in st.session_state:
    st.session_state.hp = 3
    st.session_state.level = 1
    st.session_state.q_idx = 0
    random.shuffle(methodology_data)
    random.shuffle(principles_data)
    random.shuffle(traceability_data)
    st.session_state.m_list = methodology_data
    st.session_state.p_list = principles_data
    st.session_state.t_list = traceability_data
    st.session_state.init = True

def reset():
    for key in list(st.session_state.keys()): del st.session_state[key]
    st.rerun()

st.title("🛡️ HACCP Total Revision")
st.write(f"❤️ HP: {st.session_state.hp} | Activity: {st.session_state.level}/3")

if st.session_state.hp <= 0:
    st.error("💀 GAME OVER! Please review your notes and try again.")
    if st.button("Restart"): reset()

# --- ACTIVITY 1: METHODOLOGY ---
elif st.session_state.level == 1:
    st.subheader("Activity 1: The Methodology Table (Page 3)")
    item = st.session_state.m_list[st.session_state.q_idx]
    st.info(f"DEFINITION: {item['detail']}")
    
    ans = st.radio("Which column does this belong to?", sorted([x['a'] for x in methodology_data]))
    if st.button("Submit"):
        if ans == item['a']:
            st.success("Correct!")
            st.session_state.q_idx += 1
            if st.session_state.q_idx >= len(st.session_state.m_list):
                st.session_state.level = 2
                st.session_state.q_idx = 0
            st.rerun()
        else:
            st.error(f"Wrong. This is part of: {item['a']}")
            st.session_state.hp -= 1
            st.rerun()

# --- ACTIVITY 2: THE 7 PRINCIPLES ---
elif st.session_state.level == 2:
    st.subheader("Activity 2: The 7 Principles (Pages 3-4)")
    item = st.session_state.p_list[st.session_state.q_idx]
    st.info(f"DESCRIPTION: {item['desc']}\n\nEXAMPLE: {item['ex']}")
    
    ans = st.selectbox("Which Principle is this?", [f"Principle {i}" for i in range(1, 8)])
    if st.button("Verify"):
        if ans == item['p']:
            st.success("Correct!")
            st.session_state.q_idx += 1
            if st.session_state.q_idx >= len(st.session_state.p_list):
                st.session_state.level = 3
                st.session_state.q_idx = 0
            st.rerun()
        else:
            st.error(f"Incorrect. This is {item['p']}")
            st.session_state.hp -= 1
            st.rerun()

# --- ACTIVITY 3: TRACEABILITY ---
elif st.session_state.level == 3:
    st.subheader("Activity 3: Traceability Documents (Page 5)")
    item = st.session_state.t_list[st.session_state.q_idx]
    st.warning(f"DOCUMENT: {item['item']}")
    
    ans = st.radio("Select Stage:", ["INPUTS", "PRODUCTION PROCESS", "OUTPUTS"])
    if st.button("Check Stage"):
        if ans == item['a']:
            st.success("Great job!")
            st.session_state.q_idx += 1
            if st.session_state.q_idx >= len(st.session_state.t_list):
                st.session_state.level = 4
            st.rerun()
        else:
            st.error(f"Wrong. This belongs to {item['a']}")
            st.session_state.hp -= 1
            st.rerun()

else:
    st.balloons()
    st.header("🏆 MASTER OF HACCP!")
    st.write("You have completed all tables from the material.")
    if st.button("Play Again"): reset()
