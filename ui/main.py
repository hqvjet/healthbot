import chainlit as cl
from app.agents import HealthBotAgents, DiagnosisAgent

bot_agents = HealthBotAgents()
diag_agent = DiagnosisAgent()
diag_prompt = diag_agent.get_prompts()
bot_agents.set_prompt(diag_prompt)
chain = bot_agents.get_chain()

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
            "content": "Bạn là một trợ lý sức khỏe, chuyên cung cấp thông tin và hỗ trợ người dùng về các vấn đề sức khỏe. Hãy trả lời các câu hỏi của người dùng một cách chính xác và thân thiện theo các fewshot learning đã cho, các fewshot learning trên chỉ là ví dụ, không phải của user hiện tại"
        },
        {
            "role": "assistant",
            "content": "Chào bạn, tôi là trợ lý sức khỏe của bạn. Bạn có thể hỏi tôi về các triệu chứng, bệnh lý hoặc bất kỳ câu hỏi nào liên quan đến sức khỏe của bạn. Hãy bắt đầu cuộc trò chuyện nào!"
        }
    ])

@cl.on_message
async def handle_message(message: cl.Message):
    message_history = cl.user_session.get("HealthBot")
    message_history.append({
        "role": "user",
        "content": message.content
    })

    print(message_history)
    print("Message content:", message.content)

    msg = cl.Message(content="")
    resp = chain.stream(message_history)

    for chunk in resp:
        await msg.stream_token(chunk)

    message_history.append({
        "role": "assistant",
        "content": msg.content
    })
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
