from bs4 import BeautifulSoup

html = """
<html>
<head>
    <title>Practice Page</title>
</head>
<body>

<h1>Main Heading</h1>
<h2>Sub Heading 1</h2>
<h3>Sub Heading 2</h3>

<p>This is first paragraph.</p>
<p>This is <b>bold text</b> inside paragraph.</p>

<a href="https://google.com" class="search">Google</a>
<a href="https://github.com">GitHub</a>

<img src="image1.jpg" alt="Image One">
<img src="image2.png" alt="Image Two">

<table border="1">
    <tr>
        <th>Name</th>
        <th>Age</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>22</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>25</td>
    </tr>
</table>

</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Extract Title
print("Title:", soup.title.text)

# Extract All Paragraphs
print("\nParagraphs:")
for p in soup.find_all("p"):
    print(p.text)

#Extract All Links and Count
links = soup.find_all("a")
print("\nTotal Links:", len(links))
for link in links:
    print(link.text, "->", link.get("href"))

#  Extract Attributes (Example: First link)
first_link = soup.find("a")
print("\nFirst Link Class:", first_link.get("class"))

#  Extract First h2
print("\nFirst h2:", soup.find("h2").text)

#  Extract Bold Text
print("\nBold Text:")
for b in soup.find_all("b"):
    print(b.text)

#  Extract All href Values
print("\nAll href values:")
for link in links:
    print(link.get("href"))

# Get All Text Without Tags
print("\nAll Text:")
print(soup.get_text())

#  Extract All Headings (h1-h6)
print("\nAll Headings:")
for i in range(1, 7):
    for tag in soup.find_all(f"h{i}"):
        print(tag.text)

# Extract Table Data
print("\nTable Data:")
table = soup.find("table")
rows = table.find_all("tr")
for row in rows:
    cols = row.find_all(["td", "th"])
    for col in cols:
        print(col.text, end=" | ")
    print()

# Extract Images
print("\nImages:")
for img in soup.find_all("img"):
    print("Source:", img.get("src"), "| Alt:", img.get("alt"))