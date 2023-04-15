from chatterbot import ChatBot

bot = ChatBot( "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
    "chatterbot.logic.MathematicalEvaluation",
    "chatterbot.logic.TimeLogicAdapter",
    "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="database.db"
   )

print("Type something to begin...")

while True:
    try:
        bot_input = bot.get_response(None)


    except (KeyboardInterrupt, EOFError, SystemExit):
        break