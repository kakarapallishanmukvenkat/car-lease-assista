from groq import Groq
import os

client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                       "url": "https://www.mattmahoney.net/ocr/stock_gs200.jpg"
                    }
                }
            ]
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)
