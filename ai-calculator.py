from chatterbot import ChatBot

Bot = ChatBot(name = 'Calculator',
                read_only = True,                  
                logic_adapters = ['chatterbot.logic.MathematicalEvaluation'],                 
                storage_adapter = 'chatterbot.storage.SQLStorageAdapter')
    
print('\033c')
print('Yoo, calculator speaking, What to do?')
while (True):
    user_input = input('me: ')
    
    if user_input.lower() == 'quit':
        print('Bye')
        break
        
    try:
        response = Bot.get_response(user_input)
        print('Calculator: ', response)
    except:
        print('Calculator: Please enter some valid input bro')
