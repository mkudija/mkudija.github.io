---
publish: true
latex: true
---

*[[Woodworking]], [[Chairmaking]]*

# Chair Angle Calculator

### Calculator

<div id="chair-calculator" style="background-color: #f5f5f5; border-radius: 8px; padding: 20px; margin: 20px 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h4 style="margin-top: 0; color: #333;">Interactive Angle Calculator</h4>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px;">
    <div>
      <label for="rake-input" style="display: block; margin-bottom: 5px; font-weight: 600; color: #555;">Rake Angle (degrees):</label>
      <input type="number" id="rake-input" value="15" step="0.5" min="0" max="45" style="width: 100%; padding: 8px; border: 2px solid #ddd; border-radius: 4px; font-size: 16px;">
    </div>
    
    <div>
      <label for="splay-input" style="display: block; margin-bottom: 5px; font-weight: 600; color: #555;">Splay Angle (degrees):</label>
      <input type="number" id="splay-input" value="15" step="0.5" min="0" max="45" style="width: 100%; padding: 8px; border: 2px solid #ddd; border-radius: 4px; font-size: 16px;">
    </div>
  </div>
  
  <div style="background-color: #fff; border-radius: 6px; padding: 15px; border-left: 4px solid #4CAF50;">
    <h5 style="margin-top: 0; color: #333;">Results:</h5>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
      <div>
        <div style="font-size: 14px; color: #666; margin-bottom: 3px;">Sightline (α):</div>
        <div id="sightline-result" style="font-size: 24px; font-weight: 700; color: #4CAF50;">--</div>
      </div>
      <div>
        <div style="font-size: 14px; color: #666; margin-bottom: 3px;">Resultant (θ):</div>
        <div id="resultant-result" style="font-size: 24px; font-weight: 700; color: #2196F3;">--</div>
      </div>
    </div>
  </div>
</div>

<script type="module">
  // Chair Angle Calculator Module
  function calculateAngles(rakeDeg, splayDeg) {
    // Convert degrees to radians
    const rakeRad = rakeDeg * Math.PI / 180;
    const splayRad = splayDeg * Math.PI / 180;
    
    // Calculate sightline: α = arctan(tan(r) / tan(s))
    const sightlineRad = Math.atan(Math.tan(rakeRad) / Math.tan(splayRad));
    const sightlineDeg = sightlineRad * 180 / Math.PI;
    
    // Calculate resultant: θ = arctan(√(tan²(r) + tan²(s)))
    const tanR = Math.tan(rakeRad);
    const tanS = Math.tan(splayRad);
    const resultantRad = Math.atan(Math.sqrt(tanR * tanR + tanS * tanS));
    const resultantDeg = resultantRad * 180 / Math.PI;
    
    return {
      sightline: sightlineDeg,
      resultant: resultantDeg
    };
  }
  
  function updateResults() {
    const rakeInput = document.getElementById('rake-input');
    const splayInput = document.getElementById('splay-input');
    const sightlineResult = document.getElementById('sightline-result');
    const resultantResult = document.getElementById('resultant-result');
    
    const rake = parseFloat(rakeInput.value);
    const splay = parseFloat(splayInput.value);
    
    // Validate inputs
    if (isNaN(rake) || isNaN(splay) || rake <= 0 || splay <= 0) {
      sightlineResult.textContent = '--';
      resultantResult.textContent = '--';
      return;
    }
    
    const angles = calculateAngles(rake, splay);
    
    // Display results rounded to 2 decimal places
    sightlineResult.textContent = angles.sightline.toFixed(1) + '°';
    resultantResult.textContent = angles.resultant.toFixed(1) + '°';
  }
  
  // Initialize calculator
  document.addEventListener('DOMContentLoaded', () => {
    const rakeInput = document.getElementById('rake-input');
    const splayInput = document.getElementById('splay-input');
    
    // Add event listeners for real-time calculation
    rakeInput.addEventListener('input', updateResults);
    splayInput.addEventListener('input', updateResults);
    
    // Calculate initial values
    updateResults();
  });
  
  // Also calculate on load if DOM is already ready
  updateResults();
</script>

### Background
The legs of a chair are often angled from the vertical. The side-to-side and front-to-back components of these angles are called *splay* and *rake*, and are easy to measure off a photograph of a chair. But when making a chair, it is easier to resolve the splay and rake into a single *resultant* angle along the *sightline*. [[Christopher Schwarz]] talks about this in *[[2022-10-11-The Stick Chair Book|The Stick Chair Book]]* ([PDF excerpt](https://blog.lostartpress.com/wp-content/uploads/2022/05/Stick-Chair_excerpt.pdf)):

>If you know the rake and splay that you want for your legs, you can use trigonometry to convert that to sightlines and resultants. There are equations, tables and calculators out there to guide you on that math path. (155)

Schwartz cites [[Drew Langsner]]'s *[[~The Chairmaker's Workshop|The Chairmaker's Workshop]]* as giving the best description of sightlines and resultants. This book provides an overview of the method, the diagram below showing how these angles are laid out on a chair seat (from page 291), and tables of the computed sightline and resultant given the rake and splay which is helpful for checking my calculations below.

<img src="https://raw.githubusercontent.com/mkudija/img/main/2022-07-06_chair-angles/sightline-resultant.jpg" width="100%">

A derivation is not provided in either of these sources, so I provide one here. Thanks to [Woodworking in a Tiny Shop](https://tinyshopww.blogspot.com/2020/05/resultant-and-sightline-angle-calculator.html) for providing his solution which helped me catch an error in my first version.



### Derivation

In the diagram below, we are given the angles of *splay* (*s*) and *rake* (*r*), and we will compute the sightline angle ($\alpha$) and the resultant angle ($\theta$). 


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
