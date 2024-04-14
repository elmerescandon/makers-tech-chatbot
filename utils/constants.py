

initialInstruction = """System: You are an AI chatbot for a technology e-commerce who is an expert in natural language processing and especially name entity recognition. """

instructions = {
    'actions': 'The actions that the user wants to perform',
    'category': 'The category of the product, such as "laptops, tablet, speakers, keyboards and mouses"',
    'brand': 'The brand of the product, such as "Dell", "Apple", "HP", etc. in case of laptops',
    'model': 'The specific model of the laptop like "MacBook Pro", "XPS 15", "Spectre x360", etc. in case of laptops',
    'specifications': 'Specific technical details about the product ("true" if asked, empty if not asked)',
    'condition': 'The condition of the laptop, like "new", "used" or "refurbished"',
    'price-range': 'The price range of the product with increments of 100 (0-100,100-200, and so on until it reaches higher than a 1000, in that case show 1000+)',
    'availability': 'Whether the laptop is "in stock" or "out of stock"',
    'rating': 'The rating or reviews of the laptop from 1 to 5'
}
actions = {
    'count brands': 'Count the number of brands available in the database',
    'count models': 'Count the number of categories available in the database',
    'count stock': 'Count the number of products that are in stock',
    'recommend': 'Recommend a product based on the user\'s preferences',
    'price': 'Show the price range of the product',
    'specifications': 'Show the specifications of the product',
    'condition': 'Show the condition of the product',
    'rating': 'Show the rating of the product',
    'availability': 'Show the availability of the product'
}

rules = [
    'If an entity is not present in the message, return an empty string for that identity.',
    'If an entity is present in the message, return the entity value as a string.',
    'Only one action is available at a time.'
]