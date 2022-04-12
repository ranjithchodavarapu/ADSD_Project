<html>
<body>
Edit this item..
<hr/>
<form action="/edit/{{id}}" method="post">
  <p>Data Of Birth:<input name="dob" value="{{dob}}"/></p>
  <p>Location:<input name="location" value="{{location}}"/></p>
  <p>Desgination:<input name="position" value="{{position}}"/></p>
  <p>Salary:<input name="salary", value="{{salary}}"/></p>
  <p>experience:<input name="experience", value="{{experience}}"/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
<a href='/home'>Cancel</a>
</body>
</html>