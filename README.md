# coinny
Minimum coin amount for given change calculator.

## Usage

Make sure you are using `python3`

Default coin set `[1, 2, 5, 10, 20, 50]`
 * Setup
```
pip install -r requirements.txt
```
* invoke tests
```
pytest
```
* invoke coinny app
```
python coinny.py
```
* You can use custom coin sets
```
$ python coinny.py 1 5 15 21 50 --amount 63
21 Coins x3
```
* help
```
python coinny.py --help
```