<h2><a href="https://leetcode.com/problems/ad-free-sessions/">1809. Ad-Free Sessions</a></h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Playback</code></p>

<pre style="position: relative;">+-------------+------+
| Column Name | Type |
+-------------+------+
| session_id  | int  |
| customer_id | int  |
| start_time  | int  |
| end_time    | int  |
+-------------+------+
session_id is the column with unique values for this table.
customer_id is the ID of the customer watching this session.
The session runs during the <strong>inclusive</strong> interval between start_time and end_time.
It is guaranteed that start_time &lt;= end_time and that two sessions for the same customer do not intersect.<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>

<p>Table: <code>Ads</code></p>

<pre style="position: relative;">+-------------+------+
| Column Name | Type |
+-------------+------+
| ad_id       | int  |
| customer_id | int  |
| timestamp   | int  |
+-------------+------+
ad_id is the column with unique values for this table.
customer_id is the ID of the customer viewing this ad.
timestamp is the moment of time at which the ad was shown.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>

<p>Write a solution to report all the sessions that did not get shown any ads.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> 
Playback table:
+------------+-------------+------------+----------+
| session_id | customer_id | start_time | end_time |
+------------+-------------+------------+----------+
| 1          | 1           | 1          | 5        |
| 2          | 1           | 15         | 23       |
| 3          | 2           | 10         | 12       |
| 4          | 2           | 17         | 28       |
| 5          | 2           | 2          | 8        |
+------------+-------------+------------+----------+
Ads table:
+-------+-------------+-----------+
| ad_id | customer_id | timestamp |
+-------+-------------+-----------+
| 1     | 1           | 5         |
| 2     | 2           | 17        |
| 3     | 2           | 20        |
+-------+-------------+-----------+
<strong>Output:</strong> 
+------------+
| session_id |
+------------+
| 2          |
| 3          |
| 5          |
+------------+
<strong>Explanation:</strong> 
The ad with ID 1 was shown to user 1 at time 5 while they were in session 1.
The ad with ID 2 was shown to user 2 at time 17 while they were in session 4.
The ad with ID 3 was shown to user 2 at time 20 while they were in session 4.
We can see that sessions 1 and 4 had at least one ad. Sessions 2, 3, and 5 did not have any ads, so we return them.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>
</div>