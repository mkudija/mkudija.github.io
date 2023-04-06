---
publish: true
mermaid: true
---

# [[Bible Translations|Bible Translation]] Chart

```mermaid
graph LR

orig(Original Hebrew / Greek)
kjv(KJV 1611)
rv(Revised Version 1885)
asv(ASV 1901)
rsv(RSV 1952)
rsvce(RSV-CE 1989)
rsv2ce(RSV-2CE 2006)
nrsv(NRSV 1990)
nrsvce(NRSV-CE 1991)
nrsvue(NRSVUE 2022)
nkjv(NKJV 1982)
esv(ESV 2001)
esv16(ESV 2016)
esvce(ESV-CE 2018)
nab(NAB 1970)
nabre(NABRE 2011)
niv(NIV 1978)
v(Vulgate 400)
nv(New Vulgate 1979)
nv86(New Vulgate 1986)
douay(Douay 1610)
challoner(Challoner 1752)
confraternity(Confraternity 1941)
na(NASB 1971)
nas(NASB 1995)
lsb(LSB 2021)
nasb(NASB 2020)
lbj(La Bible de Jérusalem 1956)
jb(JB 1966)
njb(NJB 1985)
alv(ALV 2016) %% https://www.bibliotheca.co/translation

classDef ct fill:lightBlue
classDef pt fill:lightGreen
classDef ec fill:pink

%% subgraph Legend
%%	direction TB
	Catholic>Catholic]:::ct
	Protestant>Protestant]:::pt
	Ecumenical>Ecumenical]:::ec
%%end

orig --> nab:::ct
orig --> v:::ct
orig --> kjv:::pt
orig --> na
orig --> niv:::pt
nab --> nabre:::ct
v --> nv:::ct
v --> douay:::ct
douay --> challoner:::ct
kjv --> challoner
challoner --> confraternity:::ct
confraternity --> nab
nv --> nv86:::ct
kjv --> rv:::pt
kjv --> nkjv:::pt
kjv --> asv:::pt
asv --> rsv:::ec
rsvce --> rsv2ce:::ct
rsv --> nrsv:::ec
nrsv --> nrsvue:::ec
nrsv --> nrsvce:::ct
rsv --> rsvce:::ct
rsv --> esv:::pt
esv --> esvce:::ct
esv --> esv16:::pt
asv --> alv:::ct
asv --> na:::pt
na --> nas:::pt
nas --> nasb:::pt
nas --> lsb:::pt
orig --> jb:::ct
orig --> lbj:::ct
lbj --> jb
jb --> njb:::ct


```

---
Created: [[2023-04-06-Thu]]
Updated: `=dateformat(this.file.mtime, "yyyy-MM-dd-ccc")`
