LEXICON: dict[str, str] = {
    "/help": "Привет. Я предназначен для поиска скинов CS:GO со скидкой. Вот список доступных команд:\n"
             "/find - Начать поиск предметов.\n"
             "/discount - Узнать либо изменить текущую скидку.\n"
             "/min - Узнать либо изменить минимальный порог цены.\n"
             "/max - Узнать либо изменить максимальный порог цены.\n",

    "disc_change_error": "Скидка должна быть целым числом от 5 до 25, "
                         "попробуйте еще раз.\n\nЕсли вы передумали "
                         "- отправьте команду /cancel",

    "min_amount_invalid": "Минимальная цена должна быть целым числом от 1 до 4000, "
                          "попробуйте еще раз. Вы можете ввести свою цену "
                          "либо выбрать из предложенных вариантов.\n\nЕсли вы передумали "
                          "- отправьте команду /cancel",
                        
    "max_amount_invalid": "Максимальная цена должна быть целым числом от 5000 до 25000, "
                          "попробуйте еще раз. Вы можете ввести свою цену "
                          "либо выбрать из предложенных вариантов.\n\nЕсли вы передумали "
                          "- отправьте команду /cancel",

    "fsm_cancel": '"Охрана, у нас отмена!" ©\n\n'
                  "Чтобы вернуться к поиску в интересующей Вас категории"
                  "отправьте команду /find\n"
                  "Для настройки поиска воспользуйтесь меню.",

    "non_fsm_cancel": "Отменять нечего.\n"
                      "Чтобы начать поиск в интересующей Вас категории "
                      "отправьте команду /find",

    "echo": "Мой функционал ограничен, извините."
            "Для просмотра списка доступных команд введите /help",

    "prompt_text": "Введите новое значение или выберите из предложенных вариантов:",

    "category": "Выберите категорию для поиска",

    "action": "Выберите действие:",

    "current_disc": "Текущая скидка: {}%",

    "min_discount": "Нижний порог скидки при поиске изменен на {}%",

    "min_price": "Текущая минимальная цена: ${}",

    "change_min_price": "Нижний порог цены при поиске изменен на ${}",

    "max_price": "Текущая максимальная цена: ${}",

    "change_max_price": "Верхний порог цены при поиске изменен на ${}",
}

HANDLERS: dict[str, list] = {
    "current_min_price": [
        "Минимальная цена",
        "Минимальный порог",
        "Какая минималка",
        "Минималка",
        "Цена от",
        "Min price",
        "Price from",
    ],
    "current_max_price": [
        "максимальная цена",
        "максимальный порог",
        "Какая максималка",
        "Максималка",
        "Цена до",
        "Max price",
        "Price to",
    ],
    "cancel": [
        "cancel",
        "/cancel",
        "выйти",
        "отмена",
    ],
    "discount": [
        "скидка",
        "discount",
        "/discount",
    ],
    "find": [
        "find",
        "/find",
        "поиск",
        "категории",
    ],
    "help": [
        "/help",
        "help",
        "помощь",
        "список команд",
        "команды",
    ],
    "current_disc": [
        "текущая скидка",
        "узнать скидку",
    ],
    "change_disc": [
        "сменить скидку",
        "изменить скидку",
        "поменять скидку",
    ],
    "change_min_price": [
        "Изменить минимальную цену",
    ],

    "change_max_price": [
        "Изменить максимальную цену",
    ],
}
