<?php
if( count($_GET) == 0 ) {
?>

<!doctype html>
<head>
 <title>jsonrpccpp </title>
   <style type="text/css">
    textarea {
      display:block; height:250px; width:500px;
      margin-botton:4px;
    }


   </style>
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
</head>

   <body>
   <center>
     <h3>A quick demo of <a href="https://github.com/cinemast/libjson-rpc-cpp">jsonrpccpp</a></h3>
   </center>

   <form id="app_form" style="margin-left:5%;">
     <div>Serving from host: <?php echo gethostname();?></div>
     <div><span>json spec file:</span><textarea name="json_spec" rows="15" columns="45" required>
        [
    {
        "name": "sayHello",
        "params": { 
            "name": "Peter"
        },
        "returns" : "Hello Peter"
    },
    {
        "name" : "notifyServer"
    }
]
     </textarea>

     <span>Click Submit to generate, and view the stubs for client, and server.</span><br>
     <div id="err_msg" style="visibility:hidden"></div>
     <input type="button" value="Submit" id="submit" style="margin-top:3%;"/>
     <script type="text/javascript">
       var path = "<?php echo $_SERVER['PHP_SELF'] . '?submit'; ?>";
       $("#submit").click(function(e) {
            var req = $.ajax({
                url: path,
                type: "POST",
                data: $("#app_form").serialize()
            });
         
            req.done(function(response, textStatus, jqxhr) {
               var res_json_obj = jQuery.parseJSON(response);

               if (res_json_obj.error) {
                  $("#err_msg").html(res_json_obj.error);
                  $("#err_msg").css("visibility", "visible");
                  $("#client_stub").html("//Client stub header");
                  $("#server_stub").html("//Server stub header");
               } else {
                  $("#err_msg").html("");
                  $("#err_msg").css("visibility", "hidden");
               }

               if (res_json_obj.client_stub) {
                  $("#client_stub").html(res_json_obj.client_stub);
               }

               if (res_json_obj.server_stub) {
                  $("#server_stub").html(res_json_obj.server_stub);
               }

               if (res_json_obj.d) {
                  $("#d").html(res_json_obj.d);
                  $("#d").css("visibility", "visible");
               }
            });
 
            e.preventDefault();
       });

     </script>
    </div>
   </form>

   <textarea id="client_stub" style="margin-left:5%;" readonly>//Client stub header</textarea>
   <textarea id="server_stub" style="margin-left:5%;" readonly>//Server stub header</textarea>
   <div id="d" style="margin-left:5%; visibility:hidden"></div>

 </body>
</html>

<?php

}

?>

<?php
 if ( isset($_GET['submit']) and isset($_POST['json_spec']) ) {

     ini_set('display_errors', 'On');
     error_reporting(E_ALL);
      
     $response_to_browser = array("error" => "",
                       "client_stub"    => "",
                       "server_stub"    => ""
                     );
    if (isset($_ENV{"APP_DEBUG"})) {
        $response_to_browser["d"] = "";
    }
    
     $json_spec_input = htmlspecialchars_decode($_POST['json_spec']);
     $json_spec_input_file = tempnam(sys_get_temp_dir(), "spec") . ".json";

     $fh = fopen($json_spec_input_file, "c+");
     if (!$fh) {
         $response_to_browser["error"] = "Internal error!";
         echo json_encode($response_to_browser);
         return;
     }

     if (!fwrite($fh, "$json_spec_input")) {
         $response_to_browser["error"] .= "Internal error!<br>";
         echo json_encode($response_to_browser);
         fclose($fh);
         unlink($json_spec_input_file);
         return;
     }

     #echo "Debug: specfile=$json_spec_input_file<br>";

     fclose($fh);

     $stub_server_header = tempnam(sys_get_temp_dir(), "Server_") . ".h"; 
     $stub_client_header = tempnam(sys_get_temp_dir(), "Client_") . ".h"; 
     
     $cmd_output = shell_exec("/usr/local/bin/jsonrpcstub $json_spec_input_file --cpp-server=AbstractStubServer  --cpp-client=StubClient --cpp-client-file=$stub_client_header --cpp-server-file=$stub_server_header 2>&1;  echo $?");

     if (preg_match('/JSON_PARSE_ERROR/', $cmd_output)) {
         $response_to_browser["error"] = "Error: $cmd_output";
         echo json_encode($response_to_browser);
         return;
     }
     #echo "Debug: cmd_output=$cmd_output<br>";

     $response_to_browser["client_stub"] = file_get_contents("$stub_client_header");
     $response_to_browser["server_stub"] = file_get_contents("$stub_server_header");
     
     echo json_encode($response_to_browser);
 }

?>
