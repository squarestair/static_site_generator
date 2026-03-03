
from textnode import TextType,TextNode

def main():
    tn = TextNode("google",TextType.ITALIC,"www.google.ca")
    tn2 = TextNode("google",TextType.ITALIC,"www.google.ca")
    tn3 = TextNode("google",TextType.CODE,"www.google.ca")
    tn4 = TextNode("test",TextType.CODE,"code.com")
    print(tn)
    print(tn == tn2)
    print(tn == tn3)
    print(tn4)



main()

