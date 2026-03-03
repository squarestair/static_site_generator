from enum import Enum

class TextType(Enum):
    TEXT = "plain"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node) -> bool:
        te = text_node.text == self.text
        tt = text_node.text_type == self.text_type
        tu = text_node.url == self.url
        return te and tt and tu

    def __repr__(self) -> str:
        return f'TextNode({self.text},{self.text_type},{self.url})'
