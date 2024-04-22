import ollama

# def chat_with_ollama():
#     response = ollama.chat(model='llama3', messages=[
#         {
#             'role': 'user',
#             'content': 'Ans shoudl be in 5 words Please: Why is the sky blue?',
#         },
#     ])
#     print(response['message']['content'])

#     #List print response 
#     print(ollama.list())

    # #Show print response
    # print(ollama.show('llama3'))

# def main():
#     chat_with_ollama()

# if __name__ == "__main__":
#     main()


# Directly from api of ollama
from ollama import Client
client = Client(host='http://127.0.0.1:11434')
response = client.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Ans should be in 5 words Please: Why is the sky blue?',
  },
])
print(response['message']['content'])


# import asyncio
# from ollama import AsyncClient

# async def chat():
#   message = {'role': 'user', 'content': 'Ans should be in 5 words Please: what is h2o?'}
#   async for part in await AsyncClient().chat(model='llama3', messages=[message], stream=True):
#     print(part['message']['content'], end='', flush=True)

# asyncio.run(chat())
