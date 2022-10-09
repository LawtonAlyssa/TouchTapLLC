<?php

if(isset($_POST["submit"])) {
    $orderToken = $_POST['orderToken'];
    $host="127.0.0.1";
    $port=3306;
    $socket="";
    $user="root";
    $password="1qaz1qaz!QAZ!QAZ";
    $dbname="shop";
// Attempt connection with database
    $mysqldb = new mysqli($host, $user, $password, $dbname, $port, $socket);
    $sqlOrder = "SELECT * FROM shop.order WHERE token = '$orderToken'";                  // Searching for order based on purchase token
// Execute SQL Query
    $result = mysqli_query($mysqldb, $sqlOrder, MYSQLI_USE_RESULT);
    $row = $result->fetch_row();                                                            // This is the order record from company
    $totalTaxes = $row[4];
    $totalShipping = $row[5];
    $totalCharges = $row[7];
    $services = $row[9];
    $result->close();
    print $totalCharges;
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Payment Confirmation - Touch Tap LLC</title>
    <link rel="icon" href="components/logo.png" type="image/x-icon">
    <meta charset="UTF-8">
    <!-- Global Includes -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="js/setup.js"></script>
    <!-- Page Includes -->
    <!-- Style Template -->
    <script src="https://kit.fontawesome.com/3aad77fea3.js" crossorigin="anonymous"></script>
    <!-- slider stylesheet -->
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.1.3/assets/owl.carousel.min.css" />
    <!-- style css -->
    <link rel="stylesheet" type="text/css" href="css/style.css" />
</head>
<body>
<div data-include="nav_bar"></div>
<div class="form">
    <div style = "position:relative; top:150px;">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Order Details</h5>
                <p class="card-text"><?php print "Services: ". $services?><br><?php print "Taxes: $". $totalTaxes?><br><?php print "Shipping: $". $totalShipping?><br><?php print "Total Amount Due: $". $totalCharges?></p>
                <button id="buyButton">Checkout</button>
            </div>
        </div>
    </div>

</div>

<script>
    const allowedCardNetworks = ["AMEX", "DISCOVER", "INTERAC", "JCB", "MASTERCARD", "MIR", "VISA"];
    const allowedCardAuthMethods = ["PAN_ONLY", "CRYPTOGRAM_3DS"];
    if (window.PaymentRequest) {
        const request = createPaymentRequest();

        request.canMakePayment()
            .then(function(result) {
                if (result) {
                    // Display PaymentRequest dialog on interaction with the existing checkout button
                    document.getElementById('buyButton')
                        .addEventListener('click', onBuyClicked);

                }
            })
            .catch(function(err) {
                showErrorForDebugging(
                    'canMakePayment() error! ' + err.name + ' error: ' + err.message);
            });
    } else {
        showErrorForDebugging('PaymentRequest API not available.');
    }

    /**
     * Show a PaymentRequest dialog after a user clicks the checkout button
     */
    function onBuyClicked() {
        createPaymentRequest()
            .show()
            .then(function(response) {
                // Dismiss payment dialog.
                response.complete('success');
                handlePaymentResponse(response);
            })
            .catch(function(err) {
                showErrorForDebugging(
                    'show() error! ' + err.name + ' error: ' + err.message);
            });
    }

    /**
     * Define your unique Google Pay API configuration
     *
     * @returns {object} data attribute suitable for PaymentMethodData
     */
    function getGooglePaymentsConfiguration() {
        return {
            environment: 'TEST',
            apiVersion: 2,
            apiVersionMinor: 0,
            merchantInfo: {
                // A merchant ID is available after approval by Google.
                // 'merchantId':'12345678901234567890',
                merchantName: 'Example Merchant'
            },
            allowedPaymentMethods: [{
                type: 'CARD',
                parameters: {
                    allowedAuthMethods: allowedCardAuthMethods,
                    allowedCardNetworks: allowedCardNetworks
                },
                tokenizationSpecification: {
                    type: 'PAYMENT_GATEWAY',
                    // Check with your payment gateway on the parameters to pass.
                    // @see {@link https://developers.google.com/pay/api/web/reference/request-objects#gateway}
                    parameters: {
                        'gateway': 'example',
                        'gatewayMerchantId': 'exampleGatewayMerchantId'
                    }
                }
            }]
        };
    }

    /**
     * Create a PaymentRequest
     *
     * @returns {PaymentRequest}
     */
    function createPaymentRequest() {
        // Add support for the Google Pay API.
        const methodData = [{
            supportedMethods: 'https://google.com/pay',
            data: getGooglePaymentsConfiguration()
        }];
        // Add other supported payment methods.
        methodData.push({
            supportedMethods: 'basic-card',
            data: {
                supportedNetworks:
                    Array.from(allowedCardNetworks, (network) => network.toLowerCase())
            }
        });

        const details = {
            total: {label: 'Test Purchase', amount: {currency: 'USD', value: '<?php print $totalCharges ?>'}}
        };

        const options = {
            requestPayerEmail: true,
            requestPayerName: true
        };

        return new PaymentRequest(methodData, details, options);
    }

    /**
     * Process a PaymentResponse
     *
     * @param {PaymentResponse} response returned when a user approves the payment request
     */
    function handlePaymentResponse(response) {
        const formattedResponse = document.createElement('pre');
        formattedResponse.appendChild(
            document.createTextNode(JSON.stringify(response.toJSON(), null, 2)));
        document.getElementById('checkout')
            .insertAdjacentElement('afterend', formattedResponse);
    }

    /**
     * Display an error message for debugging
     *
     * @param {string} text message to display
     */
    function showErrorForDebugging(text) {
        const errorDisplay = document.createElement('code');
        errorDisplay.style.color = 'red';
        errorDisplay.appendChild(document.createTextNode(text));
        const p = document.createElement('p');
        p.appendChild(errorDisplay);
        document.getElementById('checkout').insertAdjacentElement('afterend', p);
    }
</script>
</body>

</html>