# Testing

Return back to the [README.md](README.md) file.

To ensure that Back to Red Dwarf works effectively over a number of sites and devices, I have prepared details and screenshots for you to see the testing I have done to ensure it is very reliable..

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Pimmz/project-3/main/run.py) | ![screenshot](documentation/linter.png) | No errors |


## Browser Compatibility

I have tested BAck to Red Dwarf on four different browsers. The first was Chrome, the second was Firefox, the third was Brave and the fourth was Opera. I would have liked to test on Safari but unfortunately, I don’t have access to an Apple device.

- [Chrome](https://www.google.com/chrome)
- [Firefox](https://www.mozilla.org/firefox/developer)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)


I've tested my deployed project on multiple browsers to check for compatibility issues. To ensure that all are working correctly I have also tested for responsiveness on desktop, tablet and mobile.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome Desktop| ![screenshot](documentation/chrome-desktop.png) | Works as expected |
| Chrome Tablet | ![screenshot](documentation/chrome-tablet.png) | Works as expected |
| Chrome Mobile| ![screenshot](documentation/chrome-mobile.png) | Works as expected |
| Firefox Desktop| ![screenshot](documentation/firefox-desktop.png) | Works as expected |
| Firefox Tablet| ![screenshot](documentation/firefox-tablet.png) | Works as expected |
| Firefox Mobile| ![screenshot](documentation/firefox-mobile.png) | Works as expected |
| Brave Desktop| ![screenshot](documentation/brave-desktop.png) | Works as expected |
| Brave Tablet| ![screenshot](documentation/brave-tablet.png) | Works as expected |
| Brave Mobile| ![screenshot](documentation/brave-phone.png) | Works as expected |
| Opera Desktop| ![screenshot](documentation/opera-desktop.png) | Works as expected |
| Opera Tablet| ![screenshot](documentation/opera-tablet.png) | Works as expected |
| Opera Mobile| ![screenshot](documentation/opera-mobile.png) | Works as expected |
| x | x | repeat for any other tested browsers |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Iphone se | ![screenshot](documentation/iphone-se.png) | Works as expected |
| Ipad mini | ![screenshot](documentation/ipad-mini) | Works as expected |
| Pixel 5| ![screenshot](documentation/pixel5.png) | Works as expected |
| S20 Ultra | ![screenshot](documentation/S20Ultra.png) | Works as expected |
| Surface Pro | ![screenshot](documentation/surfacepro.png) | Works as expected |
| Galaxy fold | ![screenshot](documentation/fold.png) | Works as expected |
| Nest | ![screenshot](documentation/nest.png) | Works as expected |


## Lighthouse Audit

I did complete a lighthouse test. However my mentor advised me to take it out of my testing file due to python being a backend program.


## Bugs

When completing the project I only came across the following the error message:

- Python `E501 line too long` (98 > 79 characters)

    ![screenshot](documentation/error.png)

    - To fix this, I reduced down the length of the line by rewording the sentence so that it was under 79 characters.
    - I also used the print("") if the next line character(\n) was pushing the line length just over the allowed characters. 

- Traceback (most recent call last): File "/app/run.py", line 1, in <module>
  import gspread ModuleNotFoundError: No module named 'gspread'

    ![screenshot](documentation/error1.png)

    - This was caused due to an updated worksheet in codeanywhere as I had run out of hours. The gspread module had been deleted so I had to reinstall "pip install gspread" to correct the issue.
    - The requirements txt file had also been deleted. So to fix this I put in "pip3 freeze > requirements.txt" in the terminal and then saved the changes. This then meant that it could communicate with heroku and is working perfectly as far as I am aware of.

**Open Issues**

There are no open issues that I am aware of. Issues can be tracked [here](https://github.com/Pimmz/Project-3/issues).


## Unfixed Bugs

There are no remaining bugs that I am aware of.