#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random, os

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 
            'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 
            'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

            #TODO: follow the 'generating random quiz files' project in the textbook to fill in this file.
            #TODO: however, make the following modificatiosn to the instructions on the textbook:
            #       1. instead of making 35 quiz versions, you'll only make 5 quiz versions
            #       2. instead of creating quiz and answer files in the current working directory, create a folder titled 'quizzes' and another folder titled 'answers'.
            #       3. place the randomly-generated quizzes in the 'quizzes' directory.
            #       4. plaec the corresponding answers in the 'answers' directory

            
            

answerspath = r'./answers'
quizpath = r'./quizzes'
quizzQty = 5

#The quiz data; keys are questions and values are answers
answerspath =  r'./answers'
if not  os.path.exists(answerspath):
    os.makedirs(answerspath)
quizpath = r'./quizzes'
if not os.path.exists(quizpath):
    os.makedirs(quizpath)
 # Create answer file
#answerKeyFile = open('./answers/quiz_answers.txt', 'w')
for quizNum in range(5):
    # Create the quiz and answer key files.
    with    open('./quizzes/capitalsquiz%s.txt' % (quizNum + 1), 'w') as quizFile, \
            open('./answers/capital_answer%s.txt' % (quizNum + 1), 'w') as answerKeyFile:
       
            # Write out the header for the quiz.
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write(
            (' ' * 20) +
            'State Capitals Quiz (Form %s)' % (quizNum + 1)
        )
        quizFile.write('\n\n')

        # Shuffle the order of the states.
        states = list(capitals.keys())
        random.shuffle(states)

        # Loop through all 50 states, making a question for each.
        for questionNum in range(50):
            # Get right and wrong answers.
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            # Write the question and the answer options to the quiz file.
            quizFile.write('%s. What is the capital of %s?\n' %
                           (questionNum + 1, states[questionNum]))
            for i in range(4):
                quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
                quizFile.write('\n')
                # Write the answer key to a file.
                answerKeyFile.write(
                    '%s. %s\n' % (
                        questionNum + 1,
    'ABCD'[answerOptions.index(correctAnswer)]))
            
            

