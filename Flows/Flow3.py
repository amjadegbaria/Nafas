from classes.Question import Question
from classes.Flow import Flow
import i18n

translate = i18n.Translator('data').translate

questions = {
    "intro1": Question(
        id="intro1",
        text=translate("intro1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="intro2"
    ),
    "intro2": Question(
        id="intro2",
        text=translate("intro2"),
        media="",
        media_type="",
        options={translate("yes_sure"): "intro3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "intro3": Question(
        id="intro3",
        text=translate("intro3"),
        media="",
        media_type="",
        options={translate("promise"): "intro4"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "intro4": Question(
        id="intro4",
        text=translate("intro4"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="intro5"
    ),
    "intro5": Question(
        id="intro5",
        text=translate("intro5"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="intro6"
    ),
    "intro6": Question(
        id="intro6",
        text=translate("intro6"),
        media="logos.jpeg",
        media_type="image",
        options={},
        keyboard_type="inline",
        next_question_id="intro7"
    ),
    "intro7": Question(
        id="intro7",
        text=translate("intro7"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="intro8"
    ),
    "intro8": Question(
        id="intro8",
        text=translate("intro8"),
        media="",
        media_type="",
        options={translate('ready'): "stress1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress1": Question(
        id="stress1",
        text=translate("stress_question"),
        media="",
        media_type="",
        options={translate('stress_option1'): "stress1_1", translate('stress_option2'): "stress1_2", translate('stress_option3'): "stress1_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress1_1": Question(
        id="stress1_1",
        text=translate("stress_question_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="stress1_4"
    ),
    "stress1_2": Question(
        id="stress1_2",
        text=translate("stress_question_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="stress1_4"
    ),
    "stress1_3": Question(
        id="stress1_3",
        text=translate("stress_question_3"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="stress1_4"
    ),
    "stress1_4": Question(
        id="stress1_4",
        text=translate("stress_question_4"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="exc1"
    ),
    "exc1": Question(
        id="exc1",
        text=translate("exc1"),
        media="https://www.youtube.com/shorts/9JhTMTksk9s",
        media_type="youtube",
        options={},
        keyboard_type="inline",
        next_question_id="exc1_2"
    ),
    "exc1_2": Question(
        id="exc1_2",
        text=translate("exc1_2"),
        media="",
        media_type="",
        options={translate("OK"): "exc1_4"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "exc1_3": Question(
        id="exc1_3",
        text=translate("exc1_3"),
        media="",
        media_type="",
        options={translate("OK"): "exc1_4"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "exc1_4": Question(
        id="exc1_4",
        text=translate("exc1_4"),
        media="",
        media_type="",
        options={translate("yes_next"): "exc2"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "exc2": Question(
        id="exc2",
        text=translate("exc2"),
        media="",
        media_type="",
        options={translate("ready"): "exc2_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "exc2_1": Question(
        id="exc2_1",
        text="",
        media="Countdown.mp4",
        media_type="video",
        options={translate('done'): "exc2_3"},
        keyboard_type="inline",
        next_question_id="exc2_2"
    ),
    "exc2_2": Question(
        id="exc2_2",
        text=translate("exc2_2"),
        media="Countdown.mp4",
        media_type="video",
        options={translate('done'): "exc2_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "exc2_3": Question(
        id="exc2_3",
        text=translate("exc2_3"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="exc2_4"
    ),
    "exc2_4": Question(
        id="exc2_4",
        text=translate("exc2_4"),
        media="",
        media_type="",
        options={translate("ready"): "exc3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "exc3": Question(
        id="exc3",
        text=translate("exc3"),
        media="https://www.youtube.com/watch?v=1N1vtQQ9ij0",
        media_type="youtube",
        options={},
        keyboard_type="inline",
        next_question_id="exc3_1"
    ),
    "exc3_1": Question(
        id="exc3_1",
        text=translate("exc3_1"),
        media="",
        media_type="",
        options={translate('yalla'): "exc3_2"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "exc3_2": Question(
        id="exc3_2",
        text=translate("exc3_2"),
        media="https://www.youtube.com/watch?v=UfcAVejslrU",
        media_type="youtube",
        options={},
        keyboard_type="inline",
        next_question_id="exc3_3"
    ),
    "exc3_3": Question(
        id="exc3_3",
        text=translate("exc3_3"),
        media="",
        media_type="",
        options={translate('done'): "end"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "end": Question(
        id="end",
        text=translate("end"),
        media="",
        media_type="",
        options={"1": "end_1", "2": "end_1", "3": "end_1", "4": "end_1", "5": "end_1", "6": "end_1", "7": "end_1", "8": "end_1", "9": "end_1", "10": "end_1"},
        keyboard_type="reply",
        next_question_id=""
    ),
    "end_1": Question(
        id="end_1",
        text=translate("end_1"),
        media="end.webp",
        media_type="image",
        options={},
        keyboard_type="reply",
        next_question_id=""
    )
}

# Initialize Flow
flow = Flow("flow3", questions)