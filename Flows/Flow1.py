from Flow import Flow
from Question import Question
import i18n

translator = i18n.Translator('data')


q1 = Question(0, translator.translate('intro'), "", [translator.translate('start')])
q2 = Question(1, translator.translate('stress_question'), "", [translator.translate('stress_option1'),
                                                                                translator.translate('stress_option2'),
                                                                                translator.translate(
                                                                                    'stress_option3')])
q3 = Question(2, "What is your favorite animal?", "", ["Cat", "Dog", "Bird", "Fish"])
q4 = Question(3, "What is your favorite food?", "", ["Pizza", "Burger", "Pasta", "Salad"])
flow = Flow([q1, q2, q3, q4])

flow.add_question()
flow.add_question()
flow.add_question()
flow.add_question()