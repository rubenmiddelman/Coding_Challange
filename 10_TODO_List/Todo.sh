#!/bin/sh

# Author : Ruben Middelman
# Built a simple CLI TODO list in Bash

#check if the tasks file exists
Init_List () 
{
    if [ -e tasks.txt ]
    then
        echo "ready to start"
    else
        #if it doesn't exist create a new file to use
        echo "file doesn't exist"
        touch tasks.txt
        echo "New file created"
    fi 
}

#check if we want to add a task 
#problem: at this point we only add one word but most tasks consist of multiple words
Add_Task () 
{
        #check if priority is given
if [ $# -eq 4 ]
then
        #priority, adds line to specific line number
    echo "priority given at spot: $3"
    sed -i '' "$3s/$/\n$4/;" tasks.txt

else
        #no priority, adds task to bottom of the list
    echo "add task:, $2, to end of the list"
    echo $2 >> tasks.txt
fi
}

#clear of a task from the list
Clear_Task ()
{
    #deletes the given line number
    awk "NR != $1" tasks.txt > temp && mv temp tasks.txt
    echo "clear task $1"
}

#clear full list
Clear_List ()
{
        rm tasks.txt
        echo "list cleared"
}

Show_List ()
{
    cat tasks.txt
}


#initialize the list
Init_List 

#switch case to check what command is given
case $1 in
    -a)
    Add_Task $1 $2 $3 $4
    ;;
    -c)
    Clear_Task $2
    ;;
    -C)
    Clear_List
    ;;
    -s)
    Show_List
    ;;
esac
