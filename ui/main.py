import chainlit as cl
from typing import Dict, Optional

from app.agents import Orchestrator

orc = Orchestrator()

INTENTS = [
    "advise",  # Ask for health advice
    "image_search",  # Search for disease-related images
    "booking",  # Book an appointment with a doctor
    "unknown"  # Unknown intent
]

@cl.oauth_callback
def oauth_callback(
  provider_id: str,
  token: str,
  raw_user_data: Dict[str, str],
  default_user: cl.User,
) -> Optional[cl.User]:
  return default_user

@cl.on_chat_start
async def start():
    """
    This function is called when the chat starts.
    It initializes the chat with a welcome message.
    """
    pass
    # await cl.Message(
    #     author="HealthBot",
    #     content="Chào bạn, tôi là bác sĩ sức khỏe của bạn. Bạn có thể hỏi tôi về các triệu chứng, bệnh lý hoặc bất kỳ câu hỏi nào liên quan đến sức khỏe của bạn. Hãy bắt đầu cuộc trò chuyện nào!"
    # ).send()

    # cl.user_session.set("HealthBot", [
    #     {
    #         "role": "assistant",
    #         "content": "Chào bạn, tôi là bác sĩ tư vấn sức khỏe của bạn. Bạn có thể hỏi tôi về các triệu chứng, bệnh lý hoặc bất kỳ câu hỏi nào liên quan đến sức khỏe của bạn. Hãy bắt đầu cuộc trò chuyện nào!"
    #     }
    # ])

@cl.step(type="tool")
async def tool():
    # Simulate a running task
    await cl.sleep(2)

    return "Response from the tool!"

@cl.on_chat_resume
async def on_chat_resume(thread):
    pass

from typing import Optional
import chainlit as cl

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch the user matching username from your database
    # and compare the hashed password with the value stored in the database
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None

@cl.on_message
async def handle_message(message: cl.Message):
    message_history = cl.chat_context.to_openai()
    print(f"Message history: {message_history}")
    # await tool()
    msg = cl.Message(content="")
    await msg.send()


    intents = orc.classify_intent(message.content, message_history)
    print(f"Intents: {intents}")

    if intents[0] == INTENTS[-1]:  # If the intent is 'unknown'
        msg.content = "Xin lỗi, tôi chỉ có nhiệm vụ tư vấn và hỗ trợ bạn về vấn đề sức khỏe. Bạn có thể thử hỏi lại hoặc cung cấp thêm thông tin chi tiết hơn."
        await msg.send()
        return 
    else:
        for intent in intents:
            if not intent in INTENTS:
                msg.content = "Xin lỗi, tôi không hiểu ý của bạn. Bạn có thể thử hỏi lại hoặc cung cấp thêm thông tin chi tiết hơn."
                await msg.send()
                return
            
            if intent == INTENTS[1]:
                resp = orc.get_image_search_results(message.content)
                imgs = []
                for element in resp:
                    imgs.append(
                        cl.Image(
                            name=element['title'],
                            url=element['link'],
                            display='inline',

                        )
                    )
                
                msg.elements = imgs
                await msg.send()

            if intent == INTENTS[0]:
                # If the intent is 'advise', get health advice
                resp = orc.get_advice(message.content, message_history)
                for chunk in resp:
                    await msg.stream_token(chunk.content)

    await msg.update()
