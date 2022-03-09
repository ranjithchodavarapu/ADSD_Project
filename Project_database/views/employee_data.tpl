<html>
<body>
<table>
% for item in employee_list:
  <tr>
    <td>{{item['id']}}</td><td>{{item['eid']}}</td><td>{{item['ename']}}</td><td>{{item['elocation']}}</td><td>{{item['eposition']}}</td><td>{{item['esalary']}}</td><td>{{item['experience']}}</td>
    <td><a href="/delete/{{item['id']}}">Delete</a></td>
    <td><a href="/edit/{{item['id']}}">Edit</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add">Add an item...</a>
</body>
</html>