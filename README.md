# Widget API Test
### by Worakorn Chaichakan

Prerequisites
=============
* Python 3
* Robot Framework

How to Run
==========
1. Open Termainal/Command Prompt
2. Go to the target folder
3. Run the following command

`robot widget_testcases.robot`

Test Coverage
=============


|Search Filter        |Test Case ID|     ad      | news story  |image gallery|  query   |   video  |
|---------------------|------------|-------------|-------------|-------------|----------|----------|
|device - mobile      |    TC1     |      Y      |       Y     |       N     |     Y    |     N    |
|device - desktop     |    TC2     |      Y      |       Y     |       N     |     Y    |     N    |
|device - all         |    TC3     |      Y      |       Y     |       Y     |     Y    |     Y    |
|site - perthnow      |    TC4     |      Y      |       Y     |       Y     |     Y    |     N    |
|site - dailytelegraph|    TC5     |      Y      |       Y     |       Y     |     N    |     Y    |
|site - theaustralian |    TC6     |      Y      |       Y     |       N     |     Y    |     Y    |
|site - all           |    TC7     |      Y      |       Y     |       Y     |     Y    |     Y    |


Y - Yes, a widget will show
N - No, a widget won't show

## Invalid Scenarios

* device <> mobile, desktop or all
* device is blank
* site <> perthnow, dailytelegraph, theaustralian or all
* site is blank
