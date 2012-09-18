## Description ##

This is a plugin for Sublime Text that inserts an incrementing counter at the cursor positions.

## Usage ##

Executing the Counter command will open the input panel to allow the user to specify additional options or overrides with the following syntax:

    [start][+-increment][:padding]

By default, the Counter command will insert numbers starting at 1 and incrementing by 1.

The following examples demonstrate the available options and their output.

    2 → 2, 3, 4, ...

    1+3 → 1, 4, 7, ...

    10-1 → 10, 9, 8, ...

    2:3 → 002, 003, 004, ...

    100-2:4 → 0100, 0098, 0097, ...

## Example ##

Given the following text, the carets represent cursor selection regions - the first and third lines have cursor positions at the start and end of the line respectively, and the second line has the word 'the' selected.

    <>The hamster
    ate <the>
    tasty pigeon.<>

If the user executes the Counter command with the options 10+2:3, the resulting text will be:

    010The hamster
    ate 012
    tasty pigeon.014
