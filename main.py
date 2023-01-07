import discord
from pychatgpt import Chat, Options
import openai
openai.organization = "org-NvHSOMKOEO7S2KSKlOPtUW60"
openai.api_key = "sk-y3H630JzJDUT3BlbkFJ5OkSKwTZsisS3cjBIaP9"
openai.Model.list()
options = Options()

# [New] Enable, Disable logs
options.logs = True

# Track conversation
options.track = False

# Optionally, you can pass a file path to save the conversation
# They're created if they don't exist

# options.chat_log = "chat_log.txt"
# options.id_log = "id_log.txt"

# Create a Chat object
#chat = Chat(email="5@lasallehs.org", password="", options=options)

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    if message.channel.id == 943252467217465386 or message.channel.id == 1050536381182656592 or message.channel.id ==1047565374645870743:
      if "/gptunofficial" in message.content:
        chat = Chat(email="jjin25@lasallehs.org", password="", options=options)
        msg = message.content.replace("/gptunofficial ","")
        answer = chat.ask(msg)
        answer=answer[0]
        print(answer)
        n = 2000
        answer_chunks = [answer[i:i+n] for i in range(0, len(answer), n)]
        print(answer_chunks)
        for i in answer_chunks:
          await message.channel.send(i)
      elif "/gpt" in message.content:
        msg = message.content.replace("/gpt ","")
        print("/gpt command used")
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=msg,
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        n = 2000
        answer = response['choices'][0]['text']
        answer_chunks = [answer[i:i+n] for i in range(0, len(answer), n)]
        for i in answer_chunks:
          await message.channel.send(i)

client = MyClient()
client.run("")
