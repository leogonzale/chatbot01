from openai import OpenAI

client = OpenAI()


user_input = input("\nAsk anything you want...\n\n")

model = "gpt-3.5-turbo"

def set_user_input_category(user_input):
     question_keywords = ["who", "what", "when", "where", "why", "how", "?"]
     for keyword in question_keywords:
        if keyword in user_input.lower():
            return "question"
     return "statement"
         
def myquestions(usrquestion):

    messages = [
    {"role": "system", "content": "You are an assistant that talks like a michelin star chef."},
    {"role": "user", "content": user_input}
    ]

     
    response = client.chat.completions.create(
    model = model,
    messages = messages
    )

    response_for_user = response.choices[0].message.content
    if set_user_input_category(user_input) == "question":
       response_for_user = "Good question! " + response_for_user
         
    return response_for_user


print("\n" + myquestions(user_input) + "\n" )