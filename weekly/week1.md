e# Planning for Week 1

## High Level Topic Summary

> - Introduction and motivation
  - Review Lists and Dictionaries
  - File Systems to open/close/read/readline/split

## Readings for the week

Day        | Reading      | Reading Questions
:--------- |:-------------|:----------------------------------
Monday     | Preface, All of Chapter 1 |
Tuesday    | - |
Wednesday  | Chapter 2, section 1: paths and path facilities; section 2 high level operations; 2.3.1 on open/close/read/readline. |
Friday     | Chapter 2 remainder (from 2.3.2); Chapter 3, sections 1 and 2 on list patterns and dictionary review. | 2.54, 2.56, 2.65, 2.80, 3.4, 3.7, 3.35

## Projected Homework

HW | Day Out  | Day Due | Contents
:--|:--------|:--------|:------------
HW_0.1 | Monday | Wednesday | Short two notebook set
HW_1.1 | Tuesday | Friday | Python review plus simple file system from chapter 2
HW_1.2 | Friday | Monday | More file system; list patterns and dictionaries

## Tuesday Problem Day

Ensure computer setup and Git/GitHub setup to point of everyone being able to do git pull to get class resources.  Problems are the ones required for Friday (HW_1.1) on Python review and simple file system open/close/reading of files by line.


## Progression

Basic idea during class is an integration of lists and dictionaries as we look at facilities for interacting with the file system.  Wednesday start with file/path hierarchy and programmatic access in os/os.path calls from tables 2.3 and table 2.4.  Hands-on with opening and closing files and reading by line.  Refresh accumulation pattern and possibly other patterns.  On Friday, review and then get to multi-items per line, using lists and dictionaries and show more of the list patterns.

Goal of the week is review and setup for week2 on 2D representations of data and new topics of list comprehensions and lambda functions.

### Wednesday Details

- As refresher/leadin/chapter 1 "most important", use ContentFlow and dsprincipals figures to set context.
- Draw pic of file hierarchy and use hands-on with jupyter notebook to illustrate concepts and programmatic access with calls to `os` and `os.path` functions.  Interactive.  Use a *driver*.
- Define *paths* as traversal with Python realization as string
    - value add of `os.join()`
- File level operations and lines in a file and text files (foreshadowing on encoding)
- Something akin to `readNames()` in 2.3.1

## Prerequisite Concepts and References

DCS is **Discovering Computer Science** by Jessen Havill (i.e. your textbook from Intro CS).

- int, float, str data types: DCS 2.2
- integer specific operations `//` and `%`: DCS 2.2
- functional abstraction, namespaces, scope, return vs print: DCS 3.3, 3.5, 3.6
- docstrings: DCS 3.4
- scalar accumulation pattern: DCS 4.1
- string `.format()` method: DCS 4.1
- list accumulation pattern: DCS 4.2
- file system hierarchy: DCS 6.2
- text file open/close/read/readline: DCS 6.2
- string immutability: DCS 6.3
- list patterns: DCS 8.1, 8.2
- list mutability: DCS 8.2
- dictionaries: DCS 8.3
- multiple data items per line of file: DCS 8.4

For next week:

- list comprehensions: DCS 8.2
- tuples: DCS 8.2
- 2D representations: DCS: chapter 9
