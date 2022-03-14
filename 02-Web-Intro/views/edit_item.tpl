<html>
<head>
</head>
<body>
<h1>Edit this item</h1>
<p>New Item:</p>
<form action = "/edit/{{id}}" method='post'>
<input value={{item}} name='item'/>
<button type='submit'>Submit</button>
</form>
<p><a href='/'>Cancel</a></p>
</body>
</html>