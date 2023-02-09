# PietFuck
A "programming language" inspired by Piet and Brainfuck

This uses the 8 commands of Brainfuck but uses images to program like in Piet, and reads the image left-right top-bottom

This is a pain to write programs in lol

Syntax:


| Colour     | Command       | Brainfuck | 
|------------|---------------|-----------|
| Green      | ADD           | +         | 
| Red        | SUB		         | -         | 
| Black      | OUT	          | .         | 
| Purple     | IN			         | ,         | 
| Light blue | LOOP START	   | [         | 
| Dark blue  | LOOP END	     | ]         | 
| Yellow	    | POINTER PLUS  | \>        | 
| Orange	    | POINTER MINUS | \<        |

## Usage
To use this, simply run `main.py yourprogram.png`

### Custom palettes
If you want to use a custom palette, run `main.py yourprogram.png yourpalette.png`

Palettes are simply an image consisting of the 8 colours you want to use in your program. The program reads palettes in
the same way it reads regular programs (left-right top-bottom), and reads the first 8 colours. It then assigns them to
instructions in the order shown in the table above. The image in the examples folder shows the palette that the program
would use by default.