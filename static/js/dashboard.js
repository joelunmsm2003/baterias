




$( ".rr" ).click(function() {
  var text = $('#inputRF').text();
  console.log(text) 
$( "#inputDirec" ).val(text);
  
});


function guardadireccion(data){


	console.log(data)

	var direccion=data

	 $( "#gridCheckdireccion" ).click(function() {


  console.log('entre putitas')


  $( "#inputDirec" ).val(direccion);


}






  function cal() {


  try {

    console.log('entre oibches.......')
  

    var a = parseInt(document.getElementById("inputPrecio").value),
        b = parseInt(document.getElementById("inputDesc").value),

        c = parseInt(document.getElementById("inputP").value);
        
    
    console.log(a,b,c)      
    document.getElementById("inputTotal").value =(a-b)*c;
  } catch (e) {
  }
}




    function traemodelos() {


      var x = document.getElementById("marca").value;
      var cliente = document.getElementById("cliente").value;
      var apellido_p = document.getElementById("apellido_p").value;
      var apellido_m = document.getElementById("apellido_m").value;
      var dni = document.getElementById("dni").value;
      var telefono_1 = document.getElementById("telefono_1").value;
      var telefono_2 = document.getElementById("telefono_2").value;
      var direccion = document.getElementById("telefono_2").value;
     

    window.location.href = "/dashboard/?marca="+x+'&cliente='+cliente+'&apellido_p='+apellido_p+'&apellido_m='+apellido_m+'&dni='+dni+'&telefono_1='+telefono_1+'&telefono_2='+telefono_2+'&direcccion='+direccion



    }




  $(document).ready(function(){
    $("#bboleta").click(function(){

      $('#ffactura1').hide()
      $('#descripcion').hide()
       $('#bboleta1').show()
       $('#descripcion').show()

    });
   


  });

  $(document).ready(function(){
    $("#ffactura").click(function(){

        $('#bboleta1').hide()
        $('#ffactura1').hide()
       $('#descripcion').show()
       $('#ffactura1').show()
       $('#descripcion').show()
    });
   


  });
