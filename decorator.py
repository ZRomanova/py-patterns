class TextTag:
    """Represents a base text tag"""

    def __init__(self, text: str) -> None:
        self._text = text

    def render(self) -> str:
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<i>{self._wrapped.render()}</i>"



    
simple_hello = TextTag("hello, world!")
special_hello = ItalicWrapper(BoldWrapper(simple_hello))
other_hello = BoldWrapper(ItalicWrapper(simple_hello))
print("before:", simple_hello.render())
# before: hello, world!
print("after:", special_hello.render())
print("other:", other_hello.render())
# after: <i><b>hello, world!</b></i>
# other: <b><i>hello, world!</i></b>

