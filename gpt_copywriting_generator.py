import os
import openai


class GPTCopywritingGenerator:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def send_request(request: str, word_count: int, options: list):
        available_options = [option for option in options.keys() if options[option]]
        options_prompt = ("with " + ", ".join(available_options)) if available_options else ""

        prompt = f"Write a copywriting article about {request}, {options_prompt} in less than {word_count} words"
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
    opts = {
        "examples": True,
        "bullet points": True,
        "call to action": True
    }
    resp = GPTCopywritingGenerator().send_request("fried chicken", 400, opts)
    print(resp)
