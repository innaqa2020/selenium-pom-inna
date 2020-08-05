# pytest_selenium_pom

This is a simple example of test scripts written using **Python**, **Selenium WebDriver**, **PyTest**
and **Allure**. 
This framework is utilizing Page Object Model (POM). 
conftest.py includes code to use specific chromedriver version based on your Operating System.
**ChromeDriver** version is 83 and located inside resources folder. 
Please update it according to your version of Google Chrome 
installed on your machine when running locally.

**Pre-requisites:**

Please make sure you have **Python** installed https://www.python.org/downloads/

Please make sure you have **PyCharm** installed https://www.jetbrains.com/pycharm/download/

To install necessary package using **PyCharm** (on **Windows 10**):

1. Open your project in **PyCharm**.
2. Click on **File -> Settings**.
3. In the search field type in **Interpreter**.
4. In the new window, click on **+** sign to add new packages.
5. Type in **selenium** and click on **Install Package**.
6. Type in **pytest** and click on **Install Package**.
7. Type in **allure-pytest** and click on **Install Package**.
7. Close Packages and Settings windows.

Navigate to **tests** folder.

You can run your test via terminal. 
Type **pytest -v filename** or **pytest -v** to run all tests in the folder and press Enter

You can run specific test groups (smoke, regression and etc) from command line. 
Type in **pytest -v -m smoketest** and press Enter

To run it via command line and generate Allure reports from command line:
Type in **py.test --alluredir=reports** and press Enter

To view your reports:
Type in **allure serve reports** and press Enter.
Reports will open in your default browser (I recommend Firefox or Chrome).

