from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "plain"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"


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

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            return LeafNode("code", text_node.text, None)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {
                "href" : text_node.url
            })
        case TextType.IMAGE:
            return LeafNode("img", "", {
                "src" : text_node.url,
                "alt" : text_node.text,
            })
        case _:
            raise ValueError(f"ValueError: Incorrect text node type {text_node.text_type}")

