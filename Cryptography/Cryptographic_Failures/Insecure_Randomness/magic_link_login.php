<?php
if (isset($_GET['email']) && isset($_GET['constant']) && is_numeric($_GET['constant'])) {
    $email = $_GET['email'];
    $constant = (int)$_GET['constant']; 

    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $seed = crc32($email) + $constant;
        mt_srand($seed);

        echo "<h3>Predicted Magic Link Tokens for $email</h3>";
        for ($i = 0; $i < 10; $i++) {
            $random_number = mt_rand();
          
            $token = base64_encode($random_number);
            echo "Predicted magic link token " . ($i + 1) . ": " . $token . "<br>";
        }
    } else {
      
        echo "<div style='color:red;'>Invalid email format. Please provide a valid email.</div>";
    }
} else {
    echo "<div style='color:red;'>Please provide valid GET parameters: 'email' (valid email address) and 'constant' (numeric value).</div>";
}
?>
