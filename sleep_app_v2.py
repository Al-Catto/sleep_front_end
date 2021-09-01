import streamlit as st
from streamlit.hashing import _CodeHasher
import datetime
import requests
import pandas as pd
import joblib

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
    #Q1: Gender (select) "sex"
    options = ['-', 'Male', 'Female']
    state.sex = st.selectbox('What is your gender?', options, options.index(state.sex) if state.sex else 0)
    #st.write(state.sex)

    #Q2: Age (int input) "age"
    state.age = st.text_input("what is your age?", state.age or "")
    #st.write(state.age)

    #Q3: Ethnicity (select) "race"
    options = ['-', '0: Asian', '1: Black', '2: Hispanic', '3: Native American', '5: White']
    state.race = st.selectbox('What is your ethnicity?', options, options.index(state.race) if state.race else 0)
    #st.write(state.race)
    
    #Q4: Education "education_survey1"
    options = ['-', '1: 8th grade or less', '2: 9-11 grade', '3: 12th/high school graduate', '4: Some college', '5: College bachelors degree', '6: Post graduate college work']
    state.education_survey1 = st.selectbox('What is your highest level of education?', options, options.index(state.education_survey1) if state.education_survey1 else 0)
    #st.write(state.education_survey1)

    #Q5: Height "heightcm"
    state.heightcm = st.text_input("what is your height in cm?", state.heightcm or "")
    #st.write(state.heightcm)
    
    #Q6: Weight "weightkg"
    state.weightkg = st.text_input("what is your weight in kg?", state.weightkg or "")
    st.write(state.weightkg)
    
    #Q7: Coffee Intake "cups_coffee"
    state.cups_coffee = st.slider("How many cups of coffee do you drink each day?.", 0, 15, state.cups_coffee)
    #st.write(state.cups_coffee)
    
    #Q8: Other caffeinated drinks - NON_FEATURE variable used for calculation
    state.other_caffeine = st.slider("How many other caffeinated drinks do youhave each day in addition to coffee?.", 0, 15, state.other_caffeine)
    #st.write(state.other_caffeine)
    
    ## add together Coffee and Caffeine to get total caffeinated drinks - feature "caffeine" 
    state.caffeine = state.cups_coffee + state.other_caffeine
    #st.write(state.caffeine)
    
    #Q9: Alchol Consumption "alcohol_wk"
    state.alcohol_wk = st.slider("How many alcoholic beverages do you drink each day.", 0, 20, state.alcohol_wk)
    #st.write(state.alcohol_wk)
    
    #Q10: Smoking  - NON_FEATURE variable used for calculation
    options = ['-','Yes', 'No']
    state.smoke = st.radio("Do you smoke?", options, options.index(state.smoke) if state.smoke else 0)
    #st.write(state.smoke)
    
    # "packs_week" 
    state.packs_week = st.slider("If yes how many packs a week do you smoke?", 0, 30, state.packs_week)
    #st.write(state.packs_week)
    
    # NON_FEATURE variable used for calculation
    state.smoke_years = st.slider("How many years have you smoked?", 0, 60, state.smoke_years)
    #st.write(state.smoke_years)

    ## Calculation
    state.pack_years = (((20 * state.packs_week) * 52) * state.smoke_years) / 7280
    #st.write(state.pack_years)

    #st.write(st.session_state.key)

    #Q11: Life assessment "eval_life"
    options = ['-', '1: Completely satisfied', '2: Mostly satisfied', '3: Moderately satisfied', '4: Not very satisfied']
    state.eval_life = st.selectbox("Please select your level of satisfaction with life.", options, options.index(state.eval_life) if state.eval_life else 0)
    #st.write(state.eval_life)

    #Q12: Number of naps per day "naps"
    state.naps = st.slider("How many hours of sleep do you usually get during a typical week from daytime or evening naps?", 0, 20, state.naps)
    #st.write(state.naps)
    
    ##!!!!!!!!!!!!!!!!!! Add button to progress to next page
    
    prediction_df = pd.DataFrame([[state.sex, state.age, state.race, state.education_survey1, state.heightcm, state.weightkg, state.cups_coffee, state.caffeine, state.alcohol_wk, state.packs_week, state.pack_years, state.eval_life, state.naps]],
    columns=['sex', 'age', 'race', 'education_survey1', 'heightcm', 'weightkg', 'cups_coffee', 'caffeine', 'alcohol_wk', 'state.packs_week', 'state.pack_years', 'state.eval_life', 'state.naps'])
    if st.button("make prediction"):
        st.dataframe(prediction_df)
        model = joblib.load('practice_waso.joblib')
        y = model.predict(prediction_df)


    # options = ["Hello", "World", "Goodbye"]
    # state.input = st.text_input("Set input value.", state.input or "")
    # state.slider = st.slider("Set slider value.", 1, 10, state.slider)
    # state.radio = st.radio("Set radio value.", options, options.index(state.radio) if state.radio else 0)
    # state.checkbox = st.checkbox("Set checkbox value.", state.checkbox)
    # state.selectbox = st.selectbox("Select value.", options, options.index(state.selectbox) if state.selectbox else 0)
    # state.multiselect = st.multiselect("Select value(s).", options, state.multiselect)

    # Dynamic state assignments
    # for i in range(3):
    #     key = f"State value {i}"
    #     state[key] = st.slider(f"Set value {i}", 1, 10, state[key])

######################## INPUT - MEDICAL PROFESSIONAL ######################## 

# 3. Create and curate the medical professional inputs page
def page_medinputs(state):
    st.title("Inputs - Medical Professional")
    st.write("---")
    display_state_values(state)
    
    st.write("---")

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
    st.write("Ethnicity_state", state.race)
    st.write("Education_state", state.education_survey1)
    st.write("Height_state",state.heightcm)
    st.write("Weight_state", state.weightkg)
    st.write("Coffee_state", state.cups_coffee)
    st.write("Other_caffeine_state", state.other_caffeine)
    st.write("Caffeine_state",state.caffeine)
    st.write("Alcohol_state", state.alcohol_wk)
    st.write("Packs_wk_state", state.packs_week)
    st.write("Smoke_state", state.smoke)
    st.write("Smoke_years_state", state.smoke_years)
    st.write("pack_years_state", state.pack_years)
    st.write("Life_eval_state", state.eval_life)
    st.write("Naps_state", state.naps)
    #Input - medical professional state 
    #Rich to input 

    #Example states - to be removed at end
    # st.write("Input state:", state.input)
    # st.write("Slider state:", state.slider)
    # st.write("Radio state:", state.radio)
    # st.write("Checkbox state:", state.checkbox)
    # st.write("Selectbox state:", state.selectbox)
    # st.write("Multiselect state:", state.multiselect)
    
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