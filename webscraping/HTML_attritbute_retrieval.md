# HTML
To understand web scraping, it's essential to have a basic understanding of HTML.
Hypertext Markup Language is at the core of web pages.
HTML is a markup language used to create the structure and content of web pages. It consists of a set of tags that define elements on a web page. These elements can be text, images, links, forms, and more. HTML is the language that web browsers use to render web content.

### HTML Structure:
A typical HTML document has a hierarchical structure with the following key components:

`<!DOCTYPE>` declaration: specifies the document type and version of HTML being used.<br>
`<html>` element: The root element that wraps the entire web page.<br>
`<head>` element: contains metadata, such as the page title and links to external resources like CSS and JavaScript files.<br>
`<body>` element: contains the visible content of the web page, including text, images, and links.

**Attributes:**
HTML elements can have attributes that provide additional information about the element. For example, the `<a>` (anchor) element often has an `href` attribute that specifies the link's destination.

**Inspecting Web Pages:**
To scrape data from a website, you'll need to inspect the HTML structure of the page. Most web browsers offer developer tools that allow you to view the source code of a web page. This is where you can identify the HTML elements you want to extract data from.

In the Chrome browser, right-click and choose inspect. It opens the Chrome Developer Tools panel.

<img width="1439" alt="Screenshot 2023-11-06 at 9 49 39 PM" src="https://github.com/Riyavarshini/webscrapping_basic/assets/117080445/02d5f186-9827-4662-a3a6-bb6ea886e926">

### List of tags:
Here I am listing a few tags that we come across in our scraping process.
1. `<span>`:
The span tag is an inline HTML element used to group or style a specific section of text within a larger block of text. It does not add any line breaks or create a separate block; it's primarily used for applying CSS styles or JavaScript functionality to a specific portion of text.

2. `<h2>`:
The h2 tag is a heading element in HTML. It represents a second-level (or "level 2") heading and is typically used to mark subsections or subheadings within a document. Headings are often displayed with larger and bolder text by default.

3. `<a>`:
The a tag is used to create hyperlinks in HTML. It stands for "anchor" and is commonly used to link to other web pages, resources, or locations within the same page. The href attribute within the a tag specifies the URL or destination of the link.

4. `<div>`:
The div tag is a block-level HTML element used for grouping and structuring content within a web page. It is often used to create containers or sections for layout and styling purposes. The div element is versatile and can be styled with CSS to create various layouts and divisions within a page.

I hope you have some understanding of HTML, its structure, and its tags and elements.
To better understand it, just explore it yourself in your Chrome developer tool panel.

---
## HOW TO FIND REQUIRED ATTRIBUTES IN HTML CODE OF A WEBPAGE TO RETRIEVE REQUIRED DATA

1. Go to your required webpage and open the Chrome developer tool panel. (right-click -> inspect)<br>
<img width="1439" alt="Screenshot 2023-11-06 at 9 49 39 PM" src="https://github.com/Riyavarshini/webscrapping_basic/assets/117080445/02d5f186-9827-4662-a3a6-bb6ea886e926">

2. We have the option to choose the required element just by hovering over our webpage in this panel.It is found in the top left corner.
<img width="373" alt="Screenshot 2023-11-07 at 6 56 12 PM" src="https://github.com/Riyavarshini/webscrapping_basic/assets/117080445/32eebb4e-3a5f-4a10-acd5-3c384b902714">

3. Now hover and click on the first book title. It automatically highlights the html code of this block.
<img width="1216" alt="Screenshot 2023-11-07 at 6 59 32 PM" src="https://github.com/Riyavarshini/webscrapping_basic/assets/117080445/b8064bf9-5f01-46c7-97c5-402976540791">

So here, we need to get a hyperlink to the product. So it is inside the `<a> .... </a>` tag. This tag has elements to identify it.
They are `class = 's-item__link'`, `href = "href="https://www.ebay.com/itm/266370569678?hash=item3e04ec55ce:g:WEw..%2FP24cawfrFGZrSEwIiR1kdBqGeKWTWV8%2FmRjv%2BadzvSs%3D%7Ctkp%3ABFBMtKaEn_Vi"`
We use this in our code.

4. To retrieve information about each product, we visit the link page and again use the above method to get the tag and elements to use in our code.
**For example: Title of book**
<img width="1370" alt="Screenshot 2023-11-07 at 7 15 05 PM" src="https://github.com/Riyavarshini/webscrapping_basic/assets/117080445/87751363-11f6-4b88-85ee-9d3d0b2a6ac0">

The required data is inside the tag.

```html
<span> class='ux-textspans ux-textspans--BOLD>Vintage Hardy Boys Blue Back Edition Books (U-Pick) </span>
```
Class is an element of this tag, and the data is the text part of this tag.
