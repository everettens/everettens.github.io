VIMTUTOR


Last login: Tue Mar 14 15:11:19 on ttys000
nathaneverette@Nathans-Air ~ % vimtutor


===============================================================================
=    W e l c o m e   t o   t h e   V I M   T u t o r    -    Version 1.7      =
===============================================================================

     Vim is a very powerful editor that has many commands, too many to
     explain in a tutor such as this.  This tutor is designed to describe
     enough of the commands that you will be able to easily use Vim as
     an all-purpose editor.

     The approximate time required to complete the tutor is 30 minutes,
     depending upon how much time is spent with experimentation.

     ATTENTION:
     The commands in the lessons will modify the text.  Make a copy of this
     file to practice on (if you started "vimtutor" this is already a copy).

     It is important to remember that this tutor is set up to teach by
     use.  That means that you need to execute the commands to learn them
     properly.  If you only read the text, you will forget the commands!

     Now, make sure that your Caps-Lock key is NOT depressed and press
     the   j   key enough times to move the cursor so that lesson 1.1
     completely fills the screen.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        Lesson 1.1:  MOVING THE CURSOR


   ** To move the cursor, press the h,j,k,l keys as indicated. **
             ^
             k              Hint:  The h key is at the left and moves left.
       < h       l >               The l key is at the right and moves right.
             j                     The j key looks like a down arrow.
             v
  1. Move the cursor around the screen until you are comfortable.

  2. Hold down the down key (j) until it repeats.
     Now you know how to move to the next lesson.

  3. Using the down key, move to lesson 1.2.

NOTE: If you are ever unsure about something you typed, press <ESC> to place
      you in Normal mode.  Then retype the command you wanted.

NOTE: The cursor keys should also work.  But using hjkl you will be able to
      move around much faster, once you get used to it.  Really!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Lesson 1.2: EXITING VIM


  !! NOTE: Before executing any of the steps below, read this entire lesson!!

  1. Press the <ESC> key (to make sure you are in Normal mode).

  2. Type:      :q! <ENTER>.
     This exits the editor, DISCARDING any changes you have made.

  3. Get back here by executing the command that got you into this tutor. That
     might be:  vimtutor <ENTER>

  4. If you have these steps memorized and are confident, execute steps
     1 through 3 to exit and re-enter the editor.

NOTE:  :q! <ENTER>  discards any changes you made.  In a few lessons you
       will learn how to save the changes to a file.

  5. Move the cursor down to lesson 1.3.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     Lesson 1.3: TEXT EDITING - DELETION


           ** Press  x  to delete the character under the cursor. **

  1. Move the cursor to the line below marked --->.

  2. To fix the errors, move the cursor until it is on top of the
     character to be deleted.

  3. Press the  x  key to delete the unwanted character.

  4. Repeat steps 2 through 4 until the sentence is correct.

---> The cow jumped over the moon.

  5. Now that the line is correct, go on to lesson 1.4.

NOTE: As you go through this tutor, do not try to memorize, learn by usage.



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                      Lesson 1.4: TEXT EDITING - INSERTION


                        ** Press  i  to insert text. **

  1. Move the cursor to the first line below marked --->.

  2. To make the first line the same as the second, move the cursor on top
     of the character BEFORE which the text is to be inserted.

  3. Press  i  and type in the necessary additions.

  4. As each error is fixed press <ESC> to return to Normal mode.
     Repeat steps 2 through 4 to correct the sentence.

---> There is text misng this .
---> There is some text missing from this line.

  5. When you are comfortable inserting text move to lesson 1.5.



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     Lesson 1.5: TEXT EDITING - APPENDING


                        ** Press  A  to append text. **

  1. Move the cursor to the first line below marked --->.
     It does not matter on what character the cursor is in that line.

  2. Press  A  and type in the necessary additions.

  3. As the text has been appended press <ESC> to return to Normal mode.

  4. Move the cursor to the second line marked ---> and repeat
     steps 2 and 3 to correct this sentence.

---> There is some text missing from th
     There is some text missing from this line.
---> There is also some text miss
     There is also some text missing here.

  5. When you are comfortable appending text move to lesson 1.6.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     Lesson 1.6: EDITING A FILE

                    ** Use  :wq  to save a file and exit. **

  !! NOTE: Before executing any of the steps below, read this entire lesson!!

  1.  If you have access to another terminal, do the following there.
      Otherwise, exit this tutor as you did in lesson 1.2:  :q!

  2. At the shell prompt type this command:  vim file.txt <ENTER>
     'vim' is the command to start the Vim editor, 'file.txt' is the name of
     the file you wish to edit.  Use the name of a file that you can change.

  3. Insert and delete text as you learned in the previous lessons.

  4. Save the file with changes and exit Vim with:  :wq <ENTER>

  5. If you have quit vimtutor in step 1 restart the vimtutor and move down to
     the following summary.

  6. After reading the above steps and understanding them: do it.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                               Lesson 1 SUMMARY


  1. The cursor is moved using either the arrow keys or the hjkl keys.
         h (left)       j (down)       k (up)       l (right)

  2. To start Vim from the shell prompt type:  vim FILENAME <ENTER>

  3. To exit Vim type:     <ESC>   :q!   <ENTER>  to trash all changes.
             OR type:      <ESC>   :wq   <ENTER>  to save the changes.

  4. To delete the character at the cursor type:  x

  5. To insert or append text type:
         i   type inserted text   <ESC>         insert before the cursor
         A   type appended text   <ESC>         append after the line

NOTE: Pressing <ESC> will place you in Normal mode or will cancel
      an unwanted and partially completed command.

Now continue with lesson 2.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        Lesson 2.1: DELETION COMMANDS


                       ** Type  dw  to delete a word. **

  1. Press  <ESC>  to make sure you are in Normal mode.

  2. Move the cursor to the line below marked --->.

  3. Move the cursor to the beginning of a word that needs to be deleted.

  4. Type   dw   to make the word disappear.

  NOTE: The letter  d  will appear on the last line of the screen as you type
        it.  Vim is waiting for you to type  w .  If you see another character
        than  d  you typed something wrong; press  <ESC>  and start over.

---> There are a some words fun that don't belong paper in this sentence.

  5. Repeat steps 3 and 4 until the sentence is correct and go to lesson 2.2.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                      Lesson 2.2: MORE DELETION COMMANDS


           ** Type  d$  to delete to the end of the line. **

  1. Press  <ESC>  to make sure you are in Normal mode.

  2. Move the cursor to the line below marked --->.

  3. Move the cursor to the end of the correct line (AFTER the first . ).

  4. Type    d$    to delete to the end of the line.

---> Somebody typed the end of this line twice. end of this line twice.


  5. Move on to lesson 2.3 to understand what is happening.





~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     Lesson 2.3: ON OPERATORS AND MOTIONS


  Many commands that change text are made from an operator and a motion.
  The format for a delete command with the  d  delete operator is as follows:

        d   motion

  Where:
    d      - is the delete operator.
    motion - is what the operator will operate on (listed below).

  A short list of motions:
    w - until the start of the next word, EXCLUDING its first character.
    e - to the end of the current word, INCLUDING the last character.
    $ - to the end of the line, INCLUDING the last character.

  Thus typing  de  will delete from the cursor to the end of the word.

NOTE:  Pressing just the motion while in Normal mode without an operator will
       move the cursor as specified.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     Lesson 2.4: USING A COUNT FOR A MOTION


   ** Typing a number before a motion repeats it that many times. **

  1. Move the cursor to the start of the line below marked --->.

  2. Type  2w  to move the cursor two words forward.

  3. Type  3e  to move the cursor to the end of the third word forward.

  4. Type  0  (zero) to move to the start of the line.

  5. Repeat steps 2 and 3 with different numbers.

---> This is just a line with words you can move around in.

  6. Move on to lesson 2.5.




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     Lesson 2.5: USING A COUNT TO DELETE MORE


   ** Typing a number with an operator repeats it that many times. **

  In the combination of the delete operator and a motion mentioned above you
  insert a count before the motion to delete more:
         d   number   motion

  1. Move the cursor to the first UPPER CASE word in the line marked --->.

  2. Type  d2w  to delete the two UPPER CASE words.

  3. Repeat steps 1 and 2 with a different count to delete the consecutive
     UPPER CASE words with one command.

--->  this ABC DE line FGHI JK LMN OP of words is Q RS TUV cleaned up.





~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Lesson 2.6: OPERATING ON LINES


                   ** Type  dd   to delete a whole line. **

  Due to the frequency of whole line deletion, the designers of Vi decided
  it would be easier to simply type two d's to delete a line.

  1. Move the cursor to the second line in the phrase below.
  2. Type  dd  to delete the line.
  3. Now move to the fourth line.
  4. Type   2dd   to delete two lines.

--->  1)  Roses are red,
--->  2)  Mud is fun,
--->  3)  Violets are blue,
--->  4)  I have a car,
--->  5)  Clocks tell time,
--->  6)  Sugar is sweet
--->  7)  And so are you.

Doubling to operate on a line also works for operators mentioned below.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Lesson 2.7: THE UNDO COMMAND


   ** Press  u  to undo the last commands,   U  to fix a whole line. **

  1. Move the cursor to the line below marked ---> and place it on the
     first error.
  2. Type  x  to delete the first unwanted character.
  3. Now type  u  to undo the last command executed.
  4. This time fix all the errors on the line using the  x  command.
  5. Now type a capital  U  to return the line to its original state.
  6. Now type  u  a few times to undo the  U  and preceding commands.
  7. Now type CTRL-R (keeping CTRL key pressed while hitting R) a few times
     to redo the commands (undo the undo's).

---> Fiix the errors oon thhis line and reeplace them witth undo.

  8. These are very useful commands.  Now move on to the lesson 2 Summary.




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                               Lesson 2 SUMMARY

  1. To delete from the cursor up to the next word type:        dw
  2. To delete from the cursor up to the end of the word type:  de
  3. To delete from the cursor to the end of a line type:       d$
  4. To delete a whole line type:                               dd

  5. To repeat a motion prepend it with a number:   2w
  6. The format for a change command is:
               operator   [number]   motion
     where:
       operator - is what to do, such as  d  for delete
       [number] - is an optional count to repeat the motion
       motion   - moves over the text to operate on, such as  w (word),
                  e (end of word),  $ (end of the line), etc.

  7. To move to the start of the line use a zero:  0

  8. To undo previous actions, type:           u  (lowercase u)
     To undo all the changes on a line, type:  U  (capital U)
     To undo the undo's, type:                 CTRL-R

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Lesson 3.1: THE PUT COMMAND


       ** Type  p  to put previously deleted text after the cursor. **

  1. Move the cursor to the first line below marked --->.

  2. Type  dd  to delete the line and store it in a Vim register.

  3. Move the cursor to the c) line, ABOVE where the deleted line should go.

  4. Type   p   to put the line below the cursor.

  5. Repeat steps 2 through 4 to put all the lines in correct order.

---> d) Can you learn too?
---> b) Violets are blue,
---> c) Intelligence is learned,
---> a) Roses are red,



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
