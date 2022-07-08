---
publish: true
---

*[[Woodworking]], [[Chairmaking]]*

# Chair Angle Calculator

### Background
The legs of a chair are often angled from the vertical. The side-to-side and front-to-back components of these angles are called *splay* and *rake*, and are easy to measure off a photograph of a chair. But when making a chair, it is easier to resolve the splay and rake into a single *resultant* angle along the *sightline*. [[Christopher Schwarz]] talks about this in *[[~The Stick Chair Book|The Stick Chair Book]]* ([PDF excerpt](https://blog.lostartpress.com/wp-content/uploads/2022/05/Stick-Chair_excerpt.pdf)):

>If you know the rake and splay that you want for your legs, you can use trigonometry to convert that to sightlines and resultants. There are equations, tables and calculators out there to guide you on that math path. (155)

A derivation is not provided, so I provide one here. Thanks to [Woodworking in a Tiny Shop](https://tinyshopww.blogspot.com/2020/05/resultant-and-sightline-angle-calculator.html) for providing his work which helped me catch an error in my first version.



### Derivation

In the diagram below, we are given the angles of *splay* (*s*) and *rake* (*r*), and we will compute the sightline angle ($\alpha$) and the resultant angle ($\theta$). 

==DIAGRAM NEEDS TO BE REVISED==

<img src="https://raw.githubusercontent.com/mkudija/img/main/2022-07-06_chair-angles/chair-angles.png" width="100%">
<center><a href="https://raw.githubusercontent.com/mkudija/img/main/2022-07-06_chair-angles/chair-angles.png" target="_blank"><i>Larger image</i></a></center>

Recall the trigonometric relationships of [SOH, CAH, TOA](https://www.mathsisfun.com/algebra/sohcahtoa.html). 

First we need expressions for $x$ and $y$:
$$\tan(s) = \frac{x}{h} \rightarrow \boxed{x=h\tan(s)}$$
$$\tan(r) = \frac{y}{h} \rightarrow \boxed{y=h\tan(r)}$$
Then we write an expression for the sightline angle $\alpha$:

$$\tan(\alpha)=\frac{y}{x}=\frac{h\tan(r)}{h\tan(s)}$$
$$\text{sightline: } \boxed{\alpha=\tan^{-1}\left(\frac{\tan(r)}{\tan(s)} \right)}$$


Next to compute the resultant angle $\theta$, we need an expression for $z$:
$$x^2+y^2=z^2$$
$$z=\sqrt{x^2+y^2}$$
Substituting for $x$ and $y$ from above:
$$z=\sqrt{h^2\tan^2(r)+h^2\tan^2(s)}=h\sqrt{\tan^2(r)+\tan^2(s)}$$
Now we can write an expression for $\theta$ and substitute in the above:
$$\tan(\theta)=\frac{z}{h}$$
$$\tan(\theta)=\frac{h\sqrt{\tan^2(r)+\tan^2(s)}}{h}$$
$$\tan(\theta)=\sqrt{\tan^2(r)+\tan^2(s)}$$
$$\text{resultant: } \boxed{\theta=\tan^{-1}\left( \sqrt{\tan^2(r)+\tan^2(s)} \right)}$$

This is implemented in the following sheet: [Chair Angle Calculator - Google Sheets](https://docs.google.com/spreadsheets/d/1h0Ls0Vrd2oCE3AtCu19jd7lndnfqP5E0VC9R6khPpXU/edit#gid=0)


### Resources
- [Coming Soon: The Chairpanzee – Lost Art Press](https://blog.lostartpress.com/2020/10/04/coming-soon-the-chairpanzee/)
- [New Video: How to Use the Chairpanzee – Lost Art Press](https://blog.lostartpress.com/2020/10/29/new-video-how-to-use-the-chairpanzee/)
- [New in the Store: The Chairpanzee – Lost Art Press](https://blog.lostartpress.com/2020/10/27/new-in-the-store-the-chairpanzee/)
- [Woodworking in a Tiny Shop: Resultant and Sightline Angle Calculator](https://tinyshopww.blogspot.com/2020/05/resultant-and-sightline-angle-calculator.html)


---
Created: [[2022-07-05-Tue]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>
