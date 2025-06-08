import chainlit as cl

from app.agents import HealthBotAgents
from data.vector import load_retriever


retriever = load_retriever()
agent = HealthBotAgents(retriever=retriever)

@cl.on_chat_start
async def start():
    """
    This function is called when the chat starts.
    It initializes the chat with a welcome message.
    """
    await cl.Message(
        author="HealthBot",
        content="Chào bạn, tôi là bác sĩ sức khỏe của bạn. Bạn có thể hỏi tôi về các triệu chứng, bệnh lý hoặc bất kỳ câu hỏi nào liên quan đến sức khỏe của bạn. Hãy bắt đầu cuộc trò chuyện nào!"
    ).send()

    cl.user_session.set("HealthBot", [
        {
            "role": "assistant",
            "content": "Chào bạn, tôi là bác sĩ tư vấn sức khỏe của bạn. Bạn có thể hỏi tôi về các triệu chứng, bệnh lý hoặc bất kỳ câu hỏi nào liên quan đến sức khỏe của bạn. Hãy bắt đầu cuộc trò chuyện nào!"
        }
    ])

@cl.on_message
async def handle_message(message: cl.Message):
    message_history = cl.user_session.get("HealthBot")

    print(message_history)
    print("Message content:", message.content)

    msg = cl.Message(content="")
    resp = agent.execute(message.content, message_history)

    for chunk in resp:
        await msg.stream_token(chunk)

    message_history.append({
        "role": "user",
        "content": message.content
    })

    message_history.append({
        "role": "assistant",
        "content": msg.content
    })
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
