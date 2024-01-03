import xml.dom.minidom
def main():
    doc=xml.dom.minidom.parse("sample.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    name=doc.getElementsByTagName("name")
    print("%d name: "%name.index)
    for skill in name:
        print(skill.getAttribute("comany:"))
if __name__=='__main__':
    main()