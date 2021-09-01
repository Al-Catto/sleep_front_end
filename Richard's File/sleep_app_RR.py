import streamlit as st
from streamlit.hashing import _CodeHasher
import datetime
import requests

'''
# Koala - The Sleep Prediciton App
# '''
st.image('koala.jpg')

try:
    # Before Streamlit 0.65
    from streamlit.ReportThread import get_report_ctx
    from streamlit.server.Server import Server
except ModuleNotFoundError:
    #After Streamlit 0.65
    from streamlit.report_thread import get_report_ctx
    from streamlit.server.server import Server

######################## MAIN ########################  
def main():
    state = _get_state()
    pages = {
        "1. Method": page_method,
        "2. Inputs - User": page_userinputs,
        "3. Inputs - Medical Professional": page_medinputs,
        "4. Predictions": page_predictions,
    }

    st.sidebar.title("Sleep Prediction Steps")
    page = st.sidebar.radio("Select your page", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page](state)

    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()

######################## METHOD PAGE ######################## 

# 1. Create and curate the method page
def page_method(state):
  
    st.title(":smiley: Getting Started")
    st.header('Why is sleep so important?')
    st.header('How can Koala help you?')
    st.header('How to use Koala')

######################## INPUT-USER PAGE ######################## 

# 2. Create and curate the user inputs page
def page_userinputs(state):
    st.title("Inputs - User")
    st.write("---")
    display_state_values(state)

    st.write("---")
    #Q1: Gender (select)
    options = ['-', 'Male', 'Female']
    state.sex = st.selectbox('What is your gender?', options, options.index(state.sex) if state.sex else 0)
    st.write(state.sex)

    #Q2: Age (int input)
    state.age = st.text_input("what is your age?", state.age or "")
    st.write(state.age)

    #Q3: Ethnicity (select)
    options = ['-', '0: Asian', '1: Black', '2: Hispanic', '3: Native American', '5: White']
    state.ethnicity = st.selectbox('What is your ethnicity?', options, options.index(state.ethnicity) if state.ethnicity else 0)
    st.write(state.ethnicity)
    
    #Q4: Education
    options = ['-', '1: 8th grade or less', '2: 9-11 grade', '3: 12th/high school graduate', '4: Some college', '5: College bachelors degree', '6: Post graduate college work']
    state.education = st.selectbox('What is your highest level of education?', options, options.index(state.education) if state.education else 0)
    st.write(state.education)

    #Q5: Height
    state.height = st.text_input("what is your height in cm?", state.height or "")
    st.write(state.height)
    
    #Q6: Weight
    state.weight = st.text_input("what is your weight in kg?", state.weight or "")
    st.write(state.weight)
    #Q7: Coffee Intake
    state.coffee = st.slider("How many cups of coffee do you drink each day?.", 1, 15, state.coffee)
    st.write(state.coffee)
    #Q8: Other caffeinated drinks

    #Q9: Alchol Consumption

    #Q10: Smoking 
    
    #Q11: Life assessment

    #Q12: Number of naps per day
    
    
    
    
    
    
    
    options = ["Hello", "World", "Goodbye"]
    state.input = st.text_input("Set input value.", state.input or "")
    state.slider = st.slider("Set slider value.", 1, 10, state.slider)
    state.radio = st.radio("Set radio value.", options, options.index(state.radio) if state.radio else 0)
    state.checkbox = st.checkbox("Set checkbox value.", state.checkbox)
    state.selectbox = st.selectbox("Select value.", options, options.index(state.selectbox) if state.selectbox else 0)
    state.multiselect = st.multiselect("Select value(s).", options, state.multiselect)

    # Dynamic state assignments
    for i in range(3):
        key = f"State value {i}"
        state[key] = st.slider(f"Set value {i}", 1, 10, state[key])

######################## INPUT - MEDICAL PROFESSIONAL ######################## 

# 3. Create and curate the medical professional inputs page
def page_medinputs(state):
    st.title("Inputs - Medical Professional")
    st.write("---")
    display_state_values(state)
    
    st.write("---")
    
    # Q1 HDL Levels
    state.hdl = st.text_input("What is the patient's HDL level?", state.hdl or "")
    st.write(state.hdl)
    
    # Q2 LDL Levels
    state.ldl = st.text_input("What is the patient's LDL level?", state.ldl or "")
    st.write(state.ldl)
    
    # Q3 Total Cholestorol
    state.total_cholesterol = st.text_input("What is the patient's total cholesterol level?", state.total_cholesterol or "")
    st.write(state.total_cholesterol)
    
    # Q4 Triglycerides
    state.triglycerides = st.text_input("What is the patient's triglyceride level?", state.triglycerides or "")
    st.write(state.triglycerides)
    
    # Q5 Hip Girth (metres)
    state.hipgirthm = st.text_input("What is the patients hip girth (in metres)?", state.hipgirthm or "")
    
    # Q6 Neck Girth (metres)
    state.neckgrithm = st.text_input("What is the patient's neck girth (in metres)?", state.neckgrithm or "")
    
    # Q7 Waist Girth (metres)
    state.waistgirthm = st.text_input("What is the patient's waist girth (in metres)?", state.waistgirthm or "")
    
    # Q8 Waist Hip Ratio
    state.waisthip = st.text_input("What is the patient's waist to hip ratio?", state.waisthip or "")
    
    # Q9 Sit Sysm
    state.sitsysm = st.text_input("What is the mean of the patient's seated systolic measures?", state.sitsysm or "")
    
    # Q10 Sit Diam
    state.sitdiam = st.text_input("What is the mean of the patient's seated diastolic pressures?", state.sitdiam or "")
    
    # Q11 General Evaluation of the patient's sleep satisfaction
    options = ['-', '1: Most of the time', '2: Some of the time', '3: Not usually', '4: Never']
    state.eval_general = st.selectbox('How often is the patient satisfied with their sleep?',options, options.index(state.eval_general) if state.eval_general else 0)
    
    # Q12 General Evaluation of the patient's health
    options = ['-', '1: Excellent', '2: Very Good', '3: Good', '4: Fair', '5: Poor']
    state.eval_health = st.selectbox("What is your general evaluation of the patient's health?", options, options.index(state.eval_health) if state.eval_health else 0)
    
    # Q13 Snoring Frequency
    options = ['_', '1: Never or rarely', '2: Sometimes', '3: At least once a week', '4: Several (3 to 5) nights per week', '5: Every, or almost every, night', "9: Don't know"]
    state.snore_freq = st.selectbox('How often does the patient snore?', options, options.index(state.snore_freq) if state.snore_freq else 0)
    
    # Q14 Snoring Volume
    options = ['-', '1: Slightly louder than heavy breathing', '2: As loud as mumbling or talking', '3: Louder than talking', '4: Very loud, can be heard through a closed door',
               '9: Do not know', '8: Does not apply']
    state.snore_vol = st.selectbox("How loud is the patient's snoring?", options, options.index(state.snore_vol) if state.snore_vol else 0)
    
    # Q15 Frequency of choking during sleep
    options = ['-', "1: Never or rarely", '2: Sometimes', '3: At least once a week', '4: Several nights per week', "9: Don't know"]
    state.choke_freq = st.selectbox("How often does the patient gasp, choke, or make snorting sounds during sleep?", options, 
                                    options.index(state.choke_freq) if state.choke_freq else 0)
    
    # Q16 Sleep apnea
    options = ['-', "1: Never or rarely", '2: Sometimes', '3: At least once a week', '4: Several nights per week', "9: Don't know"]
    state.apnea_freq = st.selectbox("How often does the patience experience moments during sleep where they stop breathing, or breathe abnormally?", options,
                                    options.index(state.apnea_freq) if state.apnea_freq else 0)
    
    # Q17 Frequency of awakening with gasping or choking
    options = ['-', "1: Never or rarely", "2: Sometimes", "3: At least once a week", "4: Several nights a week", "5: Every, or almost every, night", "9: Don't know"]
    state.awake_freq = st.selectbox("How often does the patient wake suddenly with the feeling of gasping or choking?", options,
                                    options.index(state.awake_freq) if state.awake_freq else 0)
    
    # Q18 No Nasal Congestion
    options = ['-', 'N: No', 'Y: Yes']
    state.nasal_cong_none = st.selectbox("Does the patient have no nasal congestion today or tonight?", options, 
                                         options.index(state.nasal_cong_none) if state.nasal_cong_none else 0)
    
    # Q19 Any Cardiovascular Disease Since Baseline
    options = ['-', '0: No', '1: Yes']
    state.any_cvd = st.selectbox("Has the patient experienced any Cardiovascular Disease since their baseline Polysomnogram?",
                                 options, options.index(state.any_cvd) if state.any_cvd else 0)
    
    # Q20 Hypertension: Self-reported diagnosis by a physician
    options = ['-', 'N: No', 'Y: Yes']
    state.hypertension_ynd = st.selectbox("Does the patient have either high blood pressure or hypertension?", options,
                                          options.index(state.hypertension_ynd) if state.hypertension_ynd else 0)
    
    # Q21 Stroke
    options = ['-', 'N: No', 'Y: Yes']
    state.stroke_ynd = st.selectbox("Has the patient ever had a stroke?", options, options.index(state.stroke_ynd) if state.stroke_ynd else 0)
    
    # Q22 Asthma
    options = ['-', 'N: No', 'Y: Yes']
    state.asthma_ynd = st.selectbox("Has the patient ever had asthma?", options, options.index(state.asthma_ynd) if state.asthma_ynd else 0)
    
    # Q23 Thyroid
    options = ['-', 'N: No', 'Y: Yes']
    state.thyroid_ynd = st.selectbox("Does the patient have a thyroid problem?", options, options.index(state.thyroid_ynd) if state.thyroid_ynd else 0)
    
    # Q24 Arthritis
    options = ['-', 'N: No', 'Y: Yes']
    state.arthritis_ynd = st.selectbox("Does the patient have arthritis?", options, options.index(state.arthritis_ynd) if state.arthritis_ynd else 0)
    
    # Q25 Emphysema
    options = ['-', 'N: No', 'Y: Yes']
    state.emphysema_ynd = st.selectbox("Does the patient have emphysema?", options, options.index(state.emphysema_ynd) if state.emphysema_ynd else 0)
    
    # Q26 Menopausal Status
    options = ['-', '0: Regular Periods', '1: Irregular Periods', '2: Periods stopped due to menopause', '4: Periods stopped due to Surgery']
    state.menopausal_status = st.selectbox("Does the patient still have regular periods?", options, 
                                           options.index(state.menopausal_status) if state.menopausal_status else 0)
    
    # Q27 Number of Pregnancies
    state.num_pregnancies = st.slider('How many times has the patient been pregnant?', 0, 10, state.num_pregnancies)
    st.write(state.num_pregnancies)
    
    # Q28 Asthma medication
    options = ['-', '0: Not taking', '1: Taking']
    state.asthma_med = st.selectbox("Is the patient currently taking asthma medication?", options, options.index(state.asthma_med) if state.asthma_med else 0)
    
    # Q29 Cholesterol medication
    options = ['-', '0: Not taking', '1: Taking']
    state.cholesterol_med = st.selectbox("Is the patient currently taking cholesterol medication?", options, 
                                         options.index(state.cholesterol_med) if state.cholesterol_med else 0)
    
    # Q30 Depression Medication
    options = ['-', '0: Not taking', '1: Taking']
    state.depression_med = st.selectbox("Is the patient currently taking any depression medication?", options,
                                        options.index(state.depression_med) if state.depression_med else 0)
    
    # Q31 Hypertension Medication
    options = ['-', '0: Not taking', '1: Taking']
    state.htn_med = st.selectbox("Is the patient currently taking any hypertension medication?", options,
                                 options.index(state.htn_med) if state.htn_med else 0)
    
    # Q32 Decongestants Medication
    options = ['-', '0: Not taking', '1: Taking']
    state.decongestants_med = st.selectbox("Is the patient currently taking any decongestant medication?", options,
                                           options.index(state.decongestants_med) if state.decongestants_med else 0)
    
    # Q33 Antihistamine Medication
    options = ['-', '0: Not taking', '1: Taking']
    state.antihistamines_med = st.selectbox("Is the patient currently taking anti-histamine medication?", options,
                                            options.index(state.antihistamines_med) if state.antihistamines_med else 0)
    
    # Q34 Anxiety Medication
    options = ['-', '0: Not taking', '1: Taking']
    state.anxiety_med = st.selectbox("Is the patient currently taking any anxiety medication?", options,
                                     options.index(state.anxiety_med) if state.anxiety_med else 0)
    
    # Q35 Diabetes Medication
    options = ['-', '0: Not taking', '1: Taking']
    state.diabetes_med = st.selectbox("Is the patient currently taking any diabetes medication?", options,
                                      options.index(state.diabetes_med) if state.diabetes_med else 0)
    
    # Q36 Sedative Medication
    options = ['-', '0: Not taking', '1: Taking']
    state.sedative_med = st.selectbox("Is the patient currently taking any sedative medication?", options,
                                     options.index(state.sedative_med) if state.sedative_med else 0)
    
    # Q37 Thyroid Medication
    options = ['-', '0: Not taking', '1: Taking']
    state.thyroid_med = st.selectbox("Is the patient currently taking any thyroid medication?", options,
                                     options.index(state.thyroid_med) if state.thyroid_med else 0)
    
    # Q38 Has the patient ever taken supplemental hormones for Hypothyroid?
    options = ['-', '0: Not taken', '1: Taken']
    state.x0_Hypothyroid = st.selectbox('Has the patient ever taken supplemental hormones for Hypothyroid?', options,
                                        options.index(state.x0_Hypothyroid) if state.x0_Hypothyroid else 0)
    
    # Q39 Is the patient currently using supplemental hormones for menopause?
    options = ['-', '0: Not taking', '1: Currently taking']
    state.x0_C = st.selectbox('Is the patient currently taking supplemental hormones for monpause?', options,
                              options.index(state.x0_C) if state.x0_C else 0)
    
    # Q40 Has the patient never used supplemental hormones for menopause
    options = ['-', '0: Has taken', '1: Has never taken']
    state.x0_N = st.selectbox('Has the patient never taken supplemental hormones for menopause?', options,
                              options.index(state.x0_N) if state.x0_N else 0)
    
    # Q41 Has the patient previously used supplemental hormones for menopause
    options = ['-', '0: Has never taken', '1: Has previously taken']
    state.x0_P = st.selectbox('Has the patient previously taken supplemental hormonse for menopause?', options,
                              options.index(state.x0_P) if state.x0_P else 0)

    for i in range(3):
        key = f"State value {i}"
        state[key] = st.slider(f"Set value {i}", 1, 10, state[key])

######################## PREDICTIONS PAGE ######################## 

# 4. Create and curate the predictions page
def page_predictions(state):
    st.title("Predictions")
    st.write("---")
    display_state_values(state)

    st.write("---")
    
    
    
    # Dynamic state assignments
    for i in range(3):
        key = f"State value {i}"
        state[key] = st.slider(f"Set value {i}", 1, 10, state[key])


######################## STATE VALUES ######################## 

def display_state_values(state):
    
    #Input - user state
    st.write("Gender_state", state.sex)
    st.write("age_state",state.age)
    st.write("Ethnicity_state", state.ethnicity)
    st.write("Education_state", state.education)
    st.write("Height_state",state.height)
    st.write("Weight_state", state.weight)
    st.write("Coffee_state", state.coffee)
    
    #Input - medical professional state 
    st.write("HDL", state.hdl)
    st.write("LDL", state.ldl)
    st.write("total_cholestorol", state.total_cholesterol)
    st.write('triglycerides', state.triglycerides)
    st.write("hipgirthm", state.hipgirthm)
    st.write('neckgirthm', state.neckgirthm)
    st.write('waistgirthm', state.waistgirthm)
    st.write('waisthip', state.waisthip)
    st.write('sitsysm', state.sitsysm)
    st.write('sitdiam', state.sitdiam)
    st.write('eval_general', state.eval_general)
    st.write('eval_health', state.eval_health)
    st.write('snore_freq', state.snore_freq)
    st.write('snore_vol', state.snore_vol)
    st.write('choke_freq', state.choke_freq)
    st.write('apnea_freq', state.apnea_freq)
    st.write('awake_freq', state.awake_freq)
    st.write('nasal_cong_none', state.nasal_cong_none)
    st.write('any_cvd', state.any_cvd)
    st.write('hypertension_ynd', state.hypertension_ynd)
    st.write('stroke_ynd', state.stroke_ynd)
    st.write('asthma_ynd', state.asthma_ynd)
    st.write('thyroid_ynd', state.thyroid_ynd)
    st.write('arthritis_ynd', state.arthritis_ynd)
    st.write('emphysema_ynd', state.emphysema_ynd)
    st.write('menopausal_status', state.menopausal_status)
    st.write('num_pregnancies', state.num_pregnancies)
    st.write('asthma_med', state.asthma_med)
    st.write('cholesterol_med', state.cholesterol_med)
    st.write('depression_med', state.depression_med)
    st.write('htn_med', state.htn_med)
    st.write('decongestants_med', state.decongestants_med)
    st.write('antihistamines_med', state.antihistamines_med)
    st.write('anxiety_med', state.anxiety_med)
    st.write('diabetes_med', state.diabetes_med)
    st.write('sedative_med', state.sedative_med)
    st.write('thyroid_med', state.thyroid_med)
    st.write('x0_Hypothyroid', state.x0_Hypothyroid)
    st.write('x0_C', state.x0_C)
    st.write('x0_N', state.x0_N)
    st.write('x0_P', state.x0_P)

    #Example states - to be removed at end
    st.write("Input state:", state.input)
    st.write("Slider state:", state.slider)
    st.write("Radio state:", state.radio)
    st.write("Checkbox state:", state.checkbox)
    st.write("Selectbox state:", state.selectbox)
    st.write("Multiselect state:", state.multiselect)
    
    for i in range(3):
        st.write(f"Value {i}:", state[f"State value {i}"])

    if st.button("Clear state"):
        state.clear()

######################## SESSION STATE CLASS - DO NOT AMEND ######################## 
class _SessionState:

    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "hasher": _CodeHasher(hash_funcs),
            "is_rerun": False,
            "session": session,
        }

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for item, value in kwargs.items():
            if item not in self._state["data"]:
                self._state["data"][item] = value

    def __getitem__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)
        
    def __getattr__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __setitem__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def __setattr__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value
    
    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun()
    
    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False
        
        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun()

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)


def _get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")
    
    return session_info.session


def _get_state(hash_funcs=None):
    session = _get_session()

    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = _SessionState(session, hash_funcs)

    return session._custom_session_state


if __name__ == "__main__":
    main()