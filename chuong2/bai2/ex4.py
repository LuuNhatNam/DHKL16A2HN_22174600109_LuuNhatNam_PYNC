import xml.dom.minidom
def main():
    doc = xml.dom.minidom.parse("sample.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    staff = doc.getElementsByTagName("staff")
    

    print( staff)
    for skill in staff:
        print(skill.getElementsByTagName("name"))
        print(skill.getAttribute("id"))
        print(skill.getElementsByTagName("salary"))
if __name__=="__main__":
    main()