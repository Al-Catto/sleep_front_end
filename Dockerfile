FROM python:3.8.6-buster
COPY koala.jpg /koala.jpg
COPY sleepy_koala.jpeg /sleepy_koala.jpeg
COPY awake_koala.jpeg /awake_koala.jpeg
COPY requirements.txt /requirements.txt
COPY sleep_models /sleep_models
COPY sleep_app_v2.py /sleep_app_v2.py
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD streamlit run sleep_app_v2.py --server.port $PORT
