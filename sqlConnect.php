<?php
$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "classroom";

//creating connection
$conn = new mysqli($servername, $username, $password, $dbname);

//Checking connection
if ($conn->connect_error) {
  die("Failed to Connect: " .$conn->connect_error);
}

//creating query
$sql = "SELECT name, age2, gradeLevel FROM students';
$result = $conn->query($sql);

//outing putting data for each row
if ($result-> num_rows > 0) {
  while ($row = $result->fetch_assoc()) {
    echo "Name: ".$row["name"]. " -Age: ". $row["age2"]. " - Grade Level ". $row["gradeLevel"]."\n".\n";
    }
}
else {
  echo "0 results";
}
//closeing connection
$conn->close();

 ?>
    
