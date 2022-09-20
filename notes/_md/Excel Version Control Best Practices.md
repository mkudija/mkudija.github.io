---
publish: true
---

# Excel Version Control Best Practices

This document presents best practices for manually managing versions of Excel documents. This applies equally well to any file type, but Excel models are where I have seen this be an issue for teams that manually manage versions rather than using [Git](https://en.wikipedia.org/wiki/Git) or another version control system.

The three key principles for manually managing file versions are:
1. Frequently save versions using a standard file name format
2. Maintain a change log that maps file changes to file names
3. Maintain a milestone log that maps file names to milestones 
	
Principle #1 is—in my experience—the basic requirement for maintaining an organized manual version control system. #2 and #3 provide all needed context while allowing you to adhere to #1.


## 1. Frequently save versions using a standard file name format
All versions of a file should be saved with the same file name format in a single directory. I recommend one of the following formats:




| Format             | Example                                                                                              | Notes                                                             |
| ------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Name_vVV           | `Budget_v01`<br>`Budget_v02`<br>`Budget_v03`<br>...<br>`Budget_v15`                                             | Name and version only                                             |
| YYYY-MM-DD-VV_Name | `2021-12-10-01_Budget`<br>`2021-12-10-02_Budget`<br>`2021-12-10-03_Budget`<br>...<br>`2021-12-11-01_Budget` | Date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format |

Choose a format that works for you, but maintain the discipline of a consistent format. Save information about the contents of the file for #2. Once a version is saved, you should *never* change the contents of that file.

How frequently should you save versions? 

I always err on the side of saving versions *more* frequently rather than *less* frequently. The costs associated with saving too many versions come primarily in the form of disk space and are *much* less than the costs of not saving enough versions which in the best case scenario is your wasted time to recover from an error and in the worst case data that is completely irrecoverable.

Typically, I save a new version if any one of the following conditions are met:
- The update causes a material change in the outputs
- The version has been sent to anyone other than myself
- I have spend more than *n* minutes working since saving a new version, where *n* is the amount of time you are willing to lose by not saving a new version. For me this is typically 10-60 minutes.

When you inevitably make a mistake that breaks your file, or when you need to build a walk of changes from one state to another state, you will be glad you saved multiple versions.


## 2. Maintain a change log that maps file changes to file names
Now that you have an orderly list of named versions, you need a way to identify what changed in each version. This information belongs in a change log (not the file name), which can be as simple as this:

| Version      | Author | Notes                        |
| ------------ | ------ | ---------------------------- |
| `Budget_v01` | MK     | Initial version              |
| `Budget_v02` | MK     | Loaded fixed expenses        |
| `Budget_v03` | JK     | Updated revenue              |
| `Budget_v04` | MK     | Added headcount              |
| ...          | ...    | ...                          |
| `Budget_v15` | AM     | Fixed error in interest calc |

I typically add a `changelog` sheet to my workbook to keep the information all contained in one file, but you can also split this out if desired, which can be helpful for large files.

Change log notes can range from simple to detailed, and I find it helpful to give both summary context and detailed information. The summary is helpful for identifying a particular change when looking back over many versions, and the details are helpful for identifying exactly what changed in a particular version.
- **Simple**: "Updated revenue"
- **Detailed**: "`Calcs` tab: update formula in `BC123` to account for monthly seasonality"
- **Detailed with summary**: "Updated revenue: `Calcs` tab: update formula in `BC123` to account for monthly seasonality"


## 3. Maintain a milestone log that maps file names to milestones 
Now that you have an orderly list of named versions and a change log that identifies what changed in each version, you need a way to identify which versions correspond to important milestones. A milestone table eliminates the possibility of creating awful file names like `_FINALv2`, `_FINALv2_updated`.[^linkedin] 

[^linkedin]: As an aside, some colorful and inconsistent examples I have seen, edited for anonymity where appropriate, include: <br> • The classic [vFinal, vFinal2, etc.](https://www.linkedin.com/posts/mattbrattin_versioncontrol-analytics-excel-activity-6828746722647384064-qCAl), and [again](https://www.linkedin.com/posts/mattbrattin_excel-data-analytics-activity-6971085557951053824-id-w) <br> • Starting with a consistent naming format and then adding extra note(s) or version(s) in the filename rather than in the change log: `2018-02-25-11-Example Model vEquity v13_downside + Growth v10.xlsx` <br> • Saving versions in a crazy nested directory structure like this: `Model\2020 Plan\New Years Updates\12&0 Update\Post 1.15.20 Touch Base\2020 Plan V6 (1.22).xlsm` <br> 

| Milestone          | Version      | Notes                            |
| ------------------ | ------------ | -------------------------------- |
| 21Q4 Board Meeting | `Budget_v02` | Presented 2021-12-05, *[deck]()* |
| Debt Version       | `Budget_v07` | Shared with XYX Bank 2021-12-10  |
| 22Q1 Board Meeting | `Budget_v14` | Presented 2022-03-05, *[deck]()* |

Now, you know for all time that you presented version `Budget_v14` at the 22Q1 Board meeting. If the morning of the meeting you need to make changes, you simple save a version `Budget_v15` and note in your milestones table that this is now final Board version. 

A table like this provides the bare minimum information of the milestone, version, and some notes. It can also be helpful to have more lengthy notes that describe in detail the inputs, assumptions, and outputs of the version assigned to a particular milestone.

If you adhere to the system of consistently naming files, maintaining a change log, and maintaining a milestones table, you will significantly reduce the risk of data loss and increase your ability to answer questions about your work.


	
## Special Case: Branching
Some changes are *so* big that you need to deviate from #1 above and branch off your changes into a new directory. This situation is much rarer than you think and can cause significant errors should you need to merge the branch back to master. But if it is essential, I recommend branching in this manner:
- Within your current `Budget/` directory, create the branch directory such as `Budget/Budget_branch/`
- Copy the latest file version from the master directory into the branch directory, i.e. copy `Budget/Budget_v15.xlsx` to `Budget/Budget_branch/Budget_v15.xlsx`
- Follow principles #1, #2, and #3 as above with your files in your `Budget_branch/` directory
- If you merge the branch back into your master directory, perform and follow principles #1, #2, and #3 above, i.e. save-as `Budget/Budget_branch/Budget_v18.xlsx` to `Budget/Budget_v16.xlsx`, and note in your change log that you saved from the branch location

Again, you probably do not need to save a branch, but just need to follow principles #1, #2, and #3 above with discipline. 

One example that may tempt you to branch when you don't need to is running **scenarios**. Say you want to sensitize the impact of $100M, $110M, and $120M of marketing spend. If you have read this far you may be tempted to make branches `Budget/Budget_100M/`, `Budget/Budget_110M/`, and `Budget/Budget_120M/` (if you haven't read this you might save versions `Budget_v2_100M.xlsx`, `Budget_v2_110M.xlsx`, and `Budget_v2_110M.xlsx`). Instead of these, simply make an `Outputs/` folder and save the outputs only there without changing your model versions.

One example that may make sense for saving a branch is a static adjustment that will never change. Say you have a baseline model for setting guidance and then you want to save a "high" and "low" version of this. Then it may make sense to create a `Budget/2022_Guidance/` directory and save these two versions there.

```bash
└── Budget
    ├── Inputs
    ├── Model
    │   ├── Budget_branch
    │   │   ├── Budget_v15.xlsx
    │   │   ├── Budget_v16.xlsx
    │   │   └── Budget_v17.xlsx
    │   ├── 2022_Guadance
    │   │   ├── Budget_v18_low.xlsx
    │   │   └── Budget_v18_high.xlsx
    │   ├── Budget_v01.xlsx
    │   ├── Budget_v02.xlsx
    │   ├── Budget_v03.xlsx
    │   ├── Budget_v04.xlsx
    │   ├── ...
    │   ├── Budget_v15.xlsx
    │   └── Budget_v16.xlsx
    └── Outputs
        ├── Budget_v02_100M.pdf
        ├── Budget_v02_110M.pdf
        └── Budget_v02_120M.pdf
```


## Conclusion
This is but one of many systems that could work work to manually manage version control of important files. What matters more than the particular details of the system is having the discipline to pick a system and stick to it. Your future self will thank you.


---
Created: 2021-08-19
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD") %>
