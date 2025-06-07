import chainlit as cl

@cl.on_chat_start
async def start():
    """
    This function is called when the chat starts.
    It initializes the chat with a welcome message.
    """
    await cl.Message(
        content="Welcome to the Health Diagnosis Chatbot! How can I assist you today?"
    ).send()

@cl.on_message
async def handle_message(message: str):
    """
    This function is called when a message is received.
    It processes the message and returns a response.
    
    :param message: The message received from the user.
    """
    # Here you would typically call your health chain or agents to process the message
    # For demonstration, we will just echo the message back
    response = f"You said: {message}"
    
    await cl.Message(content=response).send()

@cl.on_error
async def handle_error(error: Exception):
    """
    This function is called when an error occurs.
    It sends an error message to the user.
    
    :param error: The exception that occurred.
    """
    await cl.Message(
        content=f"An error occurred: {str(error)}"
    ).send()
    
@cl.on_chat_end
async def end_chat():
    """
    This function is called when the chat ends.
    It sends a goodbye message to the user.
    """
    await cl.Message(
        content="Thank you for using the Health Diagnosis Chatbot! Goodbye!"
    ).send()