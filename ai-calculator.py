from chatterbot import ChatBot

Bot = ChatBot(name = 'Calculator',  #name
                read_only = True,                  
                logic_adapters = ['chatterbot.logic.MathematicalEvaluation'],  #mathematical function                 
                storage_adapter = 'chatterbot.storage.SQLStorageAdapter')  #SQLDB
    
print('\033c')
print('Yoo, calculator speaking, What to do?')
while (True):
    user_input = input('me: ')  #taking input from the user
    
    if user_input.lower() == 'quit':  #to exit from calculator
        print('Bye')
        break
        
    try:
        response = Bot.get_response(user_input)  #processing the answare
        print('Calculator: ', response)  #get the answare
    except:
        print('Calculator: Please enter some valid input bro')  #wrong, input again
