import openai

API_KEY = open("API_KEY","r").read()
openai.api_key = API_KEY

def run(transcript):

    prompt = str(transcript) + "This is a transcript of a YouTube video, Now give me a summary of this video in point format"

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role":"user", "content":prompt}
        ]
    )
    data_in_dict = response['choices'][0]['message']
    print(data_in_dict['content'])