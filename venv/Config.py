
from enum import Enum


group_id        = 188970185
token           = "8298b56e9563350669209c2bd41a555a1a9cc900aba663995fbd3b6a25454246035d8a4dadea101a7c5ef"
welcome_text    = "Вы меня успешно добавили в беседу! Теперь вам необходимо дать мне доступ к переписке и права администратора, а затем ввести команду /setup (ввести может только создатель для получения полномочий)  чтобы я мог начать работу"
helpMessage     = "... какой то текст ..."
errorAuthorityCommandExecution = "Команда не может быть применена к данному пользователю"

class AUTHORITY:
    MODERATOR       = 1
    ADMINISTRATOR   = 2
    SPECIAL_ADMIN   = 3
    CREATOR_LEVEL   = 4