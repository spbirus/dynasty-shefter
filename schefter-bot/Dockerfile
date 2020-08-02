FROM python:latest

# Install app
ADD . /usr/src/schefter-bot
WORKDIR /usr/src/schefter-bot
RUN python3 setup.py install

# Launch app
CMD ["python3", "schefter-bot/schefter-bot.py"]