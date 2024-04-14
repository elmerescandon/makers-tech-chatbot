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


def createResponseMessage(prevMessage, action, data):
    return "System: Consider yourself a customer service agent called Haikyu for a technology e-commerce," + \
            "\nBased on the previous message: %s" % prevMessage + \
            "where the customer asked for the following action: %s" % action + \
            "\nNow, generate a response for the customer based on the following data: %s" % data + \
            "\nThe following rules apply:\n" + \
            "\n- The response must be a string that could be sent directly to the costumer" + \
            "\n- The response must be short and maintain a neutral message" + \
            "\n- If no action is required respond with information about our five categories: 'laptop, tablet, speaker, keyboard and mouse'"