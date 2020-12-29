# Planning for Week 2

## High Level Topic Summary

> - Two-D Representations
  - New Python Features
      - List comprehensions
      - Functions as objects

## Readings for the week

Day        | Reading      | Reading Questions
:--------- |:-------------|:----------------------------------
Monday     | Chapter 3; reinforce 3.1, 3.2, 3.4.1, 3.4.2 | 3.102, 3.104
Tuesday    | - |
Wednesday  | Chapter 3, 3.4.3, 3.3 |
Friday     | Chapter 3.3.1, 3.3.2, Chapter 5 if time | 3.59, 3.62

## Projected Homework

HW | Day Out  | Day Due | Contents
:--|:--------|:--------|:------------
HW_1.3 | Monday | Wednesday | Building native 2D representations
HW_1.4 | Wednesday | Friday | List comprehensions and lambda functions
HW_1.5 | Friday | Monday |

## Tuesday Problem Day

List patterns and integration with LoL and DoL.


## Progression

Goal of the week is finish review topics and native Python representations so that we are in a place at the end of the week to read chapter 5 and set up and motivate the tabular data model.

Monday: Make sure we are all on the same page with respect to Python and file processing, lists and dictionaries.  

Wednesday: Complete representations with the List of Dictionaries with new material on list comprehensions and vector operations and lambda functions.

Friday: First half: complete Python features; second half: transition into data models and Part II of the textbook.

- [Function as object](http://www.pythontutor.com/visualize.html#code=import%20random%0A%0Adef%20add1%28n%29%3A%0A%20%20%20%20return%20n%2B1%0A%0AL1%20%3D%20%5B%20random.randint%281,30%29%20for%20i%20in%20range%285%29%20%5D%0A%0AL2%20%3D%20%5B%5D%0Afor%20val%20in%20L1%3A%0A%20%20%20%20newval%20%3D%20add1%28val%29%0A%20%20%20%20L2.append%28newval%29%0A%0Aprint%28L1%29%0Aprint%28L2%29%0A%0Adef%20apply_func%28func,%20data%29%3A%0A%20%20%20%20result%20%3D%20%5B%5D%0A%20%20%20%20for%20val%20in%20data%3A%0A%20%20%20%20%20%20%20%20newval%20%3D%20func%28val%29%0A%20%20%20%20%20%20%20%20result.append%28newval%29%0A%20%20%20%20return%20result%0A%0AL2%20%3D%20apply_func%28add1,%20L1%29%0A%0Aprint%28L2%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Prerequisite Concepts and References

DCS is **Discovering Computer Science** by Jessen Havill (i.e. your textbook from Intro CS).

- list comprehensions: DCS 8.2
- tuples: DCS 8.2
- 2D representations: DCS: chapter 9
