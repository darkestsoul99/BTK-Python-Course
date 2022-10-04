html_doc = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charste="UTF-8">
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>
    <h1 id="header">
        Python kursu
    </h1>

    <div class="grup1">
        <h2>
        Programlama
        </h2>

        <ul>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup1">
        <h2>
        Programlama
        </h2>

        <ul>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
        </ul>
    </div>
</body>
</html>"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head 
result = soup.body

result = soup.title.name
result = soup.title.string

result = soup.h1 
result = soup.h2 
result = soup.h2.name
result = soup.h2.string

result = soup.find_all('h2')
result = soup.find_all('h2')[1]

result = soup.div.findChildren()

result = soup.div.findNextSibling()

print(result)