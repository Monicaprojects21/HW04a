# HW04a
Develop with the Perspective of the Tester in mind

Q. Write a description of what you thought about when you were designing the code. What did you think was important to do to make it easy to test the program. What are some of the challenges that you faced when testing this assignment

Ans. I had to study this website, https://docs.github.com/en/rest, to learn about requests and the Github API. I achieved this by implementing constant files, which made my life simpler when I imported them into the gitapi.py file to obtain the desired outcomes. By developing a straightforward unittest package, self-certifying to the gihubapi, capturing and executing the package to the output, I was able to test my work. When I wanted to automate it, I utilized CircleCI and added commands for output to be added to the Test Result folder under text.xml file.

Configuring the config.yml file presented a hurdle for me during this. To receive my success status for this assignment, about 15 CircleCI actions were required.

[![Monica Mallamputti](https://circleci.com/gh/Monicaprojects21/SSW-567-HW04.svg?style=svg)](https://app.circleci.com/pipelines/github/Monicaprojects/SSW-567-HW04?branch=main&filter=all)
