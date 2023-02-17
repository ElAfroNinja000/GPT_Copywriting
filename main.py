import os
import openai


def send_request(request: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=request,
      temperature=0.5,
      max_tokens=500,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


if __name__ == '__main__':
    print()
