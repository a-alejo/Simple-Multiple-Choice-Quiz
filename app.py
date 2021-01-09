from Question import Question

question_prompts = [
    'Which of the below option is an odd number?\n(a) 1\n(b) 4\n(c) 12\n(d) 22\n ',
    'What is New Mexico?\n(a) A country\n(b) A city\n(c) A state\n(d) An island\n ',
    '3/4 is an example of which of these?\n(a) A decimal\n(b) A fraction\n(c) An odd number\n(d) A rational number\n ',
    'The planet closest to the sun is...?\n(a) Earth\n(b) Mercury\n(c) Jupiter\n(d) Mars\n ',
]
# array of questions that can later be looped
questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b'),
    Question(question_prompts[3], 'b'),
]


# function to run the test and checks responses
def run_test(ask_questions):
    score = 0
    for ask in ask_questions:
        answer = input(ask.prompt)
        if answer == ask.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(ask_questions)) + ' correct!')


run_test(questions)
