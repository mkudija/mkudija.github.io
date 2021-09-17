
# [*The Pragmatic Programmer: From Journeyman to Master*](https://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X) by Andrew Hunt

<img src="https://images-na.ssl-images-amazon.com/images/I/41as+WafrFL._SX258_BO1,204,203,200_.jpg" width=150>

`(City: Publisher, YYYY), PPP`


I need to start a discussion of *The Pragmatic Programmer: From Journeyman to Master* by Andrew Hunt and David Thomas by acknowledging that I'm not a programmer, at least not formally. Software Engineer is not in my job title, nor do I have a degree in computer science. However, I did learn basic programming in Fortran and Matlab while studying aerospace engineering, and I have since learned Python and used it over the past several years for analysis and basic automation. So, while I do not write software at a level that could fully benefit from this book, I found much of the advice contained therein to be helpful. The two aspects of Hunt and Thomas' work I found the most insightful are the development of a set of guiding principles and the focus on developing a well-rounded generalism with a mindset of continual education.

### Generalism & Learning
I'll start with the attitude of generalism they advise. Hunt and Thomas suggest that a pragmatic programmer is more of a jack of all trades than a specialist, able to adapt to a continually changing technology landscape with broad skills and continuous learning. As a pragmatic programmer you should "try hard to be familiar with a broad range of technologies and environments, and you work to keep abreast of new developments."[^jack] They advise to make learning a habit by investing regularly in your knowledge portfolio. I would add that not only does continual learning keep you competitive, it is the most interesting way to approach your work.

[^jack]: Hunt, Andrew, and David Thomas, *The Pragmatic Programmer: From Journeyman to Master* (Menlo Park: Addison-Wesley Professional, 1999), xix.

### Tidy Data
*The Pragmatic Programmer* has been helpful to bring basic automation to business processes I work with. As an aside, a prerequisite for automating anything is well-formatted data, for which I recommend both [Data organization in spreadsheets](http://www.tandfonline.com/doi/full/10.1080/00031305.2017.1375989) by Karl W. Broman and Kara H. Woo, and [Tidy Data](http://www.stat.wvu.edu/~jharner/courses/stat623/docs/tidy-dataJSS.pdf) by Hadley Wickham.

First, Broman and Woo give a number of helpful suggestions for working with Excel. Like it or not, Excel is a staple of life in most business settings. Acknowledging that Excel is often not ideal, and also that it will not be fully replaced without extensive workforce retraining, our goal becomes how to interface with Excel intelligently. While others may insist on using Excel, you need never to touch Excel directly: just read and write data to Excel files while running your analysis and visualization in Python, R or another language. Some of the tips recommended by Broman and Woo include separating analysis and visualization of data, being consistent, and using [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (`YYYY-MM-DD`) date formats. I firmly agree with their recommendation that "data rearrangement is best accomplished via code (such as with an R, Python, or Ruby script) so you never lose the record of what you did to the data."[^spreadsheets] The one recommendation of theirs that I disagree with is the suggestion to leave no cells empty and fill all with `NA` or `-`. I recommend leaving cells blank, since the filler is one more opportunity for data errors. Also, when working in Python, the `pandas.DataFrame.fillna()` method can be called immediately after loading data from Excel to consistently fill all empty cells. This is just a matter of preference, however, and I strongly recommend adherence to the principles they give.

[^spreadsheets]: [Broman, Karl, and Kara Woo. "Data organization in spreadsheets.", *The American Statistician* 0 (2017): 1.](http://www.tandfonline.com/doi/full/10.1080/00031305.2017.1375989)

Hadley Wickham's Tidy Data principles are a good guide for working with data, whether in Excel or otherwise. In essence, he recommends formatting data such that:
1. Each variable forms a column.
2. Each observation forms a row.
3. Each type of observational unit forms a table.[^tidy]


[^tidy]: [Wickham, Hadley. “Tidy Data.” *Journal of Statistical Software* 59 (2014): 4.](http://vita.had.co.nz/papers/tidy-data.pdf)

Following the advice of Froman, Woo, and Wickham for handling data sets the stage for integrating the lessons from *The Pragmatic Programmer*, which is given by means of Tips, or principles.
 
### Principles
This mindset of continual learning paired with well-rounded generalism naturally leads to the principles, or "Tips", Hunt and Thomas expound. Principles form a general framework from which you can address particular situations. "You shouldn't be wedded to any particular technology, but have a broad enough background and experience base to allow you to choose good solutions in particular situations. Your background stems from an understanding of the basic principles of computer science, and your experience comes from a wide range of practical projects. Theory and practice combine to make you strong."[^principles] Another great example of distilled principles is Ray Dalio's [*Principles: Life and Work*](https://www.amazon.com/Principles-Life-Work-Ray-Dalio-ebook/dp/B071CTK28D).

[^principles]: Hunt and Thomas, *The Pragmatic Programmer*, xviii.

In my experience, the use of principles is a two-way street. First, principles are helpful for a beginner as they deductively apply general principles to solve specific problems. Next, as you gain experience and have examples of your own, you are able to inductively formulate new principles. This process reinforces a cycle of continuous learning.

In the spirit of participating in this continuous learning, I reproduced the 70 tips from Hunt and Thomas below. For ones that I find particularly interesting, I added some notes on how I have used this principle in my own programming. This offers a nice look back and a view of much I have yet to learn.

---

**Tip 1: Care About Your Craft**: Why spend your life developing software unless you care about doing it well?

**Tip 2: Think! About Your Work**: Turn off the autopilot and take control. Constantly critique and appraise your work.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*This is the fun part of programming! It is helpful to build software that gets a job done. It is beautiful to build software that does it in an elegant way.*

**Tip 3: Provide Options, Don't Make Lame Excuses**: Instead of excuses, provide options. Don't say it can't be done; explain what can be done.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*I'm still waiting for a license to proprietary software. After a couple of months of waiting I decided to write the basic functionality I needed in [open source] Python, and I haven't looked back.*

**Tip 4: Don't Live with Broken Windows**: Fix bad designs, wrong decisions, and poor code when you see them.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Similar to the concept of continual learning is that of continuous improvement. Organizations and systems will not get better over time unless you continually invest in making them so.*

**Tip 5: Be a Catalyst for Change**: You can't force change on people. Instead, show them how the future might be and help them participate in creating it.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Many of the projects I have enjoyed the most started out as a side project because I thought it could be useful at work. It had to start as a side project motivated by self-learning because there was no support to pursue it. But once you **show** them what is possible, people will frequently support your ideas, espeically if you do it in a way that makes them feel like it was somehow their idea.*

**Tip 6: Remember the Big Picture**: Don't get so engrossed in the details that you forget to check what's happening around you.

**Tip 7: Make Quality a Requirements Issue**: Involve your users in determining the project's real quality requirements.

**Tip 8: Invest Regularly in Your Knowledge Portfolio**: Make learning a habit.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Yes. See [here](http://matthewkudija.com/reading).*

**Tip 9: Critically Analyze What You Read and Hear**: Don't be swayed by vendors, media hype, or dogma. Analyze information in terms of you and your project.

**Tip 10: It's Both What You Say and the Way You Say It**: There's no point in having great ideas if you don't communicate them effectively.

**Tip 11: DRY – Don't Repeat Yourself**: Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

**Tip 12: Make It Easy to Reuse**: If it's easy to reuse, people will. Create an environment that supports reuse.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*A great way to make code easy to reuse in Jupyter Notebooks is with the [Snippets Menu](https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/snippets_menu) extension.[^snippets] This comes with frequently used code for a number of popular libraries built in, and you can customize with your own frequently used code. I customized mine with code to import and filter frequently used data.*

[^snippets]: I came across this in Jakub Czakon's excellent talk [10 things you really should know about jupyter notebooks](https://youtu.be/FwUcJFSAfQw).

**Tip 13: Eliminate Effects Between Unrelated Things**: Design components that are self-contained. independent, and have a single, well-defined purpose.

**Tip 14: There Are No Final Decisions**: No decision is cast in stone. Instead, consider each as being written in the sand at the beach, and plan for change.

**Tip 15: Use Tracer Bullets to Find the Target**: Tracer bullets let you home in on your target by trying things and seeing how close they land.

**Tip 16: Prototype to Learn**: Prototyping is a learning experience. Its value lies not in the code you produce, but in the lessons you learn.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Of couse you can often learn just as much—if not more—from failure than from success. But first you need to build something to succeed or fail. So instead of just talking about ideas, implement them and see what you learn. Then roll that learning into the next attempt. With enough prototypes you will build something useful and come away from the experience knowing more than you did when you started.*

**Tip 17: Program Close to the Problem Domain**: Design and code in your user's language.

**Tip 18: Estimate to Avoid Surprises**: Estimate before you start. You'll spot potential problems up front.

**Tip 19: Iterate the Schedule with the Code**: Use experience you gain as you implement to refine the project time scales.

**Tip 20: Keep Knowledge in Plain Text**: Plain text won't become obsolete. It helps leverage your work and simplifies debugging and testing.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*This is one of the reasons I use [xlwings](https://www.xlwings.org/) instead of VBA for automatically interacting with Excel worksheets. In addition to just being more powerful and easier to use, Python code using xlwings is plain text that is lightweight and easily version controlled outisde of the Excel file (see Tip 23).*

**Tip 21: Use the Power of Command Shells**: Use the shell when graphical user interfaces don't cut it.

**Tip 22: Use a Single Editor Well**: The editor should be an extension of your hand; make sure your editor is configurable, extensible, and programmable.

**Tip 23: Always Use Source Code Control**: Source code control is a time machine for your work – you can go back.

**Tip 24: Fix the Problem, Not the Blame**: It doesn't really matter whether the bug is your fault or someone else's – it is still your problem, and it still needs to be fixed.

**Tip 25: Don't Panic When Debugging**: Take a deep breath and THINK! about what could be causing the bug.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The panic for me often sets in late in the afternoon after several hours of spinning my wheels and being confused. If not critical (it rarely is), the best strategy I have found is to set it aside, review the problem just before bed to let me subconscious chew on it overnight, get a good rest, and make solving that issue the first priority in the morning.*

**Tip 26: "select" Isn't Broken.**: It is rare to find a bug in the OS or the compiler, or even a third-party product or library. The bug is most likely in the application.

**Tip 27: Don't Assume It – Prove It**: Prove your assumptions in the actual environment – with real data and boundary conditions.

**Tip 28: Learn a Text Manipulation Language.**: You spend a large part of each day working with text. Why not have the computer do some of it for you?

**Tip 29: Write Code That Writes Code**: Code generators increase your productivity and help avoid duplication.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Code generation is wonderful. The code that produced this webpage was automatically generated from a markdown file I am writing. Just like any other mental work process, programming has parts of it that are repetative and tedious. Automate these and focus on the more intersting things.*

**Tip 30: You Can't Write Perfect Software**: Software can't be perfect. Protect your code and users from the inevitable errors.

**Tip 31: Design with Contracts**: Use contracts to document and verify that code does no more and no less than it claims to do.

**Tip 32: Crash Early**: A dead program normally does a lot less damage than a crippled one.

**Tip 33: Use Assertions to Prevent the Impossible**: Assertions validate your assumptions. Use them to protect your code from an uncertain world.

**Tip 34: Use Exceptions for Exceptional Problems**: Exceptions can suffer from all the readability and maintainability problems of classic spaghetti code. Reserve exceptions for exceptional things.

**Tip 35: Finish What You Start**: Where possible, the routine or object that allocates a resource should be responsible for deallocating it.

**Tip 36: Minimize Coupling Between Modules**: Avoid coupling by writing "shy" code and applying the Law of Demeter.

**Tip 37: Configure, Don't Integrate**: Implement technology choices for an application as configuration options, not through integration or engineering.

**Tip 38: Put Abstractions in Code, Details in Metadata**: Program for the general case, and put the specifics outside the compiled code base.

**Tip 39: Analyze Workflow to Improve Concurrency**: Exploit concurrency in your user's workflow.

**Tip 40: Design Using Services**: Design in terms of services – independent, concurrent objects behind well-defined, consistent interfaces.

**Tip 41: Always Design for Concurrency**: Allow for concurrency, and you'll design cleaner interfaces with fewer assumptions.

**Tip 42: Separate Views from Models**: Gain flexibility at low cost by designing your application in terms of models and views.

**Tip 43: Use Blackboards to Coordinate Workflow**: Use blackboards to coordinate disparate facts and agents, while maintaining independence and isolation among participants.

**Tip 44: Don't Program by Coincidence**: Rely only on reliable things. Beware of accidental complexity, and don't confuse a happy coincidence with a purposeful plan.

**Tip 45: Estimate the Order of Your Algorithms**: Get a feel for how long things are likely to take before you write code.

**Tip 46: Test Your Estimates**: Mathematical analysis of algorithms doesn't tell you everything. Try timing your code in its target environment.

**Tip 47: Refactor Early, Refactor Often**: Just as you might weed and rearrange a garden, rewrite, rework, and re-architect code when it needs it. Fix the root of the problem.

**Tip 48: Design to Test**: Start thinking about testing before you write a line of code.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*This is where I really need to improve (as well as Tips 49, 62, and 63). The next step to mature my code is to be much better at testing, completely and automatically.*

**Tip 49: Test Your Software, or Your Users Will**: Test ruthlessly. Don't make your users find bugs for you.

**Tip 50: Don't Use Wizard Code You Don't Understand**: Wizards can generate reams of code. Make sure you understand all of it before you incorporate it into your project.

**Tip 51: Don't Gather Requirements – Dig for Them**: Requirements rarely lie on the surface. They're buried deep beneath layers of assumptions, misconceptions, and politics.

**Tip 52: Work With a User to Think Like a User**: It's the best way to gain insight into how the system will really be used.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Most of the code I write is for myself, at least initially, so this comes naturally. I am the user. However, most users other than myself withing the organization I work for do not program. The process of thinking like those users is helpful for simplifying and streamlining code I have written to move it from personal use to organizational use.*

**Tip 53: Abstractions Live Longer than Details**: Invest in the abstraction, not the implementation. Abstractions can survive the barrage of changes from different implementations and new technologies.

**Tip 54: Use a Project Glossary**: Create and maintain a single source of all the specific terms and vocabulary for a project.

**Tip 55: Don't Think Outside the Box – Find the Box**: When faced with an impossible problem, identify the real constraints. Ask yourself: "Does it have to be done this way? Does it have to be done at all?"

**Tip 56: Start When You're Ready.**: You've been building experience all your life. Don't ignore niggling doubts.

**Tip 57: Some Things Are Better Done than Described**: Don't fall into the specification spiral – at some point you need to start coding.

**Tip 58: Don't Be a Slave to Formal Methods.**: Don't blindly adopt any technique without putting it into the context of your development practices and capabilities.

**Tip 59: Costly Tools Don't Produce Better Designs**: Beware of vendor hype, industry dogma, and the aura of the price tag. Judge tools on their merits.

**Tip 60: Organize Teams Around Functionality**: Don't separate designers from coders, testers from data modelers. Build teams the way you build code.

**Tip 61: Don't Use Manual Procedures**: A shell script or batch file will execute the same instructions, in the same order, time after time.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*I use Python scripts scheduled with [cron](https://github.com/mkudija/General-Examples/blob/master/cron.md) to perform many manual functions, such as moving data around, writing to logs, etc. Saving time is great. But being guranteed that the computer will do exactly what you want it to without making mistakes and without getting tired is even more valuable. This frees you up to add value in more powerful ways.*

**Tip 62: Test Early. Test Often. Test Automatically**: Tests that run with every build are much more effective than test plans
that sit on a shelf.

**Tip 63: Coding Ain't Done 'Til All the Tests Run**: 'Nuff said.

**Tip 64: Use Saboteurs to Test Your Testing**: Introduce bugs on purpose in a separate copy of the source to verify that testing will catch them.

**Tip 65: Test State Coverage, Not Code Coverage**: Identify and test significant program states. Just testing lines of code isn't enough.

**Tip 66: Find Bugs Once**: Once a human tester finds a bug, it should be the last time a human tester finds that bug. Automatic tests should check for it from then on.

**Tip 67: English is Just a Programming Language**: Write documents as you would write code: honor the DRY principle, use metadata, MVC, automatic generation, and so on.

**Tip 68: Build Documentation In, Don't Bolt It On**: Documentation created separately from code is less likely to be correct and up to date.

**Tip 69: Gently Exceed Your Users' Expectations**: Come to understand your users' expectations, then deliver just that little bit more.

**Tip 70: Sign Your Work**: Craftsmen of an earlier age were proud to sign their work. You should be, too.

>For more information about The Pragmatic Programmers LLC, source code for the examples, up-to-date pointers to Web resources, and an online bibiography, visit us at www.pragmaticprogrammer.com

* Preface
    * What makes a pragmatic programmer?
        * Early adopter/fast adapter
        * Inquisitive
        * Critical thinker
        * Realistic
        * Jack of all trades
    * Most important tips
        * Care about your craft 
        * Think about your work
    * "Those who cut mere stones must always be envisioning cathedrals." -quarry workers creed

---
Created: 2021-03-06
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD") %>

