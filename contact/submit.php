<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];

    // Here, you can handle the form data as needed.
    // For simplicity, we'll just simulate a successful form submission.
    
    // If you want to send an email, save to a database, etc., add that logic here.
    
    echo "success";
} else {
    echo "error";
}
?>
