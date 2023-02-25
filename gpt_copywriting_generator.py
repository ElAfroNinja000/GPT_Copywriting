import os
import openai
import numpy


class GPTCopywritingGenerator:
    def __init__(self, responses_count):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.responses_count = responses_count

    def send_request(self, request: str, word_count: int, options: list):
        available_options = [option for option in options.keys() if options[option]]
        options_prompt = ("with " + ", ".join(available_options)) if available_options else ""
        prompt = f"Write a copywriting article about {request}, {options_prompt} in less than {word_count} words"

        responses = []
        temperatures        = numpy.random.uniform(0.5, 1,   size=self.responses_count).tolist()
        frequency_penalties = numpy.random.uniform(0.2, 0.8, size=self.responses_count).tolist()
        presence_penalties  = numpy.random.uniform(0.5, 1,   size=self.responses_count).tolist()
        for i in range(self.responses_count):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=temperatures[i],
                max_tokens=1500,
                top_p=1,
                frequency_penalty=frequency_penalties[i],
                presence_penalty=presence_penalties[i])
            responses.append(response["choices"][0]["text"].replace("\n\n", ""))
        return responses


if __name__ == '__main__':
    opts = {
        "examples": True,
        "bullet points": True,
        "call to action": True
    }
    resp = GPTCopywritingGenerator(3).send_request("white chocolate", 400, opts)
    print(resp)
