from utils.constants import instructions, actions, rules

def createEntityMessage(message):
    instructions_string = '\n'.join([f'- {k}: {v}' for k, v in instructions.items()])
    actions_string = '\n'.join([f'- {k}: {v}' for k, v in actions.items()])
    rules_string = '\n'.join([f'- {rule}' for rule in rules])

    return  "System: You are an AI chatbot for a technology e-commerce who is an" + \
            "expert in natural language processing and especially name entity recognition." + \
            "\nConsider the following entities to create the object:\n" + instructions_string + \
            "\nHere are additional rules:\n" + rules_string + \
            "\nThe available actions are:\n" + actions_string + \
            "\nNow return only the entity properties as a JSON object for the following message, avoid additional info: %s" % message
