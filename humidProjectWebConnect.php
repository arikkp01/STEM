<?php
$severname = "0.0.0.0"
$username = "humid";
$password = "password";
$dbname = "sensor";

//creating connection
$connect = mysql_connect($servername, $username, $password, $dbname);

//Check mysqli connection
if ($connect->cennect_error) {
	die("Failed Connection : " . $connect->connect_error);

$query1= mysql_sensor("SELECT * FROM weather ORDER BY id DESC LIMIT 1");
$result = $connect->query($sql);

if ($result-> num_row > 0) {
	while($row = $result->fetch_assoc()) {
		echo "Temperature: " . 
		$row["temperature"]. "°C - Humidity: " . 
		$row["humidity"]."%";
    }
} 
else {
    echo "0 results";
}
$conn->close();
?>
