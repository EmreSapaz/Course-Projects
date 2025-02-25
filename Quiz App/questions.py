import requests
import html

parameters = {
    "amount" : 50,
    "type"   : "boolean",
}

url = "https://opentdb.com/api.php?amount=50&type=boolean"
response = requests.get(url,params=parameters)
response.raise_for_status()

data = response.json()

result_data = data.get("results")
questions = []
answers = []
question_answer_pair = []

for i in result_data:
    question = html.unescape(i.get("question"))
    questions.append(question)

for i in result_data:
    answer = html.unescape(i.get("correct_answer"))
    answers.append(answer)

for i,j in zip(questions,answers):
    question_answer_pair.append([i,j])
