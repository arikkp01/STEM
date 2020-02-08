 <?php
$servername = "localhost";
$username = "arikam20";
$password = "kamaka";
$dbname = "arikam20";  //phpmyadminusername

// Creating connection(new class/object)
//sending credentials 
//Object-similar to a class(ex: students is data structure)
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO students (name, age2, gradeLevel)
VALUES ('Joy', '18', '12')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>

# Most of my files will have a table called age2. 
# In my phpmyadmin, in my database students,
#I acidentally labelled a table age2 and never changed it
