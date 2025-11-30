# Sparck Nodes

## Abbreviations

<!-- md:version 1.0.0 -->
<!-- md:extension [abbr][Abbreviations] -->

The [Abbreviations] extension adds the ability to add a small tooltip to an
element, by wrapping it with an `abbr` tag. Only plain text (no markup) is
supported. Enable it via `mkdocs.yml`:

``` yaml
markdown_extensions:
  - abbr
```


### Admonition

<!-- md:version 0.1.0 -->
<!-- md:extension [admonition][Admonition] -->

The [Admonition] extension adds support for admonitions, more commonly known as
_call-outs_, which can be defined in Markdown by using a simple syntax. Enable
it via `mkdocs.yml`:

``` yaml
markdown_extensions:
  - admonition
```

### Attribute Lists

<!-- md:version 0.1.0 -->
<!-- md:extension [attr_list][Attribute Lists] -->

The [Attribute Lists] extension allows to add HTML attributes and CSS classes
to [almost every][Attribute Lists limitations] Markdown inline- and block-level
element with a special syntax. Enable it via `mkdocs.yml`:

``` yaml
markdown_extensions:
  - attr_list
```
