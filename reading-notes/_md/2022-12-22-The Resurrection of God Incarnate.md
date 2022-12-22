---
aliases: [The Resurrection of God Incarnate]
title: The Resurrection of God Incarnate
author: Richard Swinburne
category: Language Arts & Disciplines
publisher: Oxford University Press
total_page: 233
cover_url: http://books.google.com/books/content?id=J1UTDAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api
publish_date: 2003-01-09
isbn10: 0199257450
isbn13: 9780199257454
latex: true
---
# *[The Resurrection of God Incarnate]()* by [[Richard Swinburne]]

<img src="http://books.google.com/books/content?id=J1UTDAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api" width=150>

`(New York: Oxford University Press, 2003), 233`

I heard about this book in an interview with [[Cameron Bertuzzi]] describing his conversion to Catholicism ([link](https://youtu.be/bilP-Rh6jYk?t=4707)). In the book, Swinburne evaluates the evidence for the resurrection of Jesus and uses a Bayesian framework to evaluate the probability of the event happening as described. Bertuzzi used a similar approach to evaluate the Catholic dogma of the Papacy, which was his main objection with Catholicism, and he described a spreadsheet he developed to collect evidence and evaluate the probability of the historical accuracy of the Papal claims[^sheet]. 

Bertuzzi described Bayesian analysis is a more formal way of performing the types of probabilistic calculations we do everyday in our heads. I don't need to be convinced of the resurrection of Christ, but I was very interested to study the Bayesian framework Swinburne presents in the appendix and think about how that can be applied to other questions of probability. I made [this calculator](https://docs.google.com/spreadsheets/d/1XUVuNvtOvYuyIabsy6N37x4xjCJWi_Jxnw1sG7zRCsw/edit#gid=0) to implement Swinburne's Bayesian analysis and sensitize some of his inputs. 

[^sheet]: He discusses his exploration of the Papacy from about 16:40 to 37:22, and describes the spreadsheet for performing his Bayesian analysis at [18:56](https://youtu.be/bilP-Rh6jYk?t=1136). A main aspect of this argument was evaluating the The New Eliakim Typological Argument for the Papacy.


# Notes 

## Preface
- "In this book I seek to provide that evidence, in particular evidence for the Resurrection which—if it occurred—would be the divine signature on the teaching of Jesus and the teaching of the Church which he founded." (v) 

## Introduction
- Natural theology: "that there is a universe, that it conforms almost invariably to simple natural laws, that these laws and the initial state of the universe are such as to lead to the evolution of human bodies, that these are connected to souls, that humans have great opportunities for helping each other, and that there is widespread religious experience" (2)

# Part I: General Background Evidence 
_**Summary**: In so far as there is evidence of natural theology favoring that claim that there is a God, we don't need too much detailed historical evidence to show that the Resurrection occurred. We only need to show that Jesus is a serious candidate on normal historical grounds both for having lived the right kind of life and for being raised from the dead: that there is this unique coincidence of significant historical evidence in Jesus._

## Chapter 1: Principles for Weighing Evidence
_**Summary**: When we have an event of possible cosmic significance, we need to take into account general background evidence as well as detailed historical evidence. Also, in the absence of counter-evidence, we must assume that what looks like testimony to a historical event really is so._

## Chapter 2: God's Reasons for Incarnation 
_**Summary**: Considers reasons which God might have for becoming incarnate (acquiring a human body and nature)._

## Chapter 3: The Marks of an Incarnate God
_**Summary**: If God did become incarnate, he would need to "put his signature" on it with a super-miracle like the resurrection. It would be deceptive of God to raise someone from the dead other than God incarnate. There is no one in history apart from Jesus who lived his life in this manner._

# Part II: Prior Historical Evidence 
_**Summary**: The historical evidence is such that it is not too improbable that you would find it if Jesus did lead the relevant sort of life, and hence there is a significant prior probability that God would raise him from the dead._

## Chapter 4: The Historical Sources 

## Chapter 5: The Life and Moral Teaching of Jesus 

## Chapter 6: Jesus Implied his Divinity 

## Chapter 7: Jesus Taught his Atonement 

## Chapter 8: Jesus Founded a Church


# Part III: Posterior Historical Evidence 
_**Summary**: Considers the posterior evidence of what witnesses reported after the death of Jesus. Conclusion: given that general background evidence makes it as least as likely as not that there is a God, when we add the detailed historical evidence, the total evidence makes it probable that there is indeed a God who became incarnate in Jesus Christ and rose from the dead on the first Easter morning._

## Chapter 9: The Appearances of the Risen Jesus 

## Chapter 10: The Empty Tomb and the Observance of Sunday

## Chapter 11: Rival Theories of what Happened 

## Chapter 12: The Significance of the Resurrection


# Part IV: Conclusion

## Chapter 13: The Balance of Probability 
- Evidence-based support for the resurrection of Jesus requires a belief in the kind of the God who would intervene in human history (203)
- "If the background evidence leaves it not too improbable that there is a God likely to act in the ways discussed, then the total evidence makes it very probable that Jesus was God Incarnate who rose from the dead." (203)

## Appendix: Formalizing the Argument

**Logical [[Probability]]**
- Formalize his argument numerically using the axiomatic form by Kolmogorov (204)
- Three types of probability: 
	- **Physical Probability**: possible future event based on past events (relative to time)
	- **Statistical Probability**: proportion in an actual or hypothetical class 
	- we care about: Inductive or Epistemic or **Logical Probability**: the measure of the extent to which one proposition makes another likely to be true 
- **Notation**
	- $P(p|q)$: probability of $p$, given $q$
	- $N$: of logical necessity
	- $\lor$: or
	- $\iff$: if and only if
	- $N(p \iff q)$: $p$ and $q$ are logically equivalent
- Axioms (205-206):
	1.  $P(q|r) \ge 0$
		- *The probability of any proposition given any other proposition cannot be less than zero*
	2. If $N(r \rightarrow q), P(q|r) = 1$
		- *If $r$ entails $q$, then given $r$, $q$ is certainly true*
	3. If $N \sim (p \space \& \space q \space \& \space r)$ and $\sim N(\sim r)$ , $P(p \lor q | r) = P(p|r) + P(q|r)$
		- *The probability that $p$ or $q$ (or both) is true, given $r$ is the sum of {the probability that $p$ is true given $r$} plus {the probability that $q$ is true given $r$}, if $r$ is a logical possibility and if, given $r$, $p$ and $q$ cannot both be true*
	4. $P(p \space \& \space q | r) = P(p|q \space \& \space r) P(q|r)$
		- *The probability that both $p$ and $q$ are true, given $r$, is the probability that one of them ($q$) is true given $r$, multiplied by the probability that, given $r$ and also $q$, the other will be true*
	5. If $N(p \iff q)$, $P(r|p) = P(r|q)$
		- *If $p$ and $q$ are logically equivalent, the probability of some proposition given the one is the same as the probability of that proposition given the other*
- [[Bayes's Theorem]] (206)
	- $e$: observed evidence, data 
	- $k$: background evidence 
	- $h$: hypothesis under investigation
	- $P(h|e \space \& \space k) = \frac{P(e|h \space \& \space k) P(h|k)}{P(e|k)}$
	- Ignore the background evidence ($k$) in questions of metaphysics (it is mere tautology or repetition)
	- $P(h|e \space \& \space k)$ is the **posterior probability**, which is high if:
		- $P(e|h \space \& \space k)$ (the posterior probability of $e$) is high
			- Extent to which you expect to find $e$ if $h$ is true
		- $P(h|k)$ (the prior probability of $h$) is high, and 
		- $P(e|k)$ (the prior probability of $e$) is low (i.e., for tautological $k$, is a measure of how likely $e$ is to occur if we do not assume any particular theory to be true)
- "Scientific examples show us that simplicity is more important than scope for determining prior probability" (207) 

**The Logical Probability of Theism**
- For $h$ there is a God, he has argued elsewhere that $P(e|h \space \& \space k)$ is as probable as not (if there is a God with infinite power and knowledge and freedom you would expect to find the things we do in $e$), and $P(e|k)$ is comparatively low (you would not expect to find these things without a God)

**The Formal structure of the Argument of this Book**
- Definitions for this book:
	- $k$: the evidence of natural theology (beyond mere tautology)
	- $e$: the detailed historical evidence 
	- $h$: the conjunction $(h_1 \space \& \space h_2)$
	- $h_1$: the hypothesis that God became incarnate in Jesus 
	- $h_2$: the hypothesis that Jesus rose from the dead 
	- $c$: the claim that God became incarnate 
	- $f$: probability of the evidence given $c$ (?)
- 211: This book is interested in: $\boxed{P(h|e \space \& \space k)}$
	- **The probability that Jesus was God Incarnate who rose from the dead ($h$), on the evidence both of natural theology ($k$) and of the detailed history of Jesus and of other human prophets ($e$).**
	- He gets to a very high probability for this: `0.97` (214)
- $P(c|k)$: probability on the evidence of natural theology that there is a God who becomes incarnate 
	- $P(c|k)=P(c|t \space \& \space k) \space P(t|k) = 1/2 \times 1/2 = 1/4$
	- $P(t|k)$ is the probability that there is a traditional God on the evidence of natural theology
- $P(f|c \space \& \space k)$: probability that if God became incarnate we would have evidence of the strength described? he assigns this a low probability of $1/10$ 
- $P(f \space \& \space c|k) = P(f|c \space \& \space k) \space P(c|k) = 1/10 \times 1/4 = 1/40$
- $P(f|k)$: the probability of evidence $f$ given $k$
	- this is {the probability, given $k$, that there is a God who becomes incarnate and leave evidence of kind $f$} plus {the probability, given $k$, that either there is no God or he does not become incarnate and you still have $f$}
	- $P(f|k) = P(f \space \& \space c|k) + P(f \space \& \space \sim c|k)$
	- $P(f|k) = P(f|c \space \& \space k) \space P(c|k) + P(f| \sim c \space \& \space k) \space P(\sim c|k)$
		- $P(f|c \space \& \space k) \space P(c|k)= 1/40$ from above
		- $P(\sim c|k)=1-P(c|k) = 1-\textonequarter = \textthreequarters$
		- $P(f| \sim c \space \& \space k)$: the probability that $f$ occurs if there is no incarnation and there is the evidence of natural theology; we select a low ($1/1000$) value for this
		- $P(f|k) = \frac{1}{40}+\left( \frac{3}{4} \times \frac{1}{1000} \right)$
- $P(c|f \space \& \space k) = \frac{P(f | c \space \& \space k) \space P(c|k)}{P(f|k)} = \frac{1}{40} \times \frac{4000}{103} = \frac{100}{4000} \times \frac{4000}{103} = \boxed{\frac{100}{103}}$
- $P(c|e \space \& \space k) = P(c|f \space \& \space k) = \frac{100}{103}$ 
	- Because it cannot make any difference to the probability that $f$ (with $k$) gives to $c$, if we add to $f$ who the prophet is, and the details of the evidence, since we have already taken account in $f$ its strength in supporting $c$.
- $P(h|e \space \& \space k)$ will not be very different from $P(c|e \space \& \space k)$ (otherwise this would be a deception by God)
- Therefore, we conclude $P(h|e \space \& \space k) ≈ P(c|e \space \& \space k)$
- $\boxed{P(h|e \space \& \space k) ≈ \frac{100}{103} = 0.97}$
- My Google Sheet implementation of the above allowing you to change the estimated input probabilities: [Incarnation Probability (Swinburne) - Google Sheets](https://docs.google.com/spreadsheets/d/1XUVuNvtOvYuyIabsy6N37x4xjCJWi_Jxnw1sG7zRCsw/edit#gid=0)


--- 
#wishlist 
**Topic**: [[Bayesian statistics]]

**Source**
- [[Cameron Bertuzzi]]: [[2022-11-19 Cameron Bertuzzi CONVERTS to Catholicism]]


**Bibliography**
 - #wishlist *Epistemic Justification* by [[Richard Swinburne]]

**New Words**

- **tautology**: Needless repetition of the same sense in different words; redundancy.

---
Created: [[2022-12-04-Sun]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>
