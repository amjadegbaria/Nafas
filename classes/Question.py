from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InputMediaPhoto, \
    InputMediaVideo


class Question:
    def __init__(self, id: str, text: str, media: str, media_type: str, options: dict, next_question_id: str,
                 keyboard_type: str = 'inline'):
        """
        Initializes a question with its ID, text, media, media type, options, and keyboard type.
        :param id: Unique identifier for the question
        :param text: Text of the question
        :param media: URL of the media (image, YouTube, video, or game)
        :param media_type: Type of the media ('image', 'youtube', 'video', 'game')
        :param options: Dictionary where keys are button texts and values are the next question IDs
        :param keyboard_type: Type of keyboard to use ('inline' or 'reply')
        :param next_question_id: Next question id in case no options defined
        """
        self._id = id
        self._text = text
        self._media = media
        self._media_type = media_type
        self._options = options
        self.keyboard_type = keyboard_type
        self._markup_inline = self._create_inline_keyboard(options)
        self._markup_reply = self._create_reply_keyboard(options)
        self.next_question_id = next_question_id


    def _create_inline_keyboard(self, options: dict):
        """
        Creates an inline keyboard markup with buttons arranged in two columns.
        Each button is labeled with the key of the dictionary and sends the corresponding value as a callback data.
        """
        button_texts = list(options.keys())
        keyboard = []
        if len(options) > 5:
            for i in range(0, len(button_texts), 2):
                row = [
                    InlineKeyboardButton(text, callback_data=text)
                    for text in button_texts[i:i + 2]
                ]
                keyboard.append(row)
        else:
            keyboard = [[InlineKeyboardButton(text, callback_data=text)] for text, value in options.items()]
        return InlineKeyboardMarkup(keyboard)
    def _create_reply_keyboard(self, options: dict):
        """
        Creates a reply keyboard markup with buttons arranged in two columns.
        """
        button_texts = list(options.keys())
        keyboard = []
        for i in range(0, len(button_texts), 2):
            row = [KeyboardButton(text) for text in button_texts[i:i + 2]]
            keyboard.append(row)
        return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    def get_markup(self):
        """
        Returns the appropriate markup based on the keyboard type.
        """
        if self.keyboard_type == 'inline':
            return self._markup_inline
        elif self.keyboard_type == 'reply':
            return self._markup_reply
        elif len(self._options) == 0:
            return ""

        else:
            raise ValueError("Invalid keyboard type. Choose 'inline' or 'reply'.")

    def get_media_type(self):
        return self._media_type

    def get_id(self):
        return self._id

    def get_media(self):
        """
        Returns the media and its type. This method provides different content based on the media type.
        """
        if self._media_type == 'image':
            return InputMediaPhoto(media=self._media)
        elif self._media_type == 'video':
            return InputMediaVideo(media=self._media)
        elif self._media_type == 'youtube':
            # YouTube URLs should be handled as text
            return self._media
        elif self._media_type == 'game':
            # Games are usually sent using the game method
            return self._media
        else:
            raise ValueError("Invalid media type. Choose 'image', 'video', 'youtube', or 'game'.")

    def get_question_text(self):
        return self._text

    def get_options(self):
        return self._options

    def get_next_question(self, answer):
        if answer:
            return self._options.get(answer)
        return self.next_question_id

    def is_last(self):
        if len(self._options) == 0 and len(self.next_question_id) == 0:
            return True
        return False
