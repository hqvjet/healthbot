import chainlit as cl

from app.agents import Orchestrator

orc = Orchestrator()
INTENTS = [
    "advise",  # Ask for health advice
    "image_search",  # Search for disease-related images
    "booking"  # Book an appointment with a doctor
    "unknown"  # Unknown intent
]

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

    msg = cl.Message(content="")

    intents = orc.classify_intent(message.content)

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
                print(resp)
                imgs = []
                for element in resp:
                    imgs.append(
                        cl.Image(
                            name=element['title'],
                            url=element['thumbnail'],
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

    message_history.append({
        "role": "user",
        "content": message.content
    })

    message_history.append({
        "role": "assistant",
        "content": msg.content
    })

    await msg.update()
