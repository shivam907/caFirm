<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $phone = htmlspecialchars($_POST['phone']);
    $subject = htmlspecialchars($_POST['subject']);
    $message = htmlspecialchars($_POST['message']);

    // $to = "info@example.in";
    $to = "example@gmail.com";

    $subject = "New Call Back Request: " . $subject;
    $body = "You have received a new message from the user $name.\n\n".
            "Here are the details:\n\n".
            "Name: $name\n".
            "Email: $email\n".
            "Phone: $phone\n".
            "Message:\n$message";
    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "<div class='thank-you-message'>Thank you for contacting us. We will get back to you soon!</div>";
    } else {
        echo "<div class='error-message'>There was an error sending your message. Please try again later.</div>";
    }
} else {
    echo "<div class='error-message'>Invalid request method.</div>";
}
?>
