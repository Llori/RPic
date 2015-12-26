<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, maximun-scale=1" />
    <title>mostra dada</title>
<style type="text/css">
#dada{
        font-size: 3em;
        text-align: center;
        width: 100%;
        height: 60px;
        background-color: #A9007A;
        border-radius: 5px;
        margin-left: 10px;
        margin-bottom: 10px;
        float: left;
}
#dada2{
        font-size: 3em;
        text-align: center;
        width: 30%;
        height: 60px;
        background-color: #A9007A;
        border-radius: 5px;
        float: left;
        margin-left: 10px;
        margin-bottom: 10px;
}

#unit{
        font-size: 0.5em;
        color: black;
}
#comment{
        font-size: 3em;
        text-align: center;
        width: 14em;
        height: 60px;
        background-color: #A9007A;
        border-radius: 5px;
        float: left;
        overflow: hidden;
        margin-left: 10px;
        margin-bottom: 10px;
}


</style>
</head>
<body>
<p>
<div id="dada">
<?php
        $file    = file('textmcp.txt');
        echo $file[count($file) - 5]."<span id='unit'></span>";
?>
</div>
<div id="dada">
<?php
        $file    = file('textmcp.txt');
        echo $file[count($file) - 3]."<span id='unit'></span>";
?>
</div>


<div id="comment">
<?php
        $file    = file('textmcp.txt');
        if ($file[count($file) - 2] > 50)
        echo "Clar";
        else
        echo "Fosc";
?>
</div>
<div id="comment">
<?php
        $file    = file('textmcp.txt');
        if ($file[count($file) - 1] > 50)
        echo "Alta potència";
        else
        echo "Baixa potència";
?>
</div>



</body>
</html>
