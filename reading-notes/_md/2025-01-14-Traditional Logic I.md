---
aliases:
  - Traditional Logic I
title: Traditional Logic I
author: Martin Cothran
category: Mathematics
publisher: Memoria Press
total_page: 150
publish_date: 2000-01-01
isbn10: 1930953100
isbn13: 9781930953109
source: 
wishlist: 2024-07-06
acquired: 2024-07-02
started: 2024-07-14
finished: 2025-01-14
finishednotes: 2025-01-14
latex: true
mermaid: true
---
# *[Traditional Logic I](https://www.memoriapress.com/curriculum/logic-and-rhetoric/traditional-logic-i-complete-set-with-online-instruction/)* by [[Martin Cothran]]

<img src="https://www.memoriapress.com/wp-content/uploads/2012/01/Traditional-Logic1-CompleteSet-2.jpg" width=150>

`(Louisville: Memoria Press, 2000), 150`


>The kiln tests the potter's vessels; so the test of a man is in his reasoning. 
>-[[Sir-27#v5]]-6


>"Mom?"
>"Yes?"
>"What's lodge-ick?"
>"Logic? Why, dear, logic is knowing what things are true and not true."
>– [[Ray Bradbury]], *[[2024-08-16-The Illustrated Man|The Illustrated Man]]* ("Zero Hour", 260)

# Notes

<details>
 <summary><i>Contents</i></summary>
<!-- MarkdownTOC autolink="true" -->

- [Introduction: What is Logic?](#introduction-what-is-logic)
- [Simple Apprehension \(Term\)](#simple-apprehension-term)
- [Chapter 1: What Is Simple Apprehension?](#chapter-1-what-is-simple-apprehension)
- [Chapter 2: Comprehension and Extension](#chapter-2-comprehension-and-extension)
- [Chapter 3: Signification and Supposition](#chapter-3-signification-and-supposition)
- [Judgment \(Proposition\)](#judgment-proposition)
- [Chapter 4: What is Judgment?](#chapter-4-what-is-judgment)
- [Chapter 5: The Four Statements of Logic](#chapter-5-the-four-statements-of-logic)
- [Chapter 6: Contradictory and Contrary Statements](#chapter-6-contradictory-and-contrary-statements)
- [Chapter 7: Subcontraries and Subalterns](#chapter-7-subcontraries-and-subalterns)
- [Chapter 8: Distribution of Terms](#chapter-8-distribution-of-terms)
- [Chapter 9: Obversion, Conversion, and Contraposition](#chapter-9-obversion-conversion-and-contraposition)
- [Deductive Inference \(Syllogism\)](#deductive-inference-syllogism)
- [Chapter 10: What Is Deductive Inference?](#chapter-10-what-is-deductive-inference)
- [Chapter 11: Terminological Rules for Categorical Syllogisms](#chapter-11-terminological-rules-for-categorical-syllogisms)
- [Chapter 12: Quantitative Rules for Categorical Syllogisms](#chapter-12-quantitative-rules-for-categorical-syllogisms)
- [Chapter 13: Qualitative Rules for Categorical Syllogisms](#chapter-13-qualitative-rules-for-categorical-syllogisms)
- [Chapter 14: Review](#chapter-14-review)

<!-- /MarkdownTOC -->
</details>


## Introduction: What is Logic?

**Definitions**
- Josiah Royce: "The science of order." 
- Raymond McCall: "Logic in general is the science of right thinking."
- [[Jacques Maritain]]: "Logic is the art which enables us to proceed with order, ease, and correctness in the act of reason itself." 
- Irving Copi: "The distinction between correct and incorrect reasoning is the central problem with which logic deals." 

**History of Logic**
- [[Aristotle]] (384-322 BC) is the "father of logic"
- Chrysippus (279-206 BC) laid the foundation for symbolic logic, which was picked up by Leibniz (1646-1716)
- [[John Stuart Mill]] (1806-1873) pioneered *induction*

**Two Branches of Logic**
- **Formal (*minor*) Logic***: concerned with the *form* or structure of reasoning, or the method of deriving one truth from another 
- **Material (*major*) Logic**: concerned with the *content* of argumentation and the *truth* of the terms

> You can only find truth with logic if you have already found truth without it.
> –[[G.K. Chesterton]]

**Truth, Validity, Soundness**
- A statement is either _**true**_ or _**false**_. A true statement corresponds to reality. 
- The structure of an argument is _**valid**_ if its conclusion follows logically from its premises, otherwise it is _**invalid**_.
- An argument as a whole is **_sound_** if all premises are true and the argument is valid.

**Components of an Argument**
- **Term**: the verbal expression of the mental act of **_simple apprehension_**
- **Proposition**: the verbal expression of the mental act of **_judgment_**, whereby we **affirm** that something *is* something, or **deny** that something *is not* something
- **Syllogism**: the verbal expression of the mental act of **_deductive inference_**, whereby we make the logical connections between the terms in the argument in a way that shows us that the conclusion either follows or does not follow from the premises 

| Mental Act          | Verbal Expression |
| ------------------- | ----------------- |
| Simple Apprehension | Term              |
| Judgment            | Proposition       |
| Deductive Inference | Syllogism.        |


# Simple Apprehension (Term)
## Chapter 1: What Is Simple Apprehension?
- **Sense Perception**: the act whereby your senses present an object to your mind; you perceive an object by means of your senses 
- **Mental Image**: the image of an object formed in the mind as a result of a sense perception of that object 
- **Simple Apprehension**: is an act by which the mind grasps the general concept of an object without affirming or denying anything about it.
	- Simple apprehension allows us to grasp the *essence* of a thing.
- **Abstraction**: is the process by which a simple apprehension is derived from a sense perception and mental image.
- *Sense perception* → *Mental image* → *Simple apprehension*


## Chapter 2: Comprehension and Extension
- The two properties of simple apprehension (concepts) are **_comprehension_** and **_extension_**
- **Comprehension** is the completely articulated sum of the intelligible aspects or elements (or notes) represented by a concept.
	- A comprehension answers the question, *"What is a `<blank>`?"*
	- A **Note** is the simple (atomic) concept that cannot be broken into simpler parts 
	- The **Porphyrian Tree** (invented by third-century logician Porphyry) allows us to identify the notes associated with a concept

```mermaid
graph TD

a(<strong>Category:</strong> Substance)
b(Material)
c(Non-Material)
d(<strong>Remote Genus:</strong> Body)
e(Living)
f(Non-Living)
g(<strong>Remote Genus:</strong> Organsm)
h(Sentient)
i(Nonsentient)
j(<strong>Proximate Genus:</strong> Animal)
k(Rational)
l(Nonrational)
m(<strong>Logical Species:</strong> Man)

classDef r fill:#f96

a:::r --> b
a --> c
b --> d:::r 
d --> e
d --> f
e --> g:::r 
g --> h
g --> i
h --> j:::r 
j --> k
j --> l
k --> m
```

- **Extension** tells us to which things an essence applies.
	- An extensions answers the question, *"To what does the concept `<blank>` refer?*
- The greater number of notes a concept has, the less extension it has (something more specific is less applicable). 



## Chapter 3: Signification and Supposition
- A **Term** is the verbal expression of a concept.
- The two properties of terms are **_signification_** and **_supposition_**.
- **Signification** is a way of dividing terms:
	- **Univocal terms** are terms that have exactly the same meaning no matter when or how they are used. 
	- **Equivocal terms** have different and unrelated meanings.
	- **Analogous terms** are applied to different things but have related meanings. 
	- *→Logic requires an accurate and consistent use of terms (which is an issue with equivocal and analogous terms).*
- **Supposition** is a way of dividing terms:
	- **Material supposition** is when a term refers to something as it exists *verbally*
	- **Logical supposition** is when a term refers to something as it exists *logically* or *mentally*
	- **Real supposition** is when a term refers to something as it exists in the real world


# Judgment (Proposition)
## Chapter 4: What is Judgment?
- **Judgment** is the act by which the intellect unites the *subject* and *predicate* by affirming, or separates them by denying. 
	- **Judgment** is a mental act whose verbal expression is a **proposition**.
- A **Proposition** is a statement which expresses truth or falsity. A proposition consists of three elements: the **subject-term** (**S**), the **predicate-term** (**P**), and the **copula** (**c**, usually "is" or "are"), which must be arranged in **logical form**. 
	- $\text{(Man)}^S \text{ (is)}^c \text{ (an animal)}^P$
	- "The little brown-haired boy screams very loudly" becomes: $\text{(The little brown-haired boy)}^S \text{ (is)}^c \text{ (a child who screams very loudly)}^P$

## Chapter 5: The Four Statements of Logic
- The **Four Statements of Logic**
	- **A**: All S is P (*affirmo*)
	- **I**: Some S is P
	- **E**: No S is P (*nego*)
	- **O**: Some S is not P
- **Quantifiers** include: all, some, no, some...not 
- The **Quality** of a proposition is **affirmative** or **negative**
- The **Quantity** of a proposition has to do with whether it is **universal** or **particular** (or **singular**, treated as universal). Statements are assumed to be universal unless stated otherwise.
	- **A**: Affirmative-Universal
	- **I**: Affirmative-Particular
	- **E**: Negative-Universal
	- **O**: Negative-Particular

| ↓Quantity/Quality→ | Affirmative     | Negative          |
| ------------------ | --------------- | ----------------- |
| **Universal**      | A (All S is P)  | E (No S is P)     |
| **Particular**     | I (Some S is P) | O (Some S is not P) |

## Chapter 6-7: Contradictory, Contrary, Subcontrary, and Subalternate Statements 
- Categorical statements can be related in **Opposition** or in **Equivalence**
- **Opposition**: statements in opposition *affirm* and *deny* the same predicate of the same subject 
	- Contradictory 
	- Contrary 
	- Subcontrary 
	- Subaltern 
- **Equivalence**
	- Obversion 
	- Conversion 
	- Contraposition 

- **Rule of Contradiction**: Contradictory statements are statements that differ in both quality and quantity. Same colors (opposites) are contradictory:

| ↓Quantity/Quality→ | Affirmative                                    | Negative                                          |
| ------------------ | ---------------------------------------------- | ------------------------------------------------- |
| **Universal**      | <i style="color: #BD483E; ">A (All S is P)</i> | <i style="color: #46348B;">E (No S is P)</i>      |
| **Particular**     | <i style="color: #46348B;">I (Some S is P)</i> | <i style="color: #BD483E; ">O (Some S is not P)</i> |

 - **The Rule of Contraries**: Two statements are contrary to one another if they are both universals but differ in quality. <i style="color: #BD483E; ">A (red)</i> and <i style="color: #46348B; ">E (purple)</i> are contrary:

| ↓Quantity/Quality→ | Affirmative                                    | Negative                                     |
| ------------------ | ---------------------------------------------- | -------------------------------------------- |
| **Universal**      | <i style="color: #BD483E; ">A (All S is P)</i> | <i style="color: #46348B;">E (No S is P)</i> |
| **Particular**     | I (Some S is P)                                | O (Some S is not P)                          |

 - **The Rule of Subcontraries**: Two statements are contrary to one another if they are both particular statements that differ in quality. <i style="color: #BD483E; ">I (red)</i> and <i style="color: #46348B; ">O (purple)</i> are contrary:

| ↓Quantity/Quality→ | Affirmative                                     | Negative                                           |
| ------------------ | ----------------------------------------------- | -------------------------------------------------- |
| **Universal**      | A (All S is P)                                  | E (No S is P)                                      |
| **Particular**     | <i style="color: #BD483E; ">I (Some S is P)</i> | <i style="color: #46348B;">O (Some S is not P)</i> |

- **The Rule of Subalternates**: Two statements are subalternate if they have the same quality, but differ in quantity. <i style="color: #BD483E; ">A (red)</i> and <i style="color: #BD483E; ">I (red)</i> are subalternate, and <i style="color: #46348B; ">E (purple)</i> and <i style="color: #46348B; ">O (purple)</i> are subalternate:

| ↓Quantity/Quality→ | Affirmative                                     | Negative                                           |
| ------------------ | ----------------------------------------------- | -------------------------------------------------- |
| **Universal**      | <i style="color: #BD483E; ">A (All S is P)</i>  | <i style="color: #46348B;">E (No S is P)</i>       |
| **Particular**     | <i style="color: #BD483E; ">I (Some S is P)</i> | <i style="color: #46348B;">O (Some S is not P)</i> |


 - **First Law of Opposition**: Contradictories cannot at the same time be true nor at the same time be false.
 - **The Second Law of Opposition**: Contraries cannot at the same time both be true, but can at the same time both be false.
- **The Third Law of Opposition**: Subcontraries may at the same time both be true, but cannot at the same time both be false.
- **The Fourth Law of Opposition**: Subalterns may both be true or both be false. If the particular is false, the universal is false; if the universal is true, the  particular is true; otherwise their status is indeterminate.

- [Logical Opposition Chart - Google Slides](https://docs.google.com/presentation/d/1Eka2n5Fr3uJ2pvKyWzkEycFbdXEr1A6ZcxSyhej8rWM/edit#slide=id.p)

## Chapter 8: Distribution of Terms
- **Distribution** is the status of a term in regard to its extension.
	- A term is ***distributed*** if it refers to all the members of the class of things denoted by the term; a *distributed* term is *universal*.
	- A term is ***undistributed*** if it refers to only some members of the class denoted by the term.
- The **subject-term** is distributed in statements whose quantity is universal and undistributed in statements whose quantity is particular. 
 
| ↓Quantity/Quality→ | Affirmative                                    | Negative                                     |
| ------------------ | ---------------------------------------------- | -------------------------------------------- |
| **Universal**      | <i style="color: #BD483E; ">A (All S is P): Subject distributed</i> | <i style="color: #BD483E;">E (No S is P): Subject distributed</i> |
| **Particular**     | <i style="color: #46348B;">I (Some S is P): Subject undistributed</i> | <i style="color: #46348B;">O (Some S is not P): Subject undistributed</i>|



- The **predicate-term** is always undistributed for affirmative propositions and distributed for negative propositions.

| ↓Quantity/Quality→ | Affirmative                                    | Negative                                     |
| ------------------ | ---------------------------------------------- | -------------------------------------------- |
| **Universal**      | <i style="color: #46348B; ">A (All S is P): Predicate undistributed</i> | <i style="color: #BD483E;">E (No S is P): Predicate distributed</i> |
| **Particular**     | <i style="color: #46348B;">I (Some S is P): Predicate undistributed</i> | <i style="color: #BD483E;">O (Some S is not P): Predicate distributed</i>|

## Chapter 9: Obversion, Conversion, and Contraposition
- Two statements are logically the same if they are **logically equivalent**.
- Statements can be made equivalent through Obversion, Conversion, or Contraposition.
- **Obversion**: 1) Change the quality of the sentence, 2) Negate the predicate 
	- **A**: All S is P → No S is not P
	- **E**: No S is P → All S is not P
	- **I**: Some S is P → All S is not non-P
	- **O**: Some S is not P → Some S is not P
- **Conversion**: interchange the subject and predicate 
	- **E**: No S is P → No P is S
	- **I**: Some S is P → Some P is S
	- Partial conversion of the A statement is done by interchanging the subject and predicate and changing the statement from universal to particular: All S are P → Some P are S
	- *Conversion does not work with O statements and other A statements.*
- **Contraposition**: 1) Obvert the statement, 2) Convert the statement, 3) Obvert the statement again 
	- **A**: All S is P → All non-P is non-S
	- **O**: Some S is not P → Some non-P is S
	- Only works with A and O statements.
	- E statement can be partially converted.


# Deductive Inference (Syllogism)
## Chapter 10: What Is Deductive Inference?
- **Reasoning** is the act by which the mind acquires new knowledge by means of what it already knows. 
- **Deductive inference** is a form of reasoning by which the mind establishes a connection between the antecedent and the consequent. 
- A **Syllogism** is a group of propositions in orderly sequence, one of which (the consequent) is said to be necessarily inferred from the others (the antecedent).
	- A syllogism will always contain two premises and a conclusion.
- **The Essential Law of Argumentation**: If the antecedent is true, the consequent must also be true.
	- Corollary 1: If the syllogism is valid and the consequent is false, then the antecedent must be false.
	- Corollary 2: In a valid syllogism with a true consequent, the antecedent is not necessarily true.
- Terms in a Syllogism:
	- **Major Term**: predicate of the conclusion
	- **Minor Term**: subject of the conclusion
	- **Middle Term**: term that appears in both premises but not the conclusion 
- Premises in a Syllogism:
	- **Major Premise**: premise which contains the major term
	- **Minor Premise**: premise which contains the minor term
- Principles of Syllogism:
	- **The Principle of Reciprocal Identity**: Two terms that are identical with a third term are identical to each other.
	- **The Principle of Reciprocal Non-Identity**: Two terms, one of which is identical with a third term and the other of which is nonidentical with that term, are nonidentical to each other.
	- **The Dictum de Omni**: What is affirmed universally of a certain term is affirmed of every term that comes under that term.
	- **The Dictum de Nullo**: What is denied universally of a certain term is denied of every term that comes under that term.


## Chapter 11-13: Rules for Categorical Syllogisms
- **Terminological Rules**
	- There must be three and only three terms. (*Violated if there are four unconnected terms, or by the Fallacy of Equivocation where a term is used in different senses.*)
	- The middle term must not occur in the conclusion.
- **Quantitative Rules**
	- If a term is distributed in the conclusion, then it must be distributed in the premises. (*Violated by the Fallacy of Illicit Process*.)
	- The middle term must be distributed at least once. (*Violated by the Fallacy of the Undistributed Middle*.)
- **Qualitative Rules**
	- No conclusion can follow from two negative premises. (*Violated by the Fallacy of Exclusive Premises*.)
	- If the two premises are affirmative, the conclusion must also be affirmative. (*Violated by the Fallacy of Drawing a Negative Conclusion from Affirmative Premises.*)
	- If either premise is negative, the conclusion must be negative. (*Violated by the Fallacy of Drawing an Affirmative Conclusion from a Negative Premise.*) 


## Chapter 14: Review



--- 
**Topic**: [[Logic]]

**Source**
- [[Aquinas Columbus]]

---
Created: [[2024-07-06-Sat]]
Updated: `=dateformat(this.file.mtime, "yyyy-MM-dd-ccc")`