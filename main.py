import discord
import openai
import json

f = open("config.json","r")

config_f = f.read()

f.close()

config_f = json.loads(config_f)


openai.organization = config_f["openai-org"] # default use "org-NvHSOMKOEO7S2KSKlOPtUW60"
openai.api_key = config_f["openai-apikey"] 
openai.Model.list()

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    if message.channel.id == config_f["discord-channel-id"]:
      if "/gpt" in message.content:
        msg = message.content.replace("/gpt ","")

        # Accessing openai api        
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=msg,
          temperature=0.5,
          max_tokens=2000,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )

        # Dealing with chat-gpt longer msgs by splitting up the message into seperate texts
        DISCORD_MAX_LEN = 2000 

        answer = response['choices'][0]['text']
        answer_chunks = [answer[i:i+DISCORD_MAX_LEN] for i in range(0, len(answer), DISCORD_MAX_LEN)]
        for i in answer_chunks:
          await message.channel.send(i)

client = MyClient()
client.run(config_f["discord-auth-token"])
