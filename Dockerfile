FROM python:3.8.6-buster
COPY koala.jpg /koala.jpg
COPY requirements.txt /requirements.txt
COPY sleep_models /sleep_models
COPY sleep_app_v2.py /sleep_app_v2.py
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD streamlit run sleep_app_v2.py 
