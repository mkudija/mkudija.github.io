---
publish: true
---

# Excel Examples

[Example Workbook](https://github.com/mkudija/img/tree/main/excel-examples)

### Data Tables
[Data Table in Excel - Examples, Types, How to Create/Use?](https://www.wallstreetmojo.com/data-table-in-excel/)

### Sumifs with multiple conditions

```
=SUM(SUMIFS(data!$A:$A,data!$T:$T,{"C","N","B"}))
```

### Quarter of Year
```xls
=ROUNDUP(MONTH(B2)/3,0)
=ROUNDUP(MONTH(B2)/3,0)&"Q"&RIGHT(YEAR(B2),2)
```

### Every $n^{th}$ Row
```
=OFFSET($A$1,(ROW()-1)*n,0)
```

---
Created: [[2022-07-13-Wed]]
Updated: `=dateformat(this.file.mtime, "yyyy-MM-dd-ccc")`
