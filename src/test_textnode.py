import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "google.ca")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text node 1", TextType.BOLD)
        node2 = TextNode("This is a text node 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node 1", TextType.BOLD,"text.com")
        node2 = TextNode("This is a text node 1", TextType.BOLD,"text.com")
        self.assertEqual(node, node2)
if __name__ == "__main__":
    unittest.main()
