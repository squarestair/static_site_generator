import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode("This is a HTML node",None,None,{
            "href": "https://www.google.com",
            "target": "_blank",
        })
        res = node.props_to_html()
        props_to_html_test = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(res, props_to_html_test)

    def test_props_to_html_2(self):
        node = HTMLNode("This is a HTML node",None,None,{
            "href": "https://www.google.com",
            "target": "_blank",
            "test" : "test1",
        })
        res = node.props_to_html()
        props_to_html_test = ' href="https://www.google.com" target="_blank" test="test1"'
        self.assertEqual(res, props_to_html_test)
