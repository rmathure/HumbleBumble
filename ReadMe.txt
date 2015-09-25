The position of pieces needs to specified during instantiation as well as their color.

The position should be specified as 'b', '4' which means that a piece is positioned at B4.

e.g. piece = Pawn(boardObject, 'b', '4', 'white') # where white is the color of the piece

The above statement should initialize a white pawn at b4.
The board Object should be initialized and passed as a parameter for every piece constructor.

======================================================================================

Alternative method to specify the chess board configuration:

Create input.txt file in Humblebundle project directory.
The first line should specify the color of the player who is to play.

The following lines should be # delimited lines of piece name, position, color of the piece

e.g. pawn#b4#white - This means we have white pawn at b4
=======================================================================================
To run the test suite:

execute main.py as "python main.py"

Alternatively, you can also execute individual tests.

Output from main:
Pawn at <G:2> can move to <G:3>
Pawn at <G:2> can move to <G:4>
Knight at <B:1> can move to <C:3>
Knight at <B:1> can move to <A:3>
Pawn at <C:2> can move to <C:3>
Pawn at <C:2> can move to <C:4>
Pawn at <B:2> can move to <B:3>
Pawn at <B:2> can move to <B:4>
Knight at <G:1> can move to <H:3>
Knight at <G:1> can move to <F:3>
Pawn at <A:2> can move to <A:3>
Pawn at <A:2> can move to <A:4>
Pawn at <F:2> can move to <F:3>
Pawn at <F:2> can move to <F:4>
Pawn at <H:2> can move to <H:3>
Pawn at <H:2> can move to <H:4>
Pawn at <D:2> can move to <D:3>
Pawn at <D:2> can move to <D:4>
Pawn at <E:2> can move to <E:3>
Pawn at <E:2> can move to <E:4>
20 legal moves (10 unique pieces) for white player
.............................
----------------------------------------------------------------------
Ran 29 tests in 0.008s

OK

Process finished with exit code 0
======================================================================================
