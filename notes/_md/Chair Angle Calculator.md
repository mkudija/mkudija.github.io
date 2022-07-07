---
publish: true
---

*[[Woodworking]], [[Chairmaking]]*

# Chair Angle Calculator

### Background
The legs of a chair are often angled from the vertical. The side-to-side and front-to-back components of these angles are called *splay* and *rake*, and are easy to measure off a photograph of a chair. But when making a chair, it is easier to resolve the splay and rake into a single *resultant* angle along the *sightline*. [[Christopher Schwarz]] talks about this in *[[~The Stick Chair Book|The Stick Chair Book]]* ([PDF excerpt](https://blog.lostartpress.com/wp-content/uploads/2022/05/Stick-Chair_excerpt.pdf)):

>If you know the rake and splay that you want for your legs, you can use trigonometry to convert that to sightlines and resultants. There are equations, tables and calculators out there to guide you on that math path. (155)

A derivation is not provided, so I attempt one here.



### Derivation

In the diagram below, we are given the angles of *splay* (*s*) and *rake* (*r*), and we will compute the sightline angle ($\theta$) and the resultant angle ($\phi$). 

<img src="https://raw.githubusercontent.com/mkudija/img/main/2022-07-06_chair-angles/chair-angles.png" width="100%">
<center><a href="https://raw.githubusercontent.com/mkudija/img/main/2022-07-06_chair-angles/chair-angles.png" target="_blank"><i>Larger image</i></a></center>

Recall the trigonometric relationships of [SOH, CAH, TOA](https://www.mathsisfun.com/algebra/sohcahtoa.html). 

From Figure 1, we see that:
$$x = \sin(r)$$

From Figure 2, we see that:
$$y = \sin(s)$$

From Figure 3, we see that:
$$\tan(\theta) = \frac{x}{y}$$
Solving for $\theta$ and substituting the equations above for $x$ and $y$, we have a formula for the sightline angle $\theta$:
$$\boxed{sightline = \theta = \tan^{-1} \left( \frac{\sin(r)}{\sin(s)} \right)}$$

To compute the resultant angle $\phi$, first we need an expression for $A$ from Figure 3:
$$A = \frac{x}{sin(\theta)} = \frac{y}{cos(\theta)}$$

From Figure 4, which is the cross section along our sightline showing the resultant angle, we see that:
$$\sin(\phi) = \frac{A}{1} = A$$
Rearranging and substituting for $A$:
$$\phi = \sin^{-1}(A)=\sin^{-1}\left( \frac{x}{\sin(\theta)}  \right)=\sin^{-1}\left( \frac{\sin(r)}{\sin(\theta)}  \right)$$
$$\boxed{resultant=\phi=\sin^{-1}\left( \frac{\sin(r)}{\sin(\theta)}  \right)}$$
or
$$\phi = \sin^{-1}(A)=\sin^{-1}\left( \frac{y}{\cos(\theta)}  \right)=\sin^{-1}\left( \frac{\sin(s)}{\cos(\theta)}  \right)$$

$$\boxed{resultant=\phi =\sin^{-1}\left( \frac{\sin(s)}{\cos(\theta)}  \right)}$$

This is implemented in the following sheet: [Chair Angle Calculator - Google Sheets](https://docs.google.com/spreadsheets/d/1h0Ls0Vrd2oCE3AtCu19jd7lndnfqP5E0VC9R6khPpXU/edit#gid=0)


### Resources
- [Coming Soon: The Chairpanzee – Lost Art Press](https://blog.lostartpress.com/2020/10/04/coming-soon-the-chairpanzee/)
- [New Video: How to Use the Chairpanzee – Lost Art Press](https://blog.lostartpress.com/2020/10/29/new-video-how-to-use-the-chairpanzee/)
- [New in the Store: The Chairpanzee – Lost Art Press](https://blog.lostartpress.com/2020/10/27/new-in-the-store-the-chairpanzee/)
- [Woodworking in a Tiny Shop: Resultant and Sightline Angle Calculator](https://tinyshopww.blogspot.com/2020/05/resultant-and-sightline-angle-calculator.html)


---
Created: [[2022-07-05-Tue]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>
