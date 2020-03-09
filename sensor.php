<?php
$data =
    header('Content-Type: application/json');

// User credentials
$servername = "192.168.0.205";
$username = "humid";
$password = "password";
$dbname = "sensor";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connectionmysqli
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Select the most recent time, temperature, and humidity
$sql = "SELECT * FROM weather ORDER BY time DESC LIMIT 1";
//execute
$result = $conn->query($sql);


if ($result->num_rows > 0) {
    // Output data of each row
    while($row = $result->fetch_assoc()) {
        // Echo most recent temperature and humidity, and the datetime stamp
        echo "Temperature: " . $row["temperature"]. "°C - Humidity: " . $row["humidity"]."%" . " - Last updated: " . $row["time"];
        
        // Compare current time to the datetime stamp of most recent data point
        $lastPt = new DateTime($row['time']);
        $currentTime = new DateTime();
        $interval = $currentTime->diff($format);
        
        // If the difference between the current time and time of lastpoint 
        // is greater than 5 minutes, output a warning in red.
        if (($currentTime->getTimestamp() - $lastPt->getTimestamp()) > 60*5){
            echo nl2br("\n <p> <font color=red> NO DATA FOR 5 MIN </font></p>");
        }
    }   
} 
else {
    echo "0 results";
}

//if ($result2->num_rows > 0) {
    // Output highest temperature recorded and its date in human readable format
    //while($row = $result2->fetch_assoc()) {
        //echo nl2br("\n Highest temperature recorded: " . $row["temperature"]. "°C on ". date('F jS, Y h:i', strtotime($row["time"])));
    }
}

//if ($result3->num_rows > 0) {
    // Output lowest temperature recorded and its date in human readable format
    //while($row = $result3->fetch_assoc()) {
        //echo nl2br("\n Lowest temperature recorded: " . $row["temperature"]. "°C on ". date('F jS, Y h:i', strtotime($row["time"])));
    }
}

//if ($result4->num_rows > 0) {
    // Output highest humidity recorded and its date in human readable format
    //while($row = $result4->fetch_assoc()) {
        //echo nl2br("\n Highest humidity recorded: " . $row["humidity"]. "% on ". date('F jS, Y h:i', strtotime($row["time"])));
    }
}

//if ($result5->num_rows > 0) {
    // Output lowest humidity recorded and its date in human readable format
    //while($row = $result5->fetch_assoc()) {
        //echo nl2br("\n Lowest humidity recorded: " . $row["humidity"]. "% on ". date('F jS, Y h:i', strtotime($row["time"])));
    }
}

// Close database connection
$conn->close();

print json_encode($data)


?>
