from chatterbot import ChatBot  
from chatterbot.trainers import ListTrainer  
from chatterbot.languages import SPA  

  
class Spanish(SPA):  
    language_shortname = 'es_core_news_sm'  



# Crea un nuevo chatbot llamado 'Bot'  
chatbot = ChatBot('Bot',  
    language=Spanish,  
    storage_adapter='chatterbot.storage.SQLStorageAdapter',  
    logic_adapters=[  
        {  
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': 'chatterbot.comparisons.SpaCySimilarity',
            'default_response': 'Lo siento, no entiendo. Por favor, reformula tu pregunta.',  
            'maximum_similarity_threshold': 0.90  
        }  
    ],  
    database_uri='sqlite:///database.sqlite3'  
)  


  
# Vacía la base de datos  
chatbot.storage.drop()  


  
# Entrenar al bot  
trainer = ListTrainer(chatbot)  
trainer.train([  
    'Hola',  
    '¡Hola, cómo puedo ayudarte hoy?',  
    "¿Qué es Python?",  
    "Python es un lenguaje de programación interpretado de alto nivel, creado por Guido van Rossum en 1991. Se caracteriza por su sintaxis clara y legible.",  
    "¿Cómo se escribe un comentario en Python?",  
    "Los comentarios en Python se escriben comenzando la línea con un símbolo de almohadilla (#). Por ejemplo: # Este es un comentario.",  
    "¿Cómo se declara una variable en Python?",  
    "En Python, se declara una variable asignándole un valor. Por ejemplo: mi_variable = 5.",  
    "¿Cómo se define una función en Python?",  
    "En Python, una función se define con la palabra clave 'def', seguida del nombre de la función y paréntesis. Por ejemplo: def mi_funcion():",  
    "¿Cómo se crea una lista en Python?",  
    "Las listas en Python se crean encerrando una secuencia de valores entre corchetes y separándolos con comas. Por ejemplo: mi_lista = [1, 2, 3, 4, 5].",  
    "¿Cómo se realiza un bucle for en Python?",  
    "En Python, un bucle for se realiza con la palabra clave 'for' seguida de una variable, la palabra 'in' y una secuencia. Por ejemplo: for i in range(5):",  
    "¿Cómo se realiza un bucle while en Python?",  
    "Un bucle while se realiza con la palabra clave 'while' seguida de una condición. Por ejemplo: while i < 5:",  
    "¿Cómo se manejan las excepciones en Python?",  
    "En Python, las excepciones se manejan con los bloques 'try' y 'except'. El código que puede lanzar una excepción se coloca dentro del bloque 'try', y el código que se ejecutará si ocurre una excepción se coloca dentro del bloque 'except'.",  
    "¿Qué hace la función 'print' en Python?",  
    "La función 'print' en Python imprime el argumento que se le pasa a la consola. Por ejemplo: print('Hola, mundo!') imprimirá 'Hola, mundo!' en la consola.",  
    "¿Cómo se importa un módulo en Python?",  
    "En Python, se importa un módulo usando la palabra clave 'import' seguida del nombre del módulo. Por ejemplo: import math.",  
    'Gracias',
    '!De nada! No dudes en preguntar si tienes más preguntas.'  
])  

  
# Crea un nuevo chatbot para las sesiones de chat  
chatbot = ChatBot('Bot',  
    language=Spanish,  
    storage_adapter='chatterbot.storage.SQLStorageAdapter',  
    logic_adapters=[  
        {  
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': 'chatterbot.comparisons.SpaCySimilarity',
            'default_response': 'Lo siento, no entiendo. Por favor, reformula tu pregunta.',  
            'maximum_similarity_threshold': 0.90  
        }  
    ],  
    database_uri='sqlite:///database.sqlite3',  
    read_only=True  
)  
  
print('ChatBot está listo para chatear!')  


  
while True:  
    try:  
        user_input = input()  
        bot_response = chatbot.get_response(user_input)  
        print(bot_response)  
    except(KeyboardInterrupt, EOFError, SystemExit):  
        break  
