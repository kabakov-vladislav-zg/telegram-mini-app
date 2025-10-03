class Profile:
  def __init__(self, telegram="", name="", nickname="", birthday="", eyecolor=""):
    self.telegram = telegram
    self.name = name
    self.nickname = nickname
    self.birthday = birthday
    self.eyecolor = eyecolor
  def to_text(self):
    text=(
      f"<b>АНКЕТА</b><br/>"
      f"<b>tg:</b> <a href=\"https://t.me/{self.telegram}\">{self.telegram}</a><br/>"
      f"═══════════════════════════════════════<br/>"
    )
    if self.name:
      text += f"<b>Имя:</b> {self.name}<br/>"
    if self.nickname:
      text += f"<b>Ник:</b> {self.nickname}<br/>"
    if self.birthday:
      text += f"<b>День рождения:</b> {self.birthday}<br/>"
    if self.eyecolor:
      text += f"<b>Цвет глаз:</b> {self.eyecolor}<br/>"

    return text
