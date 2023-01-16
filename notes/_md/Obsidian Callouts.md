---
publish: true
---

# [[Obsidian]] Callouts

Obsidian-themed callouts (also known as alerts or admonitions).

### Note
**Rendered**
<div class="note">
	<p>Here is an alert</p>
</div>

**HTML**
```html
<div class="note">
	<p>Here is an alert</p>
</div>
```

**Espanso**
```shell
	- trigger: ";note"
	replace: "<div class=\"note\">
	  <p>$|$</p>
	</div>
	"
```


### Info
**Rendered**
<div class="info">
	<p>Here is an alert</p>
</div>

**HTML**
```html
<div class="info">
	<p>Here is an alert</p>
</div>
```

**Espanso**
```shell
	- trigger: ";info"
	replace: "<div class=\"info\">
	  <p>$|$</p>
	</div>
	"
```


### Warning
**Rendered**
<div class="warning">
	<p>Here is an alert</p>
</div>

**HTML**
```html
<div class="warning">
	<p>Here is an alert</p>
</div>
```

**Espanso**
```shell
	- trigger: ";warn"
	replace: "<div class=\"warning\">
	  <p>$|$</p>
	</div>
	"
```

### Error
**Rendered**
<div class="error">
	<p>Here is an alert</p>
</div>

**HTML**
```html
<div class="error">
	<p>Here is an alert</p>
</div>
```

**Espanso**
```shell
	- trigger: ";err"
	replace: "<div class=\"error\">
	  <p>$|$</p>
	</div>
	"
```


### Success 
**Rendered**
<div class="success">
	<p>Here is an alert</p>
</div>

**HTML**
```html
<div class="success">
	<p>Here is an alert</p>
</div>
```

**Espanso**
```shell
	- trigger: ";suc"
	replace: "<div class=\"success\">
	  <p>$|$</p>
	</div>
	"
```




### CSS
Add this CSS to your Obsidian [CSS Snippets](https://help.obsidian.md/How+to/Add+custom+styles):

```css
/*Bootstrap style alerts: */
.note, .info, .success, .warning, .error {
margin: 10px 0px;
padding:12px;
 
}
.note {
    color: #63666a;
    background-color: #whitesmoke;
    border-radius: 4px;
    border: .5px solid #63666a;
}
.info {
    color: #00529B;
    background-color: #BDE5F8;
    border-radius: 4px;
    border: .5px solid #00529B;
}
.success {
    color: #4F8A10;
    background-color: #DFF2BF;
    border-radius: 4px;
    border: .5px solid #4F8A10;
}
.warning {
    color: #9F6000;
    background-color: #FEEFB3;
    border-radius: 4px;
    border: .5px solid #9F6000;
}
.error {
    color: #D8000C;
    background-color: #FFD2D2;
    border-radius: 4px;
    border: .5px solid #D8000C;
}
.info i, .success i, .warning i, .error i {
    margin:15px 22px;
    font-size:2em;
    vertical-align:middle;
}
```


---


## Survey
*A quick survey of some callout / alert styles. Note: images may not render on published version.*

### Obsidian (rendered 2023-01-14)
Obsidian will render callouts with this syntax ( [Use callouts - Obsidian Help](https://help.obsidian.md/How+to/Use+callouts)):

```markdown
> [!INFO]
> Here's a callout block.
```

> [!INFO]
> Here's a callout block.

> [!NOTE]
> Here's a callout block.

> [!WARNING]
> Here's a callout block.

> [!DANGER]
> Here's a callout block.

> [!SUCCESS]
> Here's a callout block.

### Obsidian (docs)
*[Link](https://help.obsidian.md/How+to/Use+callouts)*
![[Pasted image 20230114215926.png]]

### Confluence
![[Pasted image 20230114215300.png]]

### Bootstrap v4
*[Link](https://getbootstrap.com/docs/4.0/components/alerts/)*
![[Pasted image 20230114215519.png]]

### Bootstrap v5
*[Link](https://getbootstrap.com/docs/5.0/components/alerts/)*
![[Pasted image 20230114220031.png]]

---
Created: [[2023-01-14-Sat]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>
