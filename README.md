# PyWebReport

Generate html reports by sources such as unittest、pytest and any more  

like allure but as do-one-thing-do-it-well for **python community**.  

## Current progress

- [x] Feasibility Study.(it seems feasible)  
- [ ] Report designing 🚧👷(you can see progress [here](https://yongchin0821.github.io/pywebreport/))  
- [x] pytest adaptation  
- [x] unittest adaptation  

## My initial idea

We may extract results in different formats from pytest、unittest. if there have a formatter to format results into the  
common datas,then we can use this datas to make html report.  

![](./idea.png)  

## Installation

```
# pip install pywebreport
```

or you can clone this rep, and run the command to install

```shell
# python setup.py install
```

## Usage

### pytest

just run the command

```shell
# pytest -q --report result/report.html
```

or in **.py** you can run script like:

```python
import pytest

if __name__ == '__main__':
    args = ['./', '-q', '--report', 'result/report.html']
    pytest.main(args)
```

### unitest

**import the WebReportRunner**, and just give the TestSuite to WebReportRunner.
no matter how TestSuite is collected，
**just give the suites to WebReportRunner**

like this:

```python
import unittest
from test_success import UnitTestSuccessCase
from pywebreport import WebReportRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # suite.addTest(UnitTestSuccessCase("test_case2"))
    # suite.addTest(UnitTestSuccessCase("test_err_print"))
    # suite.addTest(loader.loadTestsFromTestCase(UnitTestCase))
    # suite = loader.loadTestsFromTestCase(UnitTestCase)

    suite.addTest(loader.discover("."))

    runner = WebReportRunner(report="result/report.html")
    test_result = runner.run(suite)
```

## Recruitment

This is an incubation project  

hope and invite you to join me if you are interested in this project  

- [ ] a contributor who can design the report style  
- [ ] a contributor who is familiar with pytest\unittest
