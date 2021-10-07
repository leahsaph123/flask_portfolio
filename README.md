Table of Contents
============

  * [Credits](#credits)
  * [Week 3](#week-3)
  * [Week 4](#week-4)
  * [Week 6](#week-5-and-week-6)
  * [Week 7](#week-7)

Credits
=====

Name | Github | Commits | Tasks | Scrumboard | Journal 
----------- | ----------- | ------------- | ------------- | ------------- | -----------
Leah Bogomolny | [@leahsaph123](https://github.com/leahsaph123) | [Commits](https://github.com/leahsaph123/flask_portfolio/commits?author=leahsaph123) ***FOR NOW DO Ctrl+F and search "leahsaph123" in order to see what I've done | [Tasks](https://github.com/leahsaph123/flask_portfolio/projects/1?card_filter_query=assignee%3Aleahsaph123) | [Scrumboard](https://github.com/leahsaph123/flask_portfolio/projects/1) | [Isabella Yan and Leah Bogomolny Journal](https://docs.google.com/document/d/1OXrhPY_AdWYU6Hmka9spMCCovSuUE5EzOlF2UmKu1cc/edit?usp=sharing) 
Isabella Yan | [@yqw7](https://github.com/yqw7) | [Commits](https://github.com/leahsaph123/flask_portfolio/commits?author=yqw7) | [Tasks](https://github.com/leahsaph123/flask_portfolio/projects/1?card_filter_query=assignee%3Ayqw7) | [Scrumboard](https://github.com/leahsaph123/flask_portfolio/projects/1) | [Isabella Yan and Leah Bogomolny Journal](https://docs.google.com/document/d/1OXrhPY_AdWYU6Hmka9spMCCovSuUE5EzOlF2UmKu1cc/edit?usp=sharing) 
Tigran Arakelov | [@Tigran7](https://github.com/Tigran7) | [Commits](https://github.com/leahsaph123/flask_portfolio/commits?author=Tigran7) | [Tasks](https://github.com/leahsaph123/flask_portfolio/projects/1?card_filter_query=assignee%3Atigran7) | [Scrumboard](https://github.com/leahsaph123/flask_portfolio/projects/1) | [Tigran Arakelov and Simon Brunzell Journal](https://docs.google.com/document/d/1ZmRTWw3wAjc18To9BVckSW1Xj8Yx1AtsTPls_FIshU8/edit?usp=sharing) 
Simon Brunzell | [@SimonBrunzell](https://github.com/SimonBrunzell) | [Commits](https://github.com/leahsaph123/flask_portfolio/commits?author=SimonBrunzell) | [Tasks](https://github.com/leahsaph123/flask_portfolio/projects/1?card_filter_query=assignee%3Asimonbrunzell) | [Scrumboard](https://github.com/leahsaph123/flask_portfolio/projects/1) | [Tigran Arakelov and Simon Brunzell Journal](https://docs.google.com/document/d/1ZmRTWw3wAjc18To9BVckSW1Xj8Yx1AtsTPls_FIshU8/edit?usp=sharing)

Week 7
====
10/4-10/8

Assignee | Requirements | Evidence
----------- | ----------- | -----------
Tigran | Multiply and Divide by 2 (Shift).  In this example, make the Bits change positions.  Start 2^0 to 2^15.  If you multiply by 2 then 2^0 bit becomes 2^1, 2^1 to 2^2.  If you divide 2^15 becomes 2^14 | 
Leah | Color Codes.  Display three rows of 8 bits.  Allow for code to be 0 to 255, show color for RGB.  Also, show color for R,G,B independently.  This may require a different HTML layout. | [ticket](https://github.com/leahsaph123/flask_portfolio/issues/55) and [proof](http://127.0.0.1:5000/hexcodes/) and [code](https://github.com/leahsaph123/flask_portfolio/blob/main/templates/hexcodes.html)
Leah | Logic Gates.   CB requires an understanding of Expressions.  These are routed in Logic Gates (as language is routed in Latin). Consider an entirely different presentation area and idea.  In this example, you may have two inputs (a,b) and see how changing those inputs changes logic gate outputs (c).  This will likely require a different HTML. | 
Simon | Extend/Switch ASCII  to Unicode.   Use representation of U-0000 to U-FFFF for your bits.  The extension of ASCII to Unicode mode allows you to show even more Characters and Character ranges | 
Isabella | Unsigned Addition, Subtraction (Default).  Whole Numbers. Max number move from 255 to 65535.  Essentially 8 bits to 16 bits.  16 bits is often called a "Short Integer". | 
Isabella | Signed Addition, Subtraction (Selection).  Integer Numbers.  Subtraction (8th bit is a Sign, max number is  +127 and negative -128, overflow now produces negative number.  If sign bit is set the calculation is 128-bits. | 


Week 5 and Week 6
====
9/20-9/24 and 9/28-10/1

Assignee | Requirements | Evidence
----------- | ----------- | -----------
Tigran | RGB Values with an Image, Backend... how would you write a message into image (Links to an external site.) and transport it to the Web? Look at Pillow Image write in Tester. | [ticket](https://github.com/leahsaph123/flask_portfolio/issues/41) and [link/screenshot](http://127.0.0.1:5000/rgb/) and [proof](https://github.com/leahsaph123/flask_portfolio/commit/56030a2c789ce6495c191a495ec4b43c46574b32) 
Leah | RGB Values with an Image, Backend... image files are really big, this would make a Programmer consider being efficiency in programming. What are the calculations? Could the image.py function "def image_data" more efficient? There is a science to writing efficient algorithms called Big O notation (Links to an external site.). Write image_data function to be more efficient according to Big O notation. | [ticket](https://github.com/leahsaph123/flask_portfolio/issues/39) and [proof1](http://127.0.0.1:5000/rgb/) and [proof2](https://github.com/leahsaph123/flask_portfolio/blob/main/algorithm/images.py)
Simon | RGB Values with an Image, New Development. explore and implement a new possibility in manipulating images | [ticket](https://github.com/leahsaph123/flask_portfolio/issues/40) and [proof](http://127.0.0.1:5000/rgb/) [proof lines 7-18](https://github.com/leahsaph123/flask_portfolio/blob/main/templates/rgb.html)
Isabella | RGB Values with an Image, Frontend... how would you change to grey scale dynamically? Look for Hack in code. | [ticket](https://github.com/leahsaph123/flask_portfolio/issues/42) and [proof](http://127.0.0.1:5000/rgb/) and [proof (lines 63-74](https://github.com/leahsaph123/flask_portfolio/blob/main/templates/rgb.html)
-- | Documentation.   Make a document and cite examples from code describing your project layout.  A. Discuss layout of files (Links to an external site.) and organizing (Links to an external site.) B. Discuss location of static organization (Links to an external site.).  C. Discuss HTML template layout (Links to an external site.) and specifically what you are doing to manage <head> (Links to an external site.) and <body> | [document](https://docs.google.com/document/d/1Sdt6OetUsmZb0D_ojYqkKFWJw0JJ3v56op0os-v5cic/edit?usp=sharing) and [ticket](https://github.com/leahsaph123/flask_portfolio/issues/61)

video: 
Week 4
====
9/13 - 9/17

Requirements | Evidence 
----------- | ----------- 
onclick event | [click](http://127.0.0.1:5000/leah)
transitions | [thumbs up](http://127.0.0.1:5000/simon)
animations | [cloud](http://127.0.0.1:5000/isabella) and [desktop](http://127.0.0.1:5000/Tigran)
adding ascii into binary | [binary](http://127.0.0.1:5000/binary/)
video | [video week 4](https://www.loom.com/share/f66b44d7fa2a4063a5e16b1ca6847bdc)

Week 3 
=====
9/7 - 9/10

Requirements | Evidence |
----------- | ----------- |
Font | default (for now)
Style | soothing and rounded edges
Color | sage green, dark green, and white
Leah | [About Leah](http://127.0.0.1:5000/leah)
Isabella | [About Isabella](http://127.0.0.1:5000/isabella)
Tigran | [About Tigran](http://127.0.0.1:5000/Tigran)
Simon | [About Simon](http://127.0.0.1:5000/simon)
Wireframes/Minilab Page | [Minilab](http://127.0.0.1:5000/minilab)
Binary | Notes found in journals under [credits](#credits)
Video | https://www.loom.com/share/1183c0fdf91d429882d5cc4170678371
