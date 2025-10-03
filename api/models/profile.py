class Profile:
  def __init__(self, telegram="", name="", nickname="", birthday="", eyecolor=""):
    self.telegram = f"[{telegram}](https://t.me/{telegram})\n"
    self.name = name
    self.nickname = nickname
    self.birthday = birthday
    self.eyecolor = eyecolor
  def to_text(self):
    text=(
      f"АНКЕТА\n"
      f"tg: {self.telegram}\n"
      f"═══════════════════════════════════════\n"
    )
    if self.name:
      text += f"Имя: {self.name}\n"
    if self.nickname:
      text += f"Ник: {self.nickname}\n"
    if self.birthday:
      text += f"День рождения: {self.birthday}\n"
    if self.eyecolor:
      text += f"Цвет глаз: {self.eyecolor}\n"

    return text
