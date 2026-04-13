<?php
$host = "aws-1-ap-southeast-1.pooler.supabase.com";
$port = "6543";
$db   = "postgres";
$user = "postgres.drtfczavpkbatbaqxdtr";
$pass = "Violla09112020!";

$dsn = "pgsql:host=$host;port=$port;dbname=$db;sslmode=require";

$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_EMULATE_PREPARES => true,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
    echo "✅ Connected via Supabase Pooler!";
} catch (PDOException $e) {
    echo "❌ Connection failed: " . $e->getMessage();
}