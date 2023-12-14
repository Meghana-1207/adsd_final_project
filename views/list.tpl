<!DOCTYPE html>
<html>
<head>
    <title>Restaurant List</title>
</head>
<body>
    <h2>Restaurant List</h2>
        <form id="searchForm">
        <label for="searchInput">Search:</label>
        <input type="text" id="searchInput" name="search" placeholder="Type to search..." value="{{search}}">
        <input type="submit" value="Search">
    </form>
    <ul>
        % for item in shopping_list:
            <li>{{item.name}} ({{item.borough}}, {{item.cuisine}})</li>
        % end
    </ul>
    <p><a href="/add">Add New Restaurant</a></p>
</body>
</html>
