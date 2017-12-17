I need to start a discussion of *The Pragmatic Programmer: From Journeyman to Master* by Andrew Hunt and David Thomas by acknowledging that I'm not a programmer, at least not formally. My job title is not Software Engineer, nor do I have a degree in computer science. However, I did learn basic programming in Fortran and Matlab while studying aerospace engineering, and I have taught myself Python and used it over the past several years both for analysis and to automate basic business tasks. So, while I do not write software at the level that could fully benefit from this book, I found much of the advice contained therein to be helpful.

The two aspects of Hunt and Thomas' work I found the most helpful are the development of a set of guiding principles and the focus on developing a well-rounded generalism with a mindset of continual education.

I'll start with the attitude of generalism they advise. Hunt and Thomas suggest that a pragmatic programmer is more of a jack of all trades than a specialist, able to adapt to a continually changing technology landscape with broad skills and continuous learning. As a pragmatic programmer you should "try hard to be familiar with a broad range of technologies and environments, and you work to keep abreast of new developments."[^jack] Tip number 8 they advise is to make learning a habit by investing regularly in your knowlege portfolio. Not only does continual learning keep you fresh and competitive, it is the more interesting way to approach your work.

This mindset of continually learning well-rounded generalism leads into the principles, or "Tips", they expound. The principles are the framewok from which you can address particular situations. "You shouldn't be wedded to any particular technology, but have a broad enough background and experience base to allow you to choose good solutions in particular situations. Your background stems from an understanding of the basic principles of computer science, and your experience comes from a wide range of practical projects. Theory and practice combine to make you strong."[^principles] 

[^jack]: *The Pragmatic Programmer: From Journeyman to Master* by Andrew Hunt and David Thomas, xix.
[^principles]: *The Pragmatic Programmer: From Journeyman to Master* by Andrew Hunt and David Thomas, xviii.

*more quotes about generalism from Evernote?*

As I mentioned, *The Pragmatic Programmer* has been helpful to my work to bring basic automation to business processes. A prerequisite for automating anything is well-formatted data, for which I recommend both [Data organization in spreadsheets](http://www.tandfonline.com/doi/full/10.1080/00031305.2017.1375989) by Karl W. Broman and Kara H. Woo, and [Tidy Data](http://www.stat.wvu.edu/~jharner/courses/stat623/docs/tidy-dataJSS.pdf) by Hadley Wickham.

Broman and Woo give a number of helpful suggestions for working with Excel. For better or for worse, Excel is a staple of life in most business settings, even in situations where it should not be. Acknowledging both that Excel is often not ideal, but also that it will not be fully replaed without extensive workforce retraining, our goal becomes how to interface with Excel intelligently. Others may insist on using Excel, but if formatted properly *you* never need to use Excel directly, but rather just read and write data to Excel files while running your analysis and visualization in Python, R or another language. Some of the tips recommended by Broman and Woo include separating analysis and visualization of data, being consistent, and using [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (`YYYY-MM-DD`) date formats. I firmly agree with their recommendation that "data rearrangement is best accomplished via code (such as with an R, Python, or Ruby script) so you never lose the record of what you did to the data."[^spreadsheets] The one recommendation of theirs that I disagree with is the suggestion to leave no cells empty and fill all with "NA" or "-". I recommend leaving cells blank, since the filler is one more item that must be tracked and is an opportuinty for data errors. Also, when working in Python, the [`pandas.DataFrame.fillna()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html) method can be called immediatly after loading data from Excel to consistently fill all empty cells. This is just a matter of preference, however, and I strongly recommend adherence to the principles they give.

[^spreadsheets]: [Data organization in spreadsheets](http://www.tandfonline.com/doi/full/10.1080/00031305.2017.1375989) by Karl W. Broman and Kara H. Woo

Hadley Wickham's Tidy Data principles are a good guide for formatting data, whether in Excel or other storage format:
1. Each variable forms a column.
2. Each observation forms a row.
3. Each type of observational unit forms a table.[^tidy]

[^tidy]: pg 4
 

and [Principles] by Ray Dalio?


- generalism instead of specialization, with emphasis on learning
- I'm not a programmer, but this is how I've used it in my work to introduce basic automation in a business environment
- principles-based approach
-- reference Principles
-- also reference spreadsheets and Tidy Data
- review my reflections on these principles
 
Ref
- [PDF of book](http://210.240.189.214/gamedesign/type_exercise/00_9615_reference//5.%E5%AD%B8%E7%BF%92%E6%88%90%E6%9E%9C%E5%8F%83%E8%80%83/23/books/1999%20-%20The%20Pragmatic%20Programmer;%20From%20Journeyman%20To%20Master%20-%20Pearson%20Education.pdf)
- [Hugo Matilla Notes](https://github.com/HugoMatilla/The-Pragmatic-Programmer)

 

The Zen of Python
```python
In [1]: import this
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Best tips:
1. care
2. think
4. broken windows
5. show them the future
6. big picture
8. knowledge
10. also how you say it --> connect to authentic leadership
11. DRY
12. make it easy to reuse
16. prototype to learn: excel fleet view to html fleet view to ???
20. keep knowledge in plain text
23. source control
**Tip 24: Fix the Problem, Not the Blame** 
It doesn't really matter whether the bug is your fault or someone else's – it is still your problem, and it still needs to be fixed.
**Tip 25: Don't Panic When Debugging** 
Take a deep breath and THINK! about what could be causing the bug.
29. write code that writes code
**Tip 47: Refactor Early, Refactor Often** 
Just as you might weed and rearrange a garden, rewrite, rework, and re-architect code when it needs it. Fix the root of the problem.
**Tip 48: Design to Test** 
Start thinking about testing before you write a line of code.
**Tip 49: Test Your Software, or Your Users Will** 
Test ruthlessly. Don't make your users find bugs for you.
**Tip 50: Don't Use Wizard Code You Don't Understand** 
Wizards can generate reams of code. Make sure you understand all of it before you incorporate it into your project.
**Tip 51: Don't Gather Requirements – Dig for Them** 
Requirements rarely lie on the surface. They're buried deep beneath layers of assumptions, misconceptions, and politics.
**Tip 52: Work With a User to Think Like a User** 
It's the best way to gain insight into how the system will really be used.
**Tip 61: Don't Use Manual Procedures** 
A shell script or batch file will execute the same instructions, in the same order, time after time.
**Tip 62: Test Early. Test Often. Test Automatically** 
Tests that run with every build are much more effective than test plans that sit on a shelf.
**Tip 63: Coding Ain't Done 'Til All the Tests Run** 
'Nuff said.
**Tip 69: Gently Exceed Your Users' Expectations** 
Come to understand your users' expectations, then deliver just that little bit more.
**Tip 70: Sign Your Work** 
Craftsmen of an earlier age were proud to sign their work. You should be, too.


>For more information about The Pragmatic Programmers LLC, source code for the examples, up-to-date pointers to Web resources, and an online bibiography, visit us at www.pragmaticprogrammer.com

## Tips

**Tip 1: Care About Your Craft** 
Why spend your life developing software unless you care about doing it well?

**Tip 2: Think! About Your Work** 
Turn off the autopilot and take control. Constantly critique and appraise your work.

**Tip 3: Provide Options, Don't Make Lame Excuses** 
Instead of excuses, provide options. Don't say it can't be done; explain what can be done.

**Tip 4: Don't Live with Broken Windows** 
Fix bad designs, wrong decisions, and poor code when you see them.

**Tip 5: Be a Catalyst for Change** 
You can't force change on people. Instead, show them how the future might be and help them participate in creating it.

**Tip 6: Remember the Big Picture** 
Don't get so engrossed in the details that you forget to check what's happening around you.

**Tip 7: Make Quality a Requirements Issue** 
Involve your users in determining the project's real quality requirements.

**Tip 8: Invest Regularly in Your Knowledge Portfolio** 
Make learning a habit.

**Tip 9: Critically Analyze What You Read and Hear** 
Don't be swayed by vendors, media hype, or dogma. Analyze information in terms of you and your project.

**Tip 10: It's Both What You Say and the Way You Say It** 
There's no point in having great ideas if you don't communicate them effectively.

**Tip 11: DRY – Don't Repeat Yourself** 
Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

**Tip 12: Make It Easy to Reuse** 
If it's easy to reuse, people will. Create an environment that supports reuse.

**Tip 13: Eliminate Effects Between Unrelated Things** 
Design components that are self-contained. independent, and have a single, well-defined purpose.

**Tip 14: There Are No Final Decisions** 
No decision is cast in stone. Instead, consider each as being written in the sand at the beach, and plan for change.

**Tip 15: Use Tracer Bullets to Find the Target** 
Tracer bullets let you home in on your target by trying things and seeing how close they land.

**Tip 16: Prototype to Learn** 
Prototyping is a learning experience. Its value lies not in the code you produce, but in the lessons you learn.

**Tip 17: Program Close to the Problem Domain**
Design and code in your user's language.

**Tip 18: Estimate to Avoid Surprises** 
Estimate before you start. You'll spot potential problems up front.

**Tip 19: Iterate the Schedule with the Code** 
Use experience you gain as you implement to refine the project time scales.

**Tip 20: Keep Knowledge in Plain Text** 
Plain text won't become obsolete. It helps leverage your work and simplifies debugging and testing.

**Tip 21: Use the Power of Command Shells**
Use the shell when graphical user interfaces don't cut it.

**Tip 22: Use a Single Editor Well**
The editor should be an extension of your hand; make sure your editor is configurable, extensible, and programmable.

**Tip 23: Always Use Source Code Control** 
Source code control is a time machine for your work – you can go back.

**Tip 24: Fix the Problem, Not the Blame**
It doesn't really matter whether the bug is your fault or someone else's – it is still your problem, and it still needs to be fixed.

**Tip 25: Don't Panic When Debugging** 
Take a deep breath and THINK! about what could be causing the bug.

**Tip 26: "select" Isn't Broken.** 
It is rare to find a bug in the OS or the compiler, or even a third-party product or library. The bug is most likely in the application.

**Tip 27: Don't Assume It – Prove It** 
Prove your assumptions in the actual environment – with real data and boundary conditions.

**Tip 28: Learn a Text Manipulation Language.** 
You spend a large part of each day working with text. Why not have the computer do some of it for you?

**Tip 29: Write Code That Writes Code** 
Code generators increase your productivity and help avoid duplication.

**Tip 30: You Can't Write Perfect Software** 
Software can't be perfect. Protect your code and users from the inevitable errors.

**Tip 31: Design with Contracts** 
Use contracts to document and verify that code does no more and no less than it claims to do.

**Tip 32: Crash Early** 
A dead program normally does a lot less damage than a crippled one.

**Tip 33: Use Assertions to Prevent the Impossible** 
Assertions validate your assumptions. Use them to protect your code from an uncertain world.

**Tip 34: Use Exceptions for Exceptional Problems**
Exceptions can suffer from all the readability and maintainability problems of classic spaghetti code. Reserve exceptions for exceptional things.

**Tip 35: Finish What You Start** 
Where possible, the routine or object that allocates a resource should be responsible for deallocating it.

**Tip 36: Minimize Coupling Between Modules** 
Avoid coupling by writing "shy" code and applying the Law of Demeter.

**Tip 37: Configure, Don't Integrate**
Implement technology choices for an application as configuration options, not through integration or engineering.

**Tip 38: Put Abstractions in Code, Details in Metadata** 
Program for the general case, and put the specifics outside the compiled code base.

**Tip 39: Analyze Workflow to Improve Concurrency** 
Exploit concurrency in your user's workflow.

**Tip 40: Design Using Services** 
Design in terms of services – independent, concurrent objects behind well-defined, consistent interfaces.

**Tip 41: Always Design for Concurrency** 
Allow for concurrency, and you'll design cleaner interfaces with fewer assumptions.

**Tip 42: Separate Views from Models** 
Gain flexibility at low cost by designing your application in terms of models and views.

**Tip 43: Use Blackboards to Coordinate Workflow** 
Use blackboards to coordinate disparate facts and agents, while maintaining independence and isolation among participants.

**Tip 44: Don't Program by Coincidence** 
Rely only on reliable things. Beware of accidental complexity, and don't confuse a happy coincidence with a purposeful plan.

**Tip 45: Estimate the Order of Your Algorithms** 
Get a feel for how long things are likely to take before you write code.

**Tip 46: Test Your Estimates** 
Mathematical analysis of algorithms doesn't tell you everything. Try timing your code in its target environment.

**Tip 47: Refactor Early, Refactor Often** 
Just as you might weed and rearrange a garden, rewrite, rework, and re-architect code when it needs it. Fix the root of the problem.

**Tip 48: Design to Test** 
Start thinking about testing before you write a line of code.

**Tip 49: Test Your Software, or Your Users Will** 
Test ruthlessly. Don't make your users find bugs for you.

**Tip 50: Don't Use Wizard Code You Don't Understand**
Wizards can generate reams of code. Make sure you understand all of it before you incorporate it into your project.

**Tip 51: Don't Gather Requirements – Dig for Them** 
Requirements rarely lie on the surface. They're buried deep beneath layers of assumptions, misconceptions, and politics.

**Tip 52: Work With a User to Think Like a User** 
It's the best way to gain insight into how the system will really be used.

**Tip 53: Abstractions Live Longer than Details** 
Invest in the abstraction, not the implementation. Abstractions can survive the barrage of changes from different implementations and new technologies.

**Tip 54: Use a Project Glossary**
Create and maintain a single source of all the specific terms and vocabulary for a project.

**Tip 55: Don't Think Outside the Box – Find the Box** 
When faced with an impossible problem, identify the real constraints. Ask yourself: "Does it have to be done this way? Does it have to be done at all?"

**Tip 56: Start When You're Ready.**
You've been building experience all your life. Don't ignore niggling doubts.

**Tip 57: Some Things Are Better Done than Described** 
Don't fall into the specification spiral – at some point you need to start coding.

**Tip 58: Don't Be a Slave to Formal Methods.**
Don't blindly adopt any technique without putting it into the context of your development practices and capabilities.

**Tip 59: Costly Tools Don't Produce Better Designs** 
Beware of vendor hype, industry dogma, and the aura of the price tag. Judge tools on their merits.

**Tip 60: Organize Teams Around Functionality** 
Don't separate designers from coders, testers from data modelers. Build teams the way you build code.

**Tip 61: Don't Use Manual Procedures** 
A shell script or batch file will execute the same instructions, in the same order, time after time.

**Tip 62: Test Early. Test Often. Test Automatically**Tests that run with every build are much more effective than test plans that sit on a shelf.

**Tip 63: Coding Ain't Done 'Til All the Tests Run**
'Nuff said.

**Tip 64: Use Saboteurs to Test Your Testing** 
Introduce bugs on purpose in a separate copy of the source to verify that testing will catch them.

**Tip 65: Test State Coverage, Not Code Coverage** 
Identify and test significant program states. Just testing lines of code isn't enough.

**Tip 66: Find Bugs Once** 
Once a human tester finds a bug, it should be the last time a human tester finds that bug. Automatic tests should check for it from then on.

**Tip 67: English is Just a Programming Language** 
Write documents as you would write code: honor the DRY principle, use metadata, MVC, automatic generation, and so on.

**Tip 68: Build Documentation In, Don't Bolt It On** 
Documentation created separately from code is less likely to be correct and up to date.

**Tip 69: Gently Exceed Your Users' Expectations** 
Come to understand your users' expectations, then deliver just that little bit more.

**Tip 70: Sign Your Work** 
Craftsmen of an earlier age were proud to sign their work. You should be, too.