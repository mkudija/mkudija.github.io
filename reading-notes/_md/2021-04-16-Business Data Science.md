
# [*Business Data Science: Combining Machine Learning and Economics to Optimize, Automate, and Accelerate Business*](https://www.amazon.com/Business-Data-Science-Combining-Accelerate/dp/1260452778/ref=sr_1_3?dchild=1&keywords=Business+Data+Science&qid=1618600384&sr=8-3) by Matt Taddy

`(New York: McGraw Hill, 2019), 331`

### Resources
- *The author's data and R scripts for the books is on [GitHub](https://github.com/TaddyLab/bds) (see also code for [MBA course](https://github.com/TaddyLab/MBA)).*
- *My code to accompany these notes is on [GitHub](https://github.com/mkudija/taddy-business-data-science).*
- *Amazon [author interview](https://www.amazon.science/business-data-science-is-a-lot-more-than-just-making-predictions-matt-taddy) discussing concepts from the book.ou*

## Preface

## Introduction
*Summary: Our goal is to produce interpretable models that translate data into insights for decision-making. The modern methods of business data science are characterized by the addition of big data and machine learning to classical statistical and economic methods.*

*Code for this section is [here](https://github.com/mkudija/taddy-business-data-science/tree/main/00-introduction).*

- The Goal: produce an *interpretable* model that translates raw data into information relevant to decision-making; project information into a low-dimensional space that contains key insights for decision making (3-4)
  - Motivating example: visualized CAPM outputs give a richer view for decisions making than just a messy plot of returns (Figure I.3, [reproduced here](https://github.com/mkudija/taddy-business-data-science/blob/main/0-introduction/3-stock-returns/0-introduction_stock-returns.ipynb))
- "Modern methods" are distinguished by *big data* and *machine learning*
  - Data Science ≈ statistics + BD + ML
  - Business Data Science ≈ statistics + BD + ML + economics + econometrics + business context
- **Big Data**: data can be "big" in terms of both *volume* and *complexity*
  - Big (*volume*) Data is where the scale swamps RAM and requires piping by data engineers
  - Big (*complexity*) Data is big *dimension* data where the assumptions of classical statistics break down ("big *p*" problems)
- **Machine Learning**: automatically build *predictions* from complex data
  - Focus is to maximize predictive performance on out-of-sample data
  - Limited *structural* interpretability: black box for making predictions when the future follows the same patterns as the past (with the implicit warning about the danger of changing patterns)
  - *Structural analysis* refers to building analytically from theory, as compared with the pragmatic, black-box *prediction* of machine learning
  - Good data science then is having an overall understanding of the domain to know the appropriate *prediction* tasks to throw at ML, and the *structural* problems to address with classical economics and statistics
  - "A policy-maker who can deploy ML to solve the many prediction tasks that they face will be able to automate and accelerate their decision process." (7)
  - ML prediction tools should be part of a larger system with goals beyond pure prediction
- **Computation**
  - This book uses R, but the key point is that "anyone working with data will need to continue learning and updating their computational (and methodological) skills"; best way to learn is by doing (11)


## Chapter 1: Uncertainty
*Summary: This chapter introduces **nonparametric** ("data driven", frequentist) and **parametric** ("theoretical", Bayesian) approaches to quantifying uncertainty. **The Bootstrap** is a flexible nonparametric method that works by resampling with replacement. The **Benjamini-Hochberg** algorithm provides a method of selecting variables by ranked p-value based on the desired false discovery rate. Finally, we learn about the **Bayesian** framework for combining assumptions with evidence.*

- **Parametric** vs **Nonparametric**
  - **Parametric**: "theoretical"
    - conditional on assumed true model
  - **Nonparametric**: "data driven"
    - allows for model misspecification
  

| Parametric               | Nonparametric                          |
| ------------------------ | -------------------------------------- |
| Quantifies uncertainty   | Quantifies uncertainty                 |
| "Theoretical"            | "Data-driven"                          |
| Bayesian                 | Frequentist                            |
| Assume CLT/Gaussian      | Use the Bootstrap                      |
| Specify distribution     | More flexible                          |
| "Ideal" for theory       | "Ideal" for decision-making            |
| High-dimensional data ok | Requires low-dimensional data $n >> p$ |


- **Frequentist** vs **Bayesian**
  - **Frequentist**: classical uncertainty
    - *"If I were able to see a new sample of data generated by the same processes and scenarios as my current data, how would my estimates change?"*
  - **Bayesian**: mathematical framework of beliefs (more below)
    - *"If you believe A and then you observe B, you should update your beliefs to C."*
- **Central Limit Theorem** (CLT): the average of independent random variables becomes normally distributed if your sample size is large enough
- **The Bootstrap**: uses resampling (*with replacement*) from your current sample to mimic the sampling distribution and introduce variability
  - use the Bootstrap because theoretical Gaussian distributions derived from the CLT are not valid for many complex settings (i.e. number of model parameters large relative to number of observations)
  - the Bootstrap will work in many settings where theory is either unavailable or incorrect (if the Bootstrap fails, there probably isn't a good theoretical replacement)
  - an alternative is the **Parametric Bootstrap**: generate new data by drawing from a fitted model (the results are sensitive to how well the model represents reality, but this is a practical option when more robust procedures are impossible)
- ***p*-values**: represents how rare or strange your sample would be if the null hypothesis is true
  - the proportion of times that you would wrongly reject your safe null if the test statistic you've observed is enough to lead you to adopt the alternative
  - measures the probability mass in the tails past your observed test statistic
- **Benjamini-Hochberg (BH) FDR Control**: controls your false discovery rate (FDR) by defining a cutoff on the ranked list of *p*-values from your model
  - $FDR=\mathop{\mathbb{E}} \left[ \frac{FalsePositives}{TestsCalledSignificant} \right]$
  - Select your target $FDR$ of $q$, and keep all *p*-values such that $p \leq q\frac{k}{N}$
  - Gives a decent (often conservative) guess at FDR
- **Bayesian Inference**: the mathematical framework of beliefs
  - characterizes probabilities over models and parameters by appealing to the idea of subjective beliefs rather than repeated trials
  - quantification of risks and expected rewards is inherently Bayesian
  - "If you believe *A* and then you observe *B*, you should update your beliefs to *C*."
  - provides a framework for combining *assumptions* with *evidence*
  - mechanically works with combination of *prior distributions* and *likelihood* (the probability of the data you have observed given a fixed set of mode parameters)
  - inherently *parametric* since you specify a model and then update view of uncertainty based on new data


## Chapter 2: Regression
*Summary: *

*Code for this chapter is [here](https://github.com/mkudija/taddy-business-data-science/tree/main/02-regression).*

## Chapter 3: Regularization
*Summary: **Regularization** allows us to develop candidate models and select the best model for OOS performance. We add a penalty term and then minimize the penalized deviance; a common penalty construction is the **Lasso**. Then we can select the optimal penalty weight—$\lambda$—using **cross validation** or **information criteria** as our model selection process. Finally, we can approximate the uncertainty of such a model using a **parametric bootstrap** or **subsampling**.*

- **Regularization** context: provides a framework when working with high-dimensional data to develop *candidate models* and then *select* the best model to minimize error on out-of-sample data (needed to avoid *overfit*)
  - Regularization penalizes model complexity to stabilize the system, minimizes *penalized* deviance
  - "Regularization is the key to modern statistics" (77)
  - "Regularization is trading variance (noise) for bias" (91)
- The only $R^{2}$ we care about is *out-of-sample* $R^{2}$
  - In-sample $R^{2}$ is always increased with more variables, making it look artificially good (it can even produce a *negative* out-of-sample $R^{2}$, or model that performs worse than no model at all)
- **Cross validation**: use out-of-sample experiments to choose the best model
  - Use data to select the best model
  - *K*-fold out-of-sample cross-validation: split data into *K* folds, fit coefficients on everything except *k*th fold, then record $R^{2}$ for the left-out *k*th fold
- **Backward stepwise regression**: start with full model and cut it back to size
  - Start with full model, cut back variables below $\alpha$ using BH FDR control
  - This is generally *not* ideal because it does not handle *multicollinearity* (correlation between inputs) well
- **Forward stepwise regression**: build from simplicity to complexity, *greedy* search strategy, fast and stable, stable
- Regularization minimizes *penalized* deviance:
  - $\hat{\beta} = \mbox{argmin} \left\{-\frac{2}{n} \log \mbox{lhd} (\beta) + \lambda \sum_{k}{c(\beta_{k})} \right\}$ where $\lambda \sum_{k}{c(\beta_{k})}$ is the penalty term and $c(\beta_{k})$ is the cost on the size of the coefficient
  - This accounts for both the *estimation cost* (deviance, distance between data and model) and the *testing cost* (cost of $\beta \neq 0$) 
- The **lasso** has $c(\beta_{k})=|\beta|$
  - Default because least bias on large signals while retaining the stability of a convex penalty, also automatic variable screening since some $\beta$ will be exactly zero
  - Provides an enumeration of candidate models (different values of $\lambda$), then use model selection to choose the best $\lambda$
  - Lasso regularization path: start with $\lambda$ such that $\hat\beta_{1}=0$, then shrink $\lambda$ to reduce the penalty on $\beta$ and iteratively add complexity to the model
  - $\lambda$ operates on all $\beta$, so typically scale by $\mbox{sd}(x)$ so that the penalty on $\beta$ is measured on the scale of 1 standard deviation change in $x$

**Model Selection**: use *cross validation (CV)* or *information criteria (IC)* to select the best $\lambda$
- Recall: $\lambda$ is the penalty weight (signal-to-noise filter like a radio squelch)
- ***K*-Fold CV Lasso**: obtain candidate models from lasso, fit lasso path on data except *k*th fold and calculate deviance on *k*th fold, and choose $\lambda$ by either **CV-min** (recommended) or **CV-1se** (more conservative)
  - Cross validation answers: *"Which model does best in predicting unseen data?"*
  - CV is a computational experiment to approximate OOS errors
- **Information Criteria (IC)**: analytic approximation of OOS errors, many flavors (AICc, AIC, BIC, etc.)
  - *Akaike's criterion*: $\mbox{AIC} = \mbox{deviance} + 2df$ where deviance is calculated in-sample and $df$ are your model degrees of freedom; true for low-dimensional models
  - *Corrected AIC*: $\mbox{AICc} = \mbox{deviance} + 2df \frac{n}{n-df-1}$, should always be used over AIC: works where AIC doesn't and provides the same answer where it does
  - *Bayes criterion*: $\mbox{BIC} = \mbox{deviance} + \log(n) \times df$, attempts to get at the "true" model and is more conservative
- If you have time and answer is important, do CV. AICc is fast and stable. Typically use a combination of the two.

**Lasso Uncertainty**
- Uncertainty quantification not easy because of penalty term and high-dimensional objects, but can use **parametric bootstrap**, **subsampling**, or **sample splitting** (ch 6)
- **Parametric Bootstrap**: rather than resampling with replacement (as in nonparametric bootstrap, which will overfit), generate *new* data from a model with less bias, say $\bar\lambda \approx \lambda/4$
  - Drawback: relies upon the correctness of your data generating process
- **Subsampling**: re-estimate your target using *without-replacement* subsamples
  - Estimates are based on smaller sample than you actually have, so must assume a *learning rate* to adjust a size-*m* uncertainty for size-*n* sample estimate (typically $\sqrt{n}$)
- Both are approximation tools that should be treated with skepticism


## Chapter 4: Classification
*Summary: *



## Chapter 5: Experiments
*Summary: *



## Chapter 6: Controls
*Summary: *



## Chapter 7: Factorization
*Summary: *



## Chapter 8: Text as Data
*Summary: *



## Chapter 9: Nonparametrics
*Summary: *



## Chapter 10: Artificial Intelligence
*Summary: *


---

**Errata**
- 37: "is then available via Bayes rule" --> "is then available via **Bayes'** rule"
- 78: "in some data-dependent matter" --> "in some data-dependent **manner**"