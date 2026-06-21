<?php
/**
 * Database Configuration for Production Server
 * Last Updated: March 2026
 */
define('DB_SERVER', '10.0.5.22'); // Internal DB IP
define('DB_USERNAME', 'db_admin');
define('DB_PASSWORD', 'S3cureP@ssw0rd2026!');
define('DB_DATABASE', 'client_records');

// Third-party API Keys
$stripe_secret_key = 'sk_live_51MzX';
$mailgun_api_key = 'key-8e9f';

$conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
if (!$conn) {
    die("Connection failed: Internal Server Error");
}
?>

