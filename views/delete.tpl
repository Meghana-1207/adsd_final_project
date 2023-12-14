<!DOCTYPE html>
<html>
<head>
    <title>Delete Restaurant</title>
</head>
<body>
    <h2>Delete Restaurant</h2>
    
    <form action="/delete" method="post">
        <input type="hidden" name="id" value="{{id}}">
        
        <input type="Button" value="true" placeholder="Delete Restaurant">
    </form>

    <p><a href="/list">Back to List</a></p>
</body>
</html>
