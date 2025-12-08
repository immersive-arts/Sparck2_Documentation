# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / [{expressions}](QS1-expressions.md)/Variables

Variables are instantiated on load-time. All references from [{expressions}](QS1-expressions.md) to variables will report an error, if the variable isn't instantiated.

Variables can be instantiated in two ways:

## &lt;[var](QS1-var-cmd.md)&gt;

With a &lt;[var](QS1-var-cmd.md)&gt; node at the beginning a parent-node. The &lt;[var](QS1-var-cmd.md)&gt; node's [[{expression}|QS1-Expressions]] is instantiated AND evaluated at the load-time of the script. If the &lt;[var](QS1-var-cmd.md)&gt; node is a child of a &lt;[que](QS1-que-cmd.md)&gt; node, it will be evaluated once more when the &lt;[que](QS1-que-cmd.md)&gt; starts playing and upon each subsequent loop.

The variable will be in the scope of the node it is located. It is possible to have multiple variables of the same name, but each has to be located in a different scope:

    <script>
	<var name="scriptScopeVar">99</var>
	<que name="que_1" loop="no">
	    <var name="scriptScopeVar">{scriptScopeVar / 3}</var>
            <print>scriptScopeVar is {scriptScopeVar}</print>

On loading the script, the [[{expression}|QS1-Expressions]] of the &lt;[var](QS1-var-cmd.md)&gt; node inside the &lt;[que](QS1-que-cmd.md)&gt; can access the value of the {scriptScopeVar} inside the &lt;[script](QS1-script-cmd.md)&gt; scope.
But on execution of the script, the [[{expression}|QS1-Expressions]] inside the &lt;[print](QS1-print-cmd.md)&gt; node will only be able to access the {scriptScopeVar} inside the scope of the &lt;[que](QS1-que-cmd.md)&gt;, while the {scriptScopeVar} of the &lt;[script](QS1-script-cmd.md)&gt; scope will be hidden.

## inside &lt;[{expr}](QS1-Expressions.md)&gt;

Normally an [{expr}](QS1-Expressions.md) requires a variable to be instantiated beforehand when used inside. If no variable exists, QueScript will throw an error. But it is possible to instantiate variables on the fly by using the **:** or **::** prefix to the variable name.

* '**:**' prefix instantiates the variable in the local scope if it doesn't exist in **ANY** scope yet.
* '**::**' prefix instantiates the variable in the local scope if it doesn't exist in the **local** scope yet.

In other words: '**:**' only creates a variable if doesn't exist yet, '**::**' creates one no matter.

But in difference to the &lt;[var](QS1-var-cmd.md)&gt; it will be evaluated only when the node is executed.

    <while name="Loop" init="{:var = 0}" condition="{var lt 100}" next="{var = (var + 1)}">
        <print>inside while: {var}</print>
    </while>

In case of the &lt;[while](QS1-while-cmd.md)&gt; node, the attribute 'init' is evaluated first, so the prefix needs to be set there. Once the 'init'-[[{expression}|QS1-Expressions]] is evaluated, the variable 'var' is instantiated and can be accessed by the other attributes and the child nodes.

***

An [[{expression}|QS1-Expressions]] that references an undeclared variable will throw an error:

    i.e.: Error: : Variable 'globalVar' not declared | {globalVar = 1} at line(9)

If variables of the same name exist in multiple scopes, the [{expressions}](QS1-expressions.md) will take the first one it finds with the following preference: local-scope -> ... -> que-scope -> script-scope.

The variables inside the script-scope are accessible by all [{expressions}](QS1-expressions.md) inside all ques (i.e. $HOUR, $MIN, $SEC, $MILLI).

All variables set by the user through a message-list like

    var 'name' 'value'

need to be declared with &lt;[var](QS1-var-cmd.md)&gt; node inside the &lt;[script](QS1-script-cmd.md)&gt; node, otherwise an error will be thrown.

if a message list with more than three tokens is received, like

    var 'name' 'value1' 34 8.98983

it will be turned into an [[Array|QS1-Expr-Arrays]] with 'name' as the variable-name and the subsequent list as the elements inside the array.

script-scope variables keep their values even if the script is reloaded or a new script is loaded. To clear those values you can use the message.

    reset

which also stops all running ques and reloads the same script.

All variables inside the que-scopes and sub-scopes will be lost once a new script is reloaded.

If your newly loaded script needs to access the value a script-scope variable which has been changed through user interaction via a 'var' message in a previous script, then you can initialize it at the beginning of the script the following way:

    <var name="gvar">{if(:gvar == NULL, 0, gvar)}</var>

':gvar' will cause the [{expressions}](QS1-expressions.md) to instantiate a variable if it doesn't exist. The 'if'-condition will then set gvar to 0 since the newly instatiated variable is NULL.
If the variable existed in the last script, its value will be taken to set the 'gvar' again.

A special case is the sub-node &lt;[anim](QS1-anim-cmd.md)&gt;:

Variables generated inside the sub-node &lt;[anim](QS1-anim-cmd.md)&gt; belong to either its own scope or the scope of its parent &lt;[que](QS1-que-cmd.md)&gt; node. Assuming an example like the following:

    <var name="g1.a1.t1">0</var>
    <que>
       <anim name="a1">
          <var name="g1.a1.t1">0</var>
          <track name="t1">0 1.</track>
          <track name="t2">0 1.</track>
          <send>address command {t1} {t2}</send>
          <expr>{g1.a1.t1 = t1}</expr>
       </anim>
       <while condition="true">
          <send>adress command {a1.t1} {a1.t2}</send>
          <send>adress command {g1.a1.t1}</send>
       </while>
    </que>

&lt;[track](QS1-track-cmd.md)&gt; generates for each track two variables:

- `t1` and `t2` for the sub-node &lt;[anim](QS1-anim-cmd.md)&gt; scope. They can be accessed by the &lt;[send](QS1-send-cmd.md)&gt; and &lt;[var](QS1-var-cmd.md)&gt; cmnd inside the &lt;[anim](QS1-anim-cmd.md)&gt; cmnd.
- `a1.t1` and `a1.t2` for the &lt;[que](QS1-que-cmd.md)&gt; node. They can be accessed by the &lt;[send](QS1-send-cmd.md)&gt; cmnd outside the &lt;[anim](QS1-anim-cmd.md)&gt; node

In order to make the values accessible for all the script, you can use the &lt;[var](QS1-var-cmd.md)&gt; cmnd. Please note though: if you want to make sure that all the current iterated values inside the &lt;[anim](QS1-anim-cmd.md)&gt; cmnd are passed on to a variable inside the &lt;[script](QS1-script-cmd.md)&gt;-scope, the &lt;[expr](QS1-expr-cmd.md)&gt; cmnd needs to be inside the &lt;[anim](QS1-anim-cmd.md)&gt; cmnd.

## reference an expression to a variable:

    <var name="circlePos">{-> ARRAY(COS(alpha),SIN(alpha),2)}</var>

or

    <expr>{:circlePos -> ARRAY(COS(alpha),SIN(alpha),2)}</var>

sets the reference to the [{expr}](QS1-Expressions.md) as its value.

setting a reference to a variable will execute the expression each time the variable is used further along the code and returns the result of its evaluation. In a sense it is a definition of a function call that can be referenced by the variable.

!!! info
    You can use the &lt;[debugger](QS1-debugger-cmd.md)&gt; node to see the current content of all the nodes. Important: if you place the &lt;[debugger](QS1-debugger-cmd.md)&gt; inside an animation node like &lt;[anim](QS1-anim-cmd.md)&gt; or &lt;[while](QS1-while-cmd.md)&gt; you will see different domains than if you place it outside of it.
