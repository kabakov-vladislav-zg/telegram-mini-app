class Profile:
  def __init__(self, userId="", username="", name="", nickname="", birthday="", eyecolor=""):
    self.userId = userId
    self.username = username
    self.name = name
    self.nickname = nickname
    self.birthday = birthday
    self.eyecolor = eyecolor
  def to_text(self):
    text=(
      f"<b>АНКЕТА</b>\n"
      f"<b>tg:</b> <a href=\"https://t.me/{self.username}\">{self.username}</a>\n"
      f"═══════════════════════════════════════\n"
    )
    if self.name:
      text += f"<b>Имя:</b> {self.name}\n"
    if self.nickname:
      text += f"<b>Ник:</b> {self.nickname}\n"
    if self.birthday:
      text += f"<b>День рождения:</b> {self.birthday}\n"
    if self.eyecolor:
      text += f"<b>Цвет глаз:</b> {self.eyecolor}\n"

    return text
