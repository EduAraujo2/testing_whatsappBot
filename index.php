<?php

$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'bot';
$conn = mysqli_connect($servidor,$usuario,$senha,$banco);

if (!$conn){
    //echo "deu ruim";
}else{
   ///echo "deu tudo certo";
} ///

?>

<?php
$msg = $_GET['msg'];
$telefone_cliente = $_GET['telefone'];

    $sql = "SELECT * FROM usuario WHERE telefone = '$telefone_cliente'";
        $query = mysqli_query($conn, $sql);
        $total = mysql_num_rows($query);

    if ($total > 0){
        echo "numero encontrado";
    }else {
        $sql = "INSERT INTO usuario (telefone, status) VALUES ('$telefone_cliente', '1')";
        $query = mysqli_query($conn,$sql);
    }




?>



