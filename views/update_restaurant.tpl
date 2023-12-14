<!DOCTYPE html>
<html>
<head>
    <title>Update Restaurant</title>
</head>
<body>
    <h2>Update Restaurant</h2>
    <form action="/update" method="post">
        <label for="id">ID:</label>
        <input type="text" id="id" name="id" value="{{id}}" readonly><br>

        <label for="description">Description:</label>
        <textarea id="description" name="description" rows="4">{{description}}</textarea><br>

        <input type="submit" value="Update">
    </form>
    <p><a href="/list">Back to List</a></p>
</body>
</html>
