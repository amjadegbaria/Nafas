from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class Question:
    def __init__(self, id: int, text: str, image: str, options: list):
        self._id = id
        self._text = text
        self._image = image
        self._options = options
        self._markup = self._create_inline_keyboard(options)

    # Getter and Setter for id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # Getter and Setter for text
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    # Getter and Setter for image
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    # Getter and Setter for options
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value
        self._markup = self._create_inline_keyboard(value)

    # Getter for markup
    @property
    def markup(self):
        return self._markup

    def _create_inline_keyboard(self, options):
        keyboard = []
        for option in options:
            keyboard.append([InlineKeyboardButton(option, callback_data=f"{self._id}-{option}")])
        return InlineKeyboardMarkup(keyboard)

    def create_handler(self, option_index):
        async def handler(update, context):
            query = update.callback_query
            chat_id = query.message.chat_id
            await query.answer()

            # Handle the selected option
            await context.bot.send_message(chat_id=chat_id, text=f"You chose: {self.options[option_index - 1]}")

            # Get the next question
            question = context.user_data['flow'].get_next_question()
            if question:
                await context.bot.send_message(chat_id=chat_id, text=question.text, reply_markup=question.markup)
            else:
                await context.bot.send_message(chat_id=chat_id, text="No more questions.")

        return handler
