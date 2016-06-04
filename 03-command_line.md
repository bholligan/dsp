# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > **mkdir**: Make a directory  
> > **ls**: Show the folders inside a directory.  
> > **cd**: Change directory. Use '..' to move up a level.  
> > **cp**: Copy a file. Can use 'cp -r filename directoryname' to copy a file to a new directory  
> > **wildcard**: Use an asterix to stand in for all possible values.  
> > **find**: Finds files that match certain criteria. For example, to print text files in current directory use 'find . -name ".txt" -print'  
> > **grep**: Searches within files to find matches. Done with 'grep searchstring filename'. The filename can be a wildcard to search multiple files. Lot of customization here, like using -i to make the search not case-sensitive.  
> > **man**: Pulls up the help documentation for a given command.  
> > **more/less**: Quick and easy ways to display a file on screen. There are options to customize the display.  
> > **vim**: Launches the vim text editor. Type 'vimtutor' to launch the built-in tutorial.  
> > **tail**: Will display the last ten lines of a given file.

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls` Displays the files in the directory    
`ls -a` Displays all files, including hidden ones.
`ls -l`  Displays files in the long format, which shows permissions, ownership, size, mod date, and more.  
`ls -lh`  Displays files in human readable format.  
`ls -lah`  Displays all files in human readable format, including hidden files.  
`ls -t`  Displays files in order based on date modified, with the most recent ones first.  
`ls -Glp`  Displays files and highlights the directories with a "/" on the end of them.  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -r`  Displays files in the reverse order.  
`ls -1`  Displays each entry on a new line.  
`ls -R`  Displays subdirectories as well.  
`ls -o`  Displays files similar to 'ls -l', but it excludes the group name.  
`ls -d`  Displays only directories.  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs lets you perform commands on the output of other commands. It reads the input as delimited by blanks or newlines. The default output command is echo. One cool use is to combine it with find and grep to filter files that contain a particular keyword. For example:  
> > `find . -name '*.py' | xargs grep 'searchterm'`  
> > This bit of code will look in every .py file in the current directory and show you where the uses of your search term occur.  


Adding this line through a text editor and uploading via terminal as practice.

