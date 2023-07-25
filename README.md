## Table of contents
* [General Information](#general-information)
* [Step of using](#step-of-using)
* [Installation](#installation)


# General Information
I got a text file with more than 400 sample question of Azure AZ-900 Examination. However, the efficiency of studying is quite low if I just study this txt file as I can't really test how much I understand since I can see the correctly answers directly, besides, it's inconvenient for me to mark down the questions that I answered incorrectly. To improve my study process, I create a web page and make it like a multiple choice question paper, and Quiz result and correct answer will be provided too.


# Step of using 
1. Az_900_Quest.txt is look like this
```
**[⬆ Back to Top](#table-of-contents)**

### Your team needs to have a tool that provides a digital online assistant that can provide speech support. Which of the following service can be used for this purpose?

- [ ] Azure Machine Learning.
- [ ] Azure loT Hub.
- [x] Azure Al bot.
- [ ] Azure Functions.

```
2. execute QuestionList.py and access the web page by the link
3. In the page, you can see a set of Multiple-choice questions
4. tick the checkbox to answer
5. press submit for the result
6. result include:
- total number of question you answered
- how many questions you answer correctly
- the question + your answer + correct answer
- if your answer is incorrectly, the font color will be red

# Installation
```
pip install -r requirements.txt
```
