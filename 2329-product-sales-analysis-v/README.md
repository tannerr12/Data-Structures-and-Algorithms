<h2><a href="https://leetcode.com/problems/product-sales-analysis-v/">2329. Product Sales Analysis V</a></h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Sales</code></p>

<pre style="position: relative;">+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| user_id     | int   |
| quantity    | int   |
+-------------+-------+
sale_id contains unique values.
product_id is a foreign key (column with unique values) to <code>Product</code> table.
Each row of this table shows the ID of the product and the quantity purchased by a user.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>

<p>Table: <code>Product</code></p>

<pre style="position: relative;">+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| price       | int  |
+-------------+------+
product_id contains unique values.
Each row of this table indicates the price of each product.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>

<p>Write a solution to report&nbsp;the spending of each user.</p>

<p>Return the resulting table ordered by <code>spending</code> in <strong>descending order</strong>. In case of a tie, order them by <code>user_id</code> in ascending order.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> 
Sales table:
+---------+------------+---------+----------+
| sale_id | product_id | user_id | quantity |
+---------+------------+---------+----------+
| 1       | 1          | 101     | 10       |
| 2       | 2          | 101     | 1        |
| 3       | 3          | 102     | 3        |
| 4       | 3          | 102     | 2        |
| 5       | 2          | 103     | 3        |
+---------+------------+---------+----------+
Product table:
+------------+-------+
| product_id | price |
+------------+-------+
| 1          | 10    |
| 2          | 25    |
| 3          | 15    |
+------------+-------+
<strong>Output:</strong> 
+---------+----------+
| user_id | spending |
+---------+----------+
| 101     | 125      |
| 102     | 75       |
| 103     | 75       |
+---------+----------+
<strong>Explanation:</strong> 
User 101 spent 10 * 10 + 1 * 25 = 125.
User 102 spent 3 * 15 + 2 * 15 = 75.
User 103 spent 3 * 25 = 75.
Users 102 and 103 spent the same amount and we break the tie by their ID while user 101 is on the top.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>
</div>