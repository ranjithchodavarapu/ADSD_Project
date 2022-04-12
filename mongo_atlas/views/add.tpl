<html>
<body>
Add a new item..
<hr/>
<form action="/add" method="post">
  <p>New id:<input name="eid"/></p>
  <p>Employee fristName :<input name="firstname"/></p>
  <p>Employee lastName :<input name="lastname"/></p>
  <p>Employee dob :<input name="dob"/></p>
  <p>Location:<input name="location"/></p>
  <p>Desgination:<input name="position"/></p>
  <p>experience:<input name="experience"/></p>
  <p>Salary:<input name="salary"/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
<a href='/list'>Cancel</a>
</body>
</html>