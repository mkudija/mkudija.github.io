---
publish: true
---

# A Crash Course in Causality
*[A Crash Course in Causality: Inferring Causal Effects from Observational Data - Welcome and Introduction to Causal Effects | Coursera](https://www.coursera.org/learn/crash-course-in-causality/home/week/1)*

by [Dr. Jason Roy](https://pets.rutgers.edu/people/jason-roy/) from [UPenn Center for Causal Inference](https://www.cceb.med.upenn.edu/cci)


<details>
 <summary><i>Contents</i></summary>
<!-- MarkdownTOC autolink="true" -->

- [Welcome and Introduction to Causal Effects](#welcome-and-introduction-to-causal-effects)
	- [Confusion over causality](#confusion-over-causality)
	- [Potential outcomes and counterfactuals](#potential-outcomes-and-counterfactuals)
	- [Hypothetical interventions](#hypothetical-interventions)
		- [Causal effects](#causal-effects)
	- [Causal assumptions](#causal-assumptions)
	- [Stratification](#stratification)
	- [Incident user and active comparator designs](#incident-user-and-active-comparator-designs)
- [Confounding and Directed Acyclic Graphs \(DAGs\)](#confounding-and-directed-acyclic-graphs-dags)
	- [Confounding](#confounding)
	- [Causal graphs](#causal-graphs)
	- [Relationship between DAGs and probability distributions](#relationship-between-dags-and-probability-distributions)
	- [Paths and associations](#paths-and-associations)
	- [Conditional independence \(d-separation\)](#conditional-independence-d-separation)
	- [Confounding revisited](#confounding-revisited)
	- [Backdoor path criterion](#backdoor-path-criterion)
	- [Disjunctive cause criterion](#disjunctive-cause-criterion)

<!-- /MarkdownTOC -->
</details>


# Welcome and Introduction to Causal Effects
## Confusion over causality
- **Spurious Correlation**: causally unrelated variables that might happen to be highly correlated with each other over some period of time (i.e. divorce correlated with margarine consumption)
- **Anecdotes**: might be confident in our anecdotes but might not be correct
- **Science reporting**: this is "linked" to that: linked is ambiguous
- Causal inference or causal modeling attempts to clear these problems up by:
	- formal definitions of causal effects
	- assumptions necessary to identify causal effects from data
	- sensitivity analysis to determine impact of violations of assumptions on conclusions
- Course focuses on **observational studies** and **natural experiments**
- **Assumptions**: requires making untestable assumptions (can't check with the data)


## Potential outcomes and counterfactuals
- Treatment $A$ on outcome $Y$
- $Y^a$ is the outcome observed if treatment is $a$
- **Counterfactual outcomes** are ones that would have been observed had the treatment been different
	- if treatment was $A=1$, counterfactual is $Y^0$

## Hypothetical interventions
- **Intervention**: causal effects of variables that can be manipulated
- **Immutable variables**: variables you can't manipulate (race/gender/age)
	- but can do creative things like different name on resume, or focus on outcome of something you can control (like decision to have surgery rather than obesity)
- This course focuses on **interventions** since they are actionable
- **Causal effect** occurs on $Y$ if $Y^1 \ne Y^0$
- The **Fundamental Problem of Causal Inference** is that we can only observe one potential outcome for each person, so need to look at a population

### Causal effects
- **Average Causal Effect**: hypothetical difference between the whole population getting different treatments
	- $ACE = E(Y^1-Y^0)$
	- Example: suppose $E(Y^1-Y^0)=-0.1$, meaning if 1000 people were to have surgery, 100 fewer would have complications with this treatment
- Conditioning (given, or conditional on a variable):
	- $E(Y^1-Y^0) \ne E(Y|A=1) - E(Y|A=0)$
	- $E(Y|A=1)$: expected value of $Y$ given $A=1$, this restricts to a subpopulation of people who got $A=1$
	- $E(Y^1)$ is the mean of the whole population treated with $A=1$
	- Populations may be different in important ways
- We might be interested in other causal effects:
	- $E(Y^1/Y^0)$: Causal relative risk
	- $E(Y^1-Y^0|A=1)$: Causal effect of treatment on the treated population
	- $E(Y^1-Y^0|V=v)$: Average causal effect in a subpopulation
- *How do we use observed data to link observed outcomes to potential outcomes?*
	- Need to make assumptions, focus of this course

## Causal assumptions
- **Identifiability** requires making untestable, causal assumptions
	- assumptions are about the observed data: $Y$, $A$, and $X$
- **Stable Unit Treatment Value Assumption (SUTVA)**
	- Units do not interfere with each other: treatment assignment of one unit does not affect that outcome of another unit
	- One version of treatment
- **Consistency**
	- The potential outcome under treatment $A=a$, $Y^a$ is equal to the observed outcome if the actual treatment received is $A=a$
	- Links potential outcomes to observed outcomes
- **Ignorability** (no unknown measures confounder assumptions)
	- Given pre-treatment covariates $X$, treatment assignment is independent from the potential outcomes: $Y^0,Y^1 \mathbin{\perp\kern-11mu\perp} A|X$ (read as: potential outcomes $Y^0$ and $Y^1$ are independent of treatment variable $A$ conditional on $X$)
	- Among people with the same values of $X$, we can think of treatment $A$ as being randomly assigned
	- Random = independent of outcomes, might not be random in another sense
- **Positivity**
	- For every set of values for $X$, treatment assignment was not deterministic: $P(A=a|X=x)>0$ for all $a$ and $x$
	- Helps define who the population of interest is, excludes those who could never receive the treatment
- **Example**
	- $E(Y|A=a,X=x)$ involves only observed data ($Y$, $A$, and $X$)
	-  $E(Y|A=a,X=x) = E(Y^a|A=x,X=x)$ by **consistency**, goes from just observed data ($Y|A=a$) to something that involves outcomes ($Y^a$)
	- $E(Y|A=a,X=x) = E(Y^a|X=x)$ by **ignorability**, allows us to drop the conditioning on treatment, conditioning on $A$ doesn't provide any additional information
	- For a marginal causal effect, we can average over $X$

## Stratification
- Stratification aka Standardization: stratify on important variables and average over the distribution of those variables
	- composed of *conditioning* and *marginalizing*, or *stratifying* and then *averaging*, weighted by the probability (size)
- Suppose single categorical $X$ variable, then average over the distribution of $X$, a standardized mean which is the average potential outcome: 
	- $E(Y^a)=\sum_{x}{E(Y|A=a,X=x)P(X=x)}$


**Example**: treatment Saxa for MACE:

| Treatment | MACE=yes | MACE=no | Total |
| --------- | -------- | ------- | ----- |
| Saxa=yes  | 350      | 3650    | 4000  |
| Saxa=no   | 500      | 6500    | 7000  |

- Probability of MACE given Saxa=yes: $350/4000=0.088$
- Probability of MACE given Saxa=no: $500/7000=0.071$
- → raw data makes Saxa look worse, but might be because it was assigned to patients who were worse off initially
- So we stratify/standardize on the $X$ variable (prior OAD use):

Prior OAD use=no:

| Treatment | MACE=yes | MACE=no | Total |
| --------- | -------- | ------- | ----- |
| Saxa=yes  | 50       | 950     | 1000  |
| Saxa=no   | 200      | 3800    | 4000  |

- Probability of MACE given Saxa=yes: $50/1000=0.050$
- Probability of MACE given Saxa=no: $200/4000=0.050$


Prior OAD use=yes:

| Treatment | MACE=yes | MACE=no | Total |
| --------- | -------- | ------- | ----- |
| Saxa=yes  | 300      | 2700    | 3000  |
| Saxa=no   | 300      | 2700    | 3000  |

- Probability of MACE given Saxa=yes: $300/3000=0.100$
- Probability of MACE given Saxa=no: $300/3000=0.100$
- → in either group the risk of MACE is the same regardless of Saxa use
- Next compute mean potential outcome for Saxa:
	- $E(Y^{saxa}) = E(Y|A=saxa,X=OAD_{yes})P(OAD_{yes})+E(Y|A=saxa,X=OAD_{no})P(OAD_{no})$
	- $E(Y^{saxa}) = (300/3000)(6000/11000)+(50/1000)(5000/11000)$
	- $E(Y^{saxa}) = 0.077$ is the probability of MACE if everyone had been assigned Saxa
- Next compute mean potential outcome for alternate
	- $E(Y^{not-saxa}) = (300/3000)(6000/11000)+(200/4000)(5000/11000)$
	- $E(Y^{not-saxa}) = 0.077$ is the probability of MACE if everyone had *not* been assigned Saxa (same for both groups)
- Challenges: often you need many $X$ variables to achieve ignorability and will have many empty cells in this example, so need alternatives to standardization (matching, inverse probability of treatment weighting, propensity score methods, instrumental variable methods—cf. *[[2021-04-16-Business Data Science#Chapter 5 Experiments|Business Data Science]]*)



## Incident user and active comparator designs
- **Incident user design** (aka new user design): restrict the treated population to those newly initiating treatment (so as to not confound people who tried the treatment in the past and are still benefitting from the treatment)
	- or realign time index for each user for when they started treatment
- **Active comparator design**: include people with similar treatments in the treatment group: leads to less confounding but makes the causal inference apply to other treatments
- Can combine incident user and active comparator designs

# Confounding and Directed Acyclic Graphs (DAGs)

## Confounding

## Causal graphs

## Relationship between DAGs and probability distributions

## Paths and associations

## Conditional independence (d-separation)

## Confounding revisited

## Backdoor path criterion

## Disjunctive cause criterion

---
Created: [[2022-05-23-Mon]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>
