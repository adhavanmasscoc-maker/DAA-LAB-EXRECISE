# DAA-LAB-EXRECISE

Python implementations for Design and Analysis of Algorithms Laboratory.

## Repository

This repository contains Experiment 01 and its additional exercise programs based on Interpolation Search.

---

# Experiment 01

## Implementation and Performance Analysis of Interpolation Search

### Problem Statement

Given a sorted array of uniformly distributed integers, implement Interpolation Search to find the position of a target element. Compare its performance with Binary Search for different dataset sizes.

### Aim

To implement the Interpolation Search algorithm in Python and analyze its performance by comparing it with Binary Search.

---

# Program 1

## Main Experiment

### Description

Implementation of Interpolation Search and Binary Search with performance analysis on datasets of varying sizes.

### Features

* Interpolation Search
* Binary Search
* Execution time comparison
* Comparison count analysis
* Dataset sizes:

  * 1000
  * 5000
  * 10000
  * 50000
  * 100000

### Complexity

| Algorithm            | Average Case | Worst Case |
| -------------------- | ------------ | ---------- |
| Interpolation Search | O(log log n) | O(n)       |
| Binary Search        | O(log n)     | O(log n)   |

### File

```text
DAA-LAB-01.ipynb
```

---

# Program 2

## Exercise Question 1

### Problem Statement

Implement Interpolation Search on a sorted array of student roll numbers (range 1 to 10000) and count the number of probes required to find a given roll number. Compare the results with Binary Search.

### Features

* Student roll numbers dataset
* Probe counting
* Binary Search comparison
* Search efficiency analysis

### Expected Outcome

Interpolation Search requires fewer probes than Binary Search when the data is uniformly distributed.

### Complexity

| Algorithm            | Average Case |
| -------------------- | ------------ |
| Interpolation Search | O(log log n) |
| Binary Search        | O(log n)     |

### File

```text
exercise_01_roll_numbers.py
```

---

# Program 3

## Exercise Question 2

### Problem Statement

Modify Interpolation Search to work on a sorted array of floating-point numbers uniformly distributed between 0.0 and 1000.0 and analyze the number of comparisons needed for dataset sizes:

* 10000
* 50000
* 100000

### Features

* Floating-point datasets
* Comparison counting
* Large-scale analysis
* Uniform distribution testing

### Expected Outcome

Interpolation Search performs efficiently on uniformly distributed floating-point data and requires very few comparisons even for large datasets.

### Complexity

| Case         | Complexity   |
| ------------ | ------------ |
| Best Case    | O(1)         |
| Average Case | O(log log n) |
| Worst Case   | O(n)         |

### File

```text
exercise_02_float_search.py
```

---

# Learning Outcomes

* Understood the working of Interpolation Search.
* Compared Interpolation Search with Binary Search.
* Measured probes and comparisons.
* Analyzed algorithm efficiency.
* Worked with integer and floating-point datasets.
* Studied practical performance analysis.

---

# Technologies Used

* Python 3
* Google Colab
* GitHub

---

# Repository Structure

```text
DAA-LAB-EXRECISE/
│
├── DAA-LAB-01.ipynb
├── exercise_01_roll_numbers.py
├── exercise_02_float_search.py
└── README.md
```

---

# Author

Aadhavan K

Department of Computer Science and Engineering

Design and Analysis of Algorithms Laboratory
