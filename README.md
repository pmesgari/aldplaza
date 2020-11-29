# Python Algorithms and Data Structures

Aldplaza stands for Algorithms and Data Structures Plaza, a made up name for this repository, which is a collection of mathematical algorithms and data structures implemented in Python.

Each item in the repository is accompanied by the followings:

- The source code
- The test code
- The explanation

Hopefully this repository will be useful for anyone looking for material on learning algorithms and data structures.

## Algorithms

Algorithms are among the most fundamental concepts of mathematics and computer science. Algorithms are studied rigorously in mathematics and analyzing their performance is a core topic in computer science.

The very initial works on algorithms dates back to the early 9th Century **Persian mathematician called Muhammad Al-Khwarizmi**. Donald E.Knuth gives a brief history of the word algorithms. In his words:

> *The word “algorithm” itself is quite interesting; at first glance it may look  as though someone intended to write “logarithm” but jumbled up the first four  letters. It comes  from the name of a famous Persian textbook author, Abu ‘Abd Allah Muhammad  ibn Musa al-Khwarizmi (c. 825) — literally, “Father of Abdullah, Mohammed,  son of Moses, native of Khwarizm.” Donald E.Knuth The Art of Computer Programming Vol 1*

### Algorithms by Type

- Preliminaries
  - [Fibonacci](src/algorithms/fibonacci)

### Tips for Running Tests

#### Stress Tests

For some algorithms and data structures it is possible a stress test is included. The stress tests are basically a never ending `while` loop to be terminated by user. Thus, when trying to run the tests for the entire repository it is required to avoid tests marked as stress tests. This is possible by running the command below:

```bash
pytest -m "not stresstest"
```