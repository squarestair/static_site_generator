from enum import Enum
import re
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
        return f'TextNode("{self.text}",{self.text_type},{self.url})'

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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Unclosed tags")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i],TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

def split_nodes_image(old_nodes):
    # print(f"\n Testing: {old_nodes}")
    new_nodes = []
    for old_node in old_nodes:
        sections = []
        extracted_md_list = extract_markdown_images(old_node.text)
        if len(extracted_md_list) == 0:
            sections.append(old_node)
            continue
        working_string = old_node.text
        # print(working_string)
        for count, (img_alt, img_src) in enumerate(extracted_md_list):
            # print(f"Iter= {count} CHECKING extract_md_list: ", img_alt,img_src)
            temp = working_string.split(f"![{img_alt}]({img_src})",1)

            if working_string != '' and temp[0] != '':
                sections.append(TextNode(temp[0],TextType.TEXT))
            sections.append(TextNode(f"{img_alt}",TextType.IMAGE,f"{img_src}"))

            working_string = re.sub(r"^.*?!\[(.*?)\]\((.*?)\)",'',working_string)
            # print("TEMP : ", temp)
            # print("working_string : ", working_string)
            # print(f"sections after: {sections}")
            # print("\n end")
        if working_string != '':
            sections.append(TextNode(working_string,TextType.TEXT))
        new_nodes.extend(sections)
    # print("Final:", new_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    # print(f"\n Testing: {old_nodes}")
    new_nodes = []
    for old_node in old_nodes:
        sections = []
        extracted_md_list = extract_markdown_links(old_node.text)
        if len(extracted_md_list) == 0:
            sections.append(old_node)
            continue
        working_string = old_node.text
        # print(working_string)
        for count, (link_alt, link_src) in enumerate(extracted_md_list):
            # print(f"Iter= {count} CHECKING extract_md_list: ", img_alt,img_src)
            temp = working_string.split(f"[{link_alt}]({link_src})",1)

            if working_string != '' and temp[0] != '':
                sections.append(TextNode(temp[0],TextType.TEXT))
            sections.append(TextNode(f"{link_alt}",TextType.LINK,f"{link_src}"))

            working_string = re.sub(r"^.*?\[(.*?)\]\((.*?)\)",'',working_string)
            # print("TEMP : ", temp)
            # print("working_string : ", working_string)
            # print(f"sections after: {sections}")
            # print("\n end")
        if working_string != '':
            sections.append(TextNode(working_string,TextType.TEXT))
        new_nodes.extend(sections)
    # print("Final:", new_nodes)
    return new_nodes

def split_nodes_image_SOLUTION(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link_SOLUTION(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
