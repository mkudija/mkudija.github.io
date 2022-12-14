---
aliases: [Biostatistics For Dummies]
title: Biostatistics For Dummies
author: John Pezzullo
category: Medical
publisher: John Wiley & Sons
total_page: 425
cover_url: http://books.google.com/books/content?id=QYcQAAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api
publish_date: 2013-07-29
isbn10: 1118553985
isbn13: 9781118553985
started: 
finished: 
latex: true
---
# *[Biostatistics For Dummies]()* by [[John Pezzullo]]

<img src="http://books.google.com/books/content?id=QYcQAAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api" width=150>

`(New York: John Wiley & Sons, 2013-07-29), 425`

I want to read this book for a couple of reasons:
1. Some of this is relevant to work
2. *[[2018-01-01-How Not to Die|How Not To Die]]* cited a bunch of clinical studies, and I want to understand the math behind "showed a 34% reduction in cancer risk" or whatever
3. Epidemeological data
4. General stats knowledge

## Introduction
Biostats is the practical application of statistics to biology. Author chose topics based on a survey of popular topics covered in graduate-level biostats courses, with a focus on clinical research. 


## Biostatistics Basics
Chapter 1: Biostats 101
*skimmed*

Chapter 2: Basic Math
*skimmed*

Chapter 3: Basic Statistics
Review of probability, odds, randomness, population vs. sample, probability distribution functions, accuracy vs. precision, 

Standard Error (SE): tells you how much the estimate or measured value might vary if you were to repeat the experiment or measurement many times using a different random sample from the same population (see ch 9)

Confidence intervals (ch 10)

statistical decision theory

Test significance: just compare the difference you are interested in versus a measure of the randomness of your data. The different formulas just give different ways of quantifying both of these (42). End result is a p-value (probability that random fluctuations alone account for the difference)

Type I vs. Type II errors

Power of test (interplay of significance, sample size, and effect size)



Chapter 4: Statistical Software
skimmed

Chapter 5: Conducting Clinical Research
Randomization allows for:
1. elmininates selection bias
2. permits appliaction of statistical methods to data collected
3. facilitates blinding

Type I error inflation can quickly get out of hand if you have multiple sequential statisitical tests, so be aware of this. Also gives ways of dealing with this based on your objectives (75)

Chapter 6: Clinical Trials and Drug Development

Phase I: determine maximum tolerated dose (MTD). "Dose makes the poison." (80)

Phase II: "dose finding trials" to monitor the drug's performance

Phase III: prove the dose selected is safe and effective

Phase IV: monitor marketed drug

PK/PD Studies
- PK: *pharmacokinetics* is the study of how fast and how completely the drug is absorbed into the body, how it is distributed in the body, to what extent it is metabolized, and how quickly it is excreted (what the body does to the drug)
- PD: *pharmacodynamics* is the relationship between the concentration of the drug and the effects on the body (what the drug does to the body)

## Data
Chapter 7: Data to Computer

Types of data:
- **Nominal**: categories (not ordered)
- **Ordinal**: ordered categories
- **Interval**: distance between number is meaningful, but starting point is not (i.e. Celcius temp scale)
- **Ratio**: has a true zero point

Check data for errors:
- look at min/max
- sort values
- search for blanks, commas, etc.
- tabulate categoral values (`value_counts()`)
- color coding cells

Chapter 8: Graphing Data
- for a distribution, getting the center, dispersion, symmetry, and shape
- standard deviation, variance, and coefficient of variation (SD/mean)
- skewness (left-right), kurtosis (shape)
- chart types: histograms, box plots, etc.

Chapter 9: Accuracy and Precision
*skimmed*
- discussion of sources of error and how to minimize

Chapter 10: Confidence
*skimmed*
- Confidence intervals, discussion and calculation

Chapter 11: Fuzzy In, Fuzzy Out
*skimmed*
- discussion of error propagation and formulas 

## Comparing Groups
Chapter 12: Comparing Averages Between Groups
A number of different tests are available to compare averages between groups, based on the number of comparisons, assumptions about the underlying data, etc. Use this section to find a test appropriate to your situation. Examples include student t-test, ANOVA, ANCOVA, etc. 

Chapter 13: Comparing Proportions and Cross-Tabulations

Chapter 14: Fourfold Tables

Chapter 15: Incidence and prevalence Rate in Epidemiologic Data
**Prevalance**: proportion of the population that has the condition at a point in time

**Incidence**: rate at which new cases appear in the population

Chapter 16: Noninferior

Show that things are not different (bioequivalence,, theraputic noninferiority, or absence of harmful effects). Tools include significance tests and confidence intervals.

## Correlation and Regression
Chapter 17: Correlation and Regression
Pearson correlation coefficient (r) measures correlation (straight line when plotted). 

Chapter 18: Straight-Line Regression
- Y: dependent variable (outcome)
- X: independent variable (predictor)
- a: intercept
- b: slope

To fit, we solve $SSQ = (a + bX - Y)^2$ by setting the partial derivatives of SSQ with respect to a and b equal to 0.

$R^2$: coefficient of determination, what percent of the total variability in the dependent variable is explained by the model

Chapter 19: Multiple Regression
- create a scatter chart matrix ([Python Example here](https://seaborn.pydata.org/generated/seaborn.pairplot.html)) to view your data beforehand to evaluate appropriatness of MLR
- 259-260 gives info for reading regression results
- Syntergy and anti-synergy: test with an interaction term (multiplied)
- Collinearity: this doesn't impact the power of your model, but makes it hard to tell which independent variable is responsible for the change

Chapter 20: Logistic Regression (Categorical Result)
- logistic regression to predict categorical outcome
- sensitivity: predicting a yes outcome when the actual outcome is yes
- specificity: predictint a no outcome when the actual outcome is no
- ROC curve: displayes the sensitivity/specificity tradeoff for a fitted model

Chapter 21: Other Regressions
- GLM (generalized linear model) let's you specify the link function and therefore perform almost any kind of regression; [statsmodels here](http://www.statsmodels.org/dev/glm.html)

# Part V: Analyzing Survival Data
Chapter 22: Survival Data
- hazard rate: probability of dying in the next small interval of time
- survival rate: probability of living for a certain amount of time after the starting point
- pages 320+ detail how to construct survival data

Chapter 23: Survival Times
- use the log-rank test to determine if observed differences in survival curves are significant

Chapter 24: Survival Regression


# Part VI: The Part of Tens
Chapter 25: Ten Distributions Worth Knowing

Chapter 26: Ten Easy Ways to Estimate How Many Subjects You Need


---
Created: 2017-12-06
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>
