
import json
from colorama import Fore, Back, Style
from colorama import init
from openai import OpenAI
import time
import os
chathistory = []


def prasci():
    print(Fore.GREEN + """



      ███        ▄████████ ████████▄   ▄█   ▄██████▄  ███    █▄     ▄████████ 
   ▀█████████▄  ███    ███ ███   ▀███ ███  ███    ███ ███    ███   ███    ███ 
     ▀███▀▀██   ███    █▀  ███    ███ ███▌ ███    ███ ███    ███   ███    █▀  
      ███   ▀  ▄███▄▄▄     ███    ███ ███▌ ███    ███ ███    ███   ███        
      ███     ▀▀███▀▀▀     ███    ███ ███▌ ███    ███ ███    ███ ▀███████████ 
      ███       ███    █▄  ███    ███ ███  ███    ███ ███    ███          ███ 
      ███       ███    ███ ███   ▄███ ███  ███    ███ ███    ███    ▄█    ███ 
     ▄████▀     ██████████ ████████▀  █▀    ▀██████▀  ████████▀   ▄████████▀                                                                                                     
    """)
    print(Fore.BLUE + "\t " +"4TD, Ethically used artficial intellegence, model: 1e")

prasci()




nm = input(Fore.WHITE + "Enter your name >> ")
user_profile = {f"name": "{nm}", "prefrences": {"theme": "funny"}}


client = OpenAI(
  api_key="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"
)

def printdy(text, colorama1=Fore.WHITE):
  for i in text:
    if i.isdigit():
      print(colorama1 + Style.BRIGHT + i + Style.RESET_ALL, end='', flush=True)
    else:
      print(colorama1 + i + Style.RESET_ALL, end='', flush=True)
    time.sleep(0.034)
  time.sleep(2)
  print("")
  return None

def add_to_history(role, content):
  chathistory.append({"role": role, "content": content})


def get_context():
  context_messages = [
    {"role": "system", "content": f"User profile: {json.dumps(user_profile)}", "model": "you are a custom ai client named 4TD and your model name is 1e (first public release of 4TD), you are designed to be used properly and avoid procrastination or questions which are easily researchable without ai, to prevent ai slop and loosing cognative functions by overusing ai for everything, made by Mohammed Moustafa Abdelaal a 14 year old Egyptian self learnt programmer in Python after realising his dream job of software engineering is slowly being taken over by unbounded modern ai like GPT-5 and decided to make 4Tedious or 4TD to sympathise with people like him but having ai like it was ment to be used."},
    *chathistory[-len(chathistory):]
  ]
  return context_messages

def check_question(question):
  rp = client.responses.create(
    model="gpt-4o-mini",
    input=question + str(get_context()) + "does this question need the use of ai? be strict and only allow smart or niche questions, prevent questions that are easibly researchable or end up with a conversation with the ai, allow questions related to 4TD/4Tedious and allow questions asking for reviews or crtitasism also allow ANY questions about the 4TD/4Tedious or the founder of it, still dont be overly strict and dont be opinionated and allow questions or statements that regard mental health or are potentoinally dangerous to something or themselves. explicitly in one word yes or no.",
    store=False
    )

  if "yes" in rp.output_text.lower():
    return True
  else:
    return False



while True:
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
  prasci()
  print(Fore.BLUE + """
Options:
.  Show chat history [1]
.  More information on the 4TD project [2]
.  Ask question [no number just write it.]
.  Quit [write quit]
.  Restart Chat [write Restart]


    """)
  question = input(Fore.WHITE + "\n" + ">> ")
  if question == "quit" or question == "Quit":
    quit(Style.RESET_ALL + "")
  if question == "1":
    printdy(str(chathistory), Fore.GREEN)
    continue
  if question == "2":
    response2 = client.responses.create(
    model="gpt-4o-mini",
    input="Explain what is the 4TD ai client in its fullest" + str(get_context()),
    store=False,
  )
    printdy("\n" + response2.output_text, Fore.GREEN)
    continue

  if question == "Restart" or question == "restart" or question == "restart chat" or question == "Restart Chat" or question == "Restart chat":
      chathistory = []
      question = ""
      continue

  if check_question(question) != True:
    printdy("This question does not require or benefit with the usage of AI, instead you can search this question up on the internet or study it to prevent overeliance on AI and to prevent the loss of cognative abilities, you can ask more questions but keep them smart and good for the use of AI! :(", Fore.RED)
    continue
  
  add_to_history("user", question)


  response = client.responses.create(
    model="gpt-4o-mini",
    input=question + str(get_context()),
    store=True,
  )
  add_to_history("ai", response.output_text)
  printdy("\n" + response.output_text, Fore.GREEN)

