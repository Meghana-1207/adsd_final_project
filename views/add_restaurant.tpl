<!DOCTYPE html>
<html>
<head>
    <title>Add New Restaurant</title>
</head>
<body>
    <h2>Add New Restaurant</h2>
    <form action="/add" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="borough">Borough:</label>
        <input type="text" id="borough" name="borough" required><br>

        <label for="cuisine">Cuisine:</label>
        <input type="text" id="cuisine" name="cuisine" required><br>

        <label for="description">Description:</label>
        <textarea id="description" name="description" rows="4" required></textarea><br>

        <input type="submit" value="Add">
    </form>
    <p><a href="/list">Back to List</a></p>
</body>
</html>
