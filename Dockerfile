FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/tictactoe

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "./tic_tac_toe.py"]
