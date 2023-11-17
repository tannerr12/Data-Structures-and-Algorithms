<h2><a href="https://leetcode.com/problems/form-a-chemical-bond/">2480. Form a Chemical Bond</a></h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Elements</code></p>

<pre style="position: relative;">+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| symbol      | varchar |
| type        | enum    |
| electrons   | int     |
+-------------+---------+
symbol is the primary key (column with unique values) for this table.
Each row of this table contains information of one element.
type is an ENUM (category) of type ('Metal', 'Nonmetal', 'Noble')
 - If type is Noble, electrons is 0.
 - If type is Metal, electrons is the number of electrons that one atom of this element can give.
 - If type is Nonmetal, electrons is the number of electrons that one atom of this element needs.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>

<p>Two elements can form a bond if one of them is <code>'Metal'</code> and the other is <code>'Nonmetal'</code>.</p>

<p>Write a solution to find all the pairs of elements that can form a bond.</p>

<p>Return the result table <strong>in any order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> 
Elements table:
+--------+----------+-----------+
| symbol | type     | electrons |
+--------+----------+-----------+
| He     | Noble    | 0         |
| Na     | Metal    | 1         |
| Ca     | Metal    | 2         |
| La     | Metal    | 3         |
| Cl     | Nonmetal | 1         |
| O      | Nonmetal | 2         |
| N      | Nonmetal | 3         |
+--------+----------+-----------+
<strong>Output:</strong> 
+-------+----------+
| metal | nonmetal |
+-------+----------+
| La    | Cl       |
| Ca    | Cl       |
| Na    | Cl       |
| La    | O        |
| Ca    | O        |
| Na    | O        |
| La    | N        |
| Ca    | N        |
| Na    | N        |
+-------+----------+
<strong>Explanation:</strong> 
Metal elements are La, Ca, and Na.
Nonmeal elements are Cl, O, and N.
Each Metal element pairs with a Nonmetal element in the output table.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>
</div>