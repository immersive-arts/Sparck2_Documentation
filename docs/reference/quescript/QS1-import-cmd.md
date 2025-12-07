# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;import&gt;
&lt;import&gt;filepath.que&lt;/import&gt;

### Simple Example

<script>
    <import>another.que</import>
    <que name="xy">
      ...
</script>

### Content
Relative filepath to another que script

### Attributes
* None

### Child Commands
* None

### Explained
The import command will import the specified que script, which it expects to be relative to its own location.

The import command has to be the first command inside the script.

Caveats:

If the imported script also imports scripts, it will try to do so, but it is NOT checking if a circular import will happen. If this is the case, the script will fall into an infinite loop and will not recover.

It also will NOT check if ques ares imported which might have a naming collision with already loaded ques.
