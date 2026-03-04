
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("NotImplementedError")

    def props_to_html(self):
        if not self.props:
            return ''
        res = ""
        for prop in self.props:
            fs = f' {prop}="{self.props[prop]}"'
            res += fs
        return res


    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None) -> None:
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value == None:
            raise ValueError("ValueError")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
