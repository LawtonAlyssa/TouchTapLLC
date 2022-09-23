<?php
/***********************************************************************************************************************
Author: Brandon Romero
Assignment: Software Engineering Project (PHP-HTML-MYSQL-New Customer)
Last Edited: 9/2022
Program Description: Provides method to send customer provided information from a html webpage into MySQL database
 ************************************************************************************************************************
'user' Table Properties
Columns: 'id', 'firstName', 'middleName', 'lastName', 'mobile', 'email', 'passwordHash', 'admin', 'registeredAt',
'lastLogin'
 ***********************************************************************************************************************/

if(isset($_POST['submit'])) {
    //Setting variables to those of the html 'webpage'
    $regDate = date("Y-m-d");
    $regTime = date("H:i:s");
    $dateTime = $regDate . ' ' . $regTime;

    $id = '0';
    $fname = $_POST['firstname'];
    $mname = $_POST['middlename'];
    $lname = $_POST['lastname'];
    $phone = $_POST['phonenum'];
    $email = $_POST['email'];
    $passwordHash1 = $_POST['password'];
    $passwordHash2 = $_POST['repassword'];
    $admin = '0';
    $registeredAt = $dateTime;
    $lastLogin = $dateTime;                   // Need to find out how to get this

    if ($passwordHash1 == $passwordHash2) {
        $passwordHash = $passwordHash1;
    } else  {
        $passwordHash = 'apples';             // Need to change this to reject user input
    }
    // Database connection set-up
    $host="127.0.0.1";
    $port=3306;
    $socket="";
    $user="root";
    $password="1qaz1qaz!QAZ!QAZ";
    $dbname="shop";

// Attempt connection with database
    try {
        $mysqldb = new mysqli($host, $user, $password, $dbname, $port, $socket);
    } catch (mysqli_sql_exception $e) {
        echo 'Connection failed: ' . $e->getMessage();
    }
    if ($mysqldb) {
        echo "Connection successful!";
    } else {
        echo "Error, no connection! Something's Wrong.";
    }
// SQL Statement to execute
    $sqlstmt = "INSERT INTO shop.user (id, firstName, middleName, lastName, mobile, email, passwordHash, admin, registeredAt, lastLogin) VALUES ('$id', '$fname', '$mname', '$lname', '$phone', '$email', '$passwordHash', '$admin', '$registeredAt', '$lastLogin')";

// Execute SQL command
    $rs = mysqli_query($mysqldb, $sqlstmt);
    if ($rs) {
        echo "Upload successful!";
    } else {
        echo "Error, information not saved didn't send.";
    }
// Close connection with database
    mysqli_close($mysqldb);
}
