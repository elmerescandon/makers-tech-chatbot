# makers-tech-chatbot

Makers Tech Chabot (called Haikyuu!) is an flexible, easy-to-use, and scalable API implementation for e-commerce solutions. We use the Claude 3 Haiku (Opus for testing) AI to generate entity classification and generative language. Also, our AI connects with your non-relational database, ideal
for VTex or Shopify implementations. Try it out locally now!

## Installation

1. Clone the repository.
2. Create a virtual environment: `python -m venv env`.
3. Activate the virtual environment:
    - For Windows: `.\env\Scripts\activate`
    - For macOS/Linux: `source env/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`.

## Usage

1. Run the application: `uvicorn main:app --reload`.
2. Open your browser and go to `http://localhost:8000/docs` to access the API documentation.

## API Endpoints

-   `/message`:
    -   Description: This endpoint is used to send a message object with the input text from the conversation.
    -   Method: POST
    -   Request Body:
        -   `text` (string): The input text from the conversation.
    -   Response:
        -   Success: Returns a response object with the generated message.
        -   Error: Returns an error object if there was an issue processing the request.

## Contribution

This project is part of the technical assesment for the Makers Fellowship. The group was formed by Elmer Escandón and Juan Galdo.
Each contributed to the project as follows:

-   Problem definition-idea: Juan (50%) and Raúl (50%)
-   Technology decision/research: Juan (50%) and Raúl (50%)
-   Prompt Engineering: Juan (70%) and Raúl (30%)
-   API implementation: Raúl (100%)
-   Testing with database: Ráúl (100%)
-   UI Mockups: Juan (100%)
-   Presentation Design and Pitch: Juan (80%) and Raúl(20%)

## Contact

Please do not hesitate to contact us at [elmer.escandontufino@gmail.com](mailto:elmer.escandontufino@gmail.com) or [juan.galdo@ucb.edu.bo](mailto:juan.galdo@ucb.edu.bo)
