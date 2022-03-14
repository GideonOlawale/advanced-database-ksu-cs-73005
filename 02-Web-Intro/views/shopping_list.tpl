<html>
<head>
</head>
<body>
<table>
% for row in shopping_list:
<tr><td>{{row['id']}}</td><td>{{row['desc']}}</td><td><a href='/delete/{{row['id']}}'>Delete</a></td><td><a href='/edit/{{row['id']}}'>Edit</a></td></tr>
%end
</table>
<p><a href='/add'>Add an item...</a></p>
</body>
</html>