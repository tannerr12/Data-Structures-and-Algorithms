<h2><a href="https://leetcode.com/problems/shortest-distance-in-a-line/">613. Shortest Distance in a Line</a></h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Point</code></p>

<pre style="position: relative;">+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
+-------------+------+
In SQL, x is the primary key column for this table.
Each row of this table indicates the position of a point on the X-axis.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>

<p>Find the shortest distance between any two points from the <code>Point</code> table.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> 
Point table:
+----+
| x  |
+----+
| -1 |
| 0  |
| 2  |
+----+
<strong>Output:</strong> 
+----------+
| shortest |
+----------+
| 1        |
+----------+
<strong>Explanation:</strong> The shortest distance is between points -1 and 0 which is |(-1) - 0| = 1.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> How could you optimize your solution if the <code>Point</code> table is ordered <strong>in ascending order</strong>?</p>
</div>