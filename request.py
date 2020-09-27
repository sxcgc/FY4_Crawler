from lxml import etree
import codecs

f = codecs.open("1.txt", "r", "utf-8")
content = f.read()
f.close()
tree = etree.HTML(content)
a = tree.xpath('//*[@id="pager"]/div/a[7]')

