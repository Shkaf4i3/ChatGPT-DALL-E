from typing import Text, IO
from os import getenv
from dotenv import load_dotenv

from openai import AsyncOpenAI


load_dotenv()

client_gpt = AsyncOpenAI(api_key=getenv('gpt_key'),
                        base_url="https://api.deepseek.com"
                     )

async def generate_answer(user_message) -> Text:
    chat_completion = await client_gpt.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f'{user_message}',
            }
        ],
        model='deepseek-chat',
        temperature=0.0,
    )
    return chat_completion.choices[0].message.content


client_dalle = AsyncOpenAI(api_key=getenv('dalle_key'))


async def generate_image(user_prompt) -> IO[bytes]:
    chat_completion = await client_dalle.images.generate(
        model='dall-e-3',
        prompt=f'{user_prompt}',
        size='1024x1024',
        quality='standard',
        n=1,
    )

    return chat_completion.data[0].url
