# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / [{expressions}](QS1-expressions.md)/Arrays

Arrays can be instantiated with the ARRAY()-function:

   ARRAY(1, 2, 'text1', 'text3', 4.652)

and can contain any number of floats and strings.

It needs to be assigned to a variable, either with a &lt;[var](QS1-var-cmd.md)&gt; node:

    <var name="arrayVar">ARRAY(1, 2, 'text1', 'text3', 4.652)</var>

or an &lt;[expr](QS1-expr-cmd.md)&gt; node:

    <expr>{:onTheFly = ARRAY(5, 'Paris', 'NY', 4.652)}</expr>

Accessing the Array is done by specifying the indices with the **[]** delimiter:

    <print>onTheFly {onTheFly[0]} {onTheFly[2]}</print>

It is also possible to use variables as indices:

    <que name="que" loop="no">
       <var name="myArray">ARRAY('Zuerich','Vienna', 'Berlin', 'London', 'Madrid', 'Casablanca')</var>
       <while name="while" init="{:index = 0}" condition="{index lt LENGTH(myArray)}" next="{index = index + 1}">
           <print>Cities to go: {myArray[index]}</print>
       </while>
       <wait anim="while"/>
    </que>


where the LENGTH()-function returns the number of elements inside an Array.

### Note
