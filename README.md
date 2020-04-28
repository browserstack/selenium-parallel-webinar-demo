# Speed up your releases with parallelization in Selenium

This repository contains all the code to run from the Webinar held by [David Burns](https://github.com/automatedtester).

## Running the demos.

* You will need to check out the [demo site](https://github.com/AutomatedTester/demosite).
* Install the python requirements with `pip install -r requirements.txt`
* Run the tests
``` pytest path/to_tests.py```

* With some of the tests you can change the driver by simply changing the `--driver browser` argument. For running against Firefox you would do ```pytest parallel/site_tests.py --driver Firefox```.

* You can also use [BrowserStack](https://www.browserstack.com) if you set the following environment variables
```bash
export BSUSERNAME=browserstack_user
export BSPASSWORD=browserstack_key
```