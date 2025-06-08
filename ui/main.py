import chainlit as cl
from app.agents.base_agent import client

@cl.on_chat_start
async def start():
    """
    This function is called when the chat starts.
    It initializes the chat with a welcome message.
    """
    await cl.Message(
        author="HealthBot",
        content="Chào bạn, tôi là trợ lý sức khỏe của bạn. Bạn có thể hỏi tôi về các triệu chứng, bệnh lý hoặc bất kỳ câu hỏi nào liên quan đến sức khỏe của bạn. Hãy bắt đầu cuộc trò chuyện nào!"
    ).send()

    cl.user_session.set("HealthBot", [
        {
            "role": "system",
            "content": "You are a helpful health assistant. Provide accurate and concise information about health-related queries."
        }
    ])

@cl.on_message
async def handle_message(message: cl.Message):
    message_history = cl.user_session.get("HealthBot")
    message_history.append({
        "role": "user",
        "content": message.content
    })

    msg = cl.Message(content="")

    stream = await client.chat(
        model="mrjacktung/phogpt-4b-chat-gguf",
        messages=message_history,
        stream=True
    )

    async for chunk in stream:
        if not chunk.get("done") and chunk.get("message"):
            await msg.stream_token(chunk.message.content)

    message_history.append({
        "role": "assistant",
        "content": msg.content
    })
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
