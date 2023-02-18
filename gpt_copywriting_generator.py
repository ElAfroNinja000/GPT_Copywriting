import os
import openai


class GPTCopywritingGenerator:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def send_request(request: str, word_count: int = 400, with_bullet_points: bool = False):
        bullet_points = "bullet points," if with_bullet_points else ""
        prompt = f"Write a copywriting article about {request}, with examples, {bullet_points} and a call to action in less than {word_count} words"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=1,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1)
        return response["choices"][0]["text"].replace("\n\n", "\n")


if __name__ == '__main__':
    resp = GPTCopywritingGenerator().send_request("fried chicken")
    print(resp)
