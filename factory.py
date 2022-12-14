class RussianLocalizer:
    """A simple localizer"""

    def __init__(self) -> None:
        self.translations = {"dog": "собака", "cat": "кошка"}

    def localize(self, msg: str) -> str:
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply echoes the message"""

    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") -> object:

    """Factory"""
    localizers = {
        "English": EnglishLocalizer,
        "Russian": RussianLocalizer,
    }

    return localizers[language]()

# Create our localizers
e, g = get_localizer(language="English"), get_localizer(language="Russian")
# Localize some text
for msg in "dog parrot cat bear".split():
  print(e.localize(msg), g.localize(msg))
# dog собака
# parrot parrot
# cat кошка
# bear bear


