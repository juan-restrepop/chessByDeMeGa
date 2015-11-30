# python chess game and ml

===

#### Contributors:

* [loops](https://github.com/juan-restrepop/)
* [pach](https://github.com/rodfr/)
* [shin](https://github.com/santiaago/)


#### Test:

To run test on chess_game do: `python chess_game_test.py -v`

To run test on chess_board do: `python chess_board_test.py -v`

To run *both tests* run:
    `python -m unittest discover ./ -p '*_test.py'` 

### Code coverage by test
To do the following the package `coverage.py` needs to be installed.
To get the test coverage do:
    `coverage run --source ./ -m unittest discover ./ -p '*_test.py'`
    `coverage report -m`

#### Launch basic game:

To launch a basic game do : `python launch.py`