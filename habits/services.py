import requests


def send_telegram_message(chat_id, message, bot_token):
    """Отправка сообщения в Telegram"""

    URL = "https://api.telegram.org/bot"
    response = requests.post(
        url=f"{URL}{bot_token}/sendMessage",
        data={
            'chat_id': chat_id,
            'text': message,
        }
    )


def create_message(habit):
    """ Функция создания сообщения """

    if habit.owner.chat_id:
        chat_id = habit.owner.chat_id
        message = f"Напоминание: {habit.action} в {habit.place} в {habit.time.strftime('%H:%M')}"

    if habit.reward:
        message += f" Награда за выполнение: {habit.reward}."

    if habit.related_habit:
        related_habit_action = habit.related_habit.action
        message += f" Связанная привычка: {related_habit_action}."

    return chat_id, message
