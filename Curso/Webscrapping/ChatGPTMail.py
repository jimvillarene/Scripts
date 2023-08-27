#! /usr/bin/env python3
import webbrowser, sys, pyperclip, openai

openai.api_key = "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"

sys.argv #Here it receives arguments from the command line
if len(sys.argv)>1: #Check if the script receives arguments
    petition=' '.join(sys.argv[1:])
else:
    petition=pyperclip.paste()    
#check if we're receiving

#Funtion to chat with ChatGPT, here it will receive the prompt and return a message
def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message


chatbot_response = chat_with_chatgpt(petition)
print(chatbot_response)


#webbrowser.open('https://www.google.com/search?q=' + petition)