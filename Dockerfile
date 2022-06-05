FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PIP_TIMEOUT 60
ENV PYTHONPATH $PYTHONPATH:/usr/src/app
ENV POETRYPATH /root/.local/bin
ENV PATH $POETRYPATH:$PATH

WORKDIR /code

RUN curl -sSL https://install.python-poetry.org | python -

COPY pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . /code/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
