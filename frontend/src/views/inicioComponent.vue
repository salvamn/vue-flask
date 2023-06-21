<template>




    <div id="contenedor_principal_inicio">

        <div id="contenido_principal_inicio_top">


            <span>Bienvenido a nuestra Web!</span>

            <!---<test style="position: absolute; bottom: 0;"/>-->


        </div>

        <div id="contenedor-tarjetas-proyectos">


            <div class="tarjeta"></div>
            <div class="tarjeta"></div>
            <div class="tarjeta"></div>
            <div class="tarjeta"></div>
            <div class="tarjeta"></div>
            <div class="tarjeta"></div>
            <div class="tarjeta"></div>
            <div class="tarjeta"></div>
            <div class="tarjeta"></div>


        </div>


    </div>


</template>





<script>  
export default{
    components: {
      
    }
}


</script>







<style scoped>   /* scoped quiere decir que mapea los estilos que le pondremos en este componente */
   #contenedor_principal_inicio {
       width: 100%;
       height: 100%;
       display: flex;
       justify-content: center;
       align-items: center;
       flex-direction: column;
       background-color: #1A1A1A;
       /* margin-top: 7em; */
       margin-bottom: 7em;
   }


   #contenido_principal_inicio_top {

       display: flex;
       justify-content: center;
       align-items: center;
       width: 100%;
       height: 100vh;
       padding: 20px;
       border-radius: 10px;
       /*background: greenyellow;*/
       margin-bottom: 7em;

   }



   #contenedor_principal_inicio span {
       font-size: 50px;
       color: #569fd3;
   }


   #contenido_principal_inicio_bottom {
       height: 20%;
       width: 100%;
       display: flex;
       justify-content: center;
       align-items: center;
       background: rgba(0, 0, 0, 0);
   }

   #contenido_principal_inicio_bottom img {
       width: 3em;
       cursor: pointer;
   }


   #contenedor-tarjetas-proyectos{
    width: 70%;
    height: auto;
    display: inline-flex;
    flex-direction: row;
    justify-content: space-around;
    flex-wrap: wrap;
   }

   #contenedor-tarjetas-proyectos .tarjeta{
    width: 45%;
    height: 400px;
    background-color: #242424;
    margin-bottom: 10em;
    border: 1px solid #33333375;
    border-radius: 7px;
    box-shadow: 0px 10px 15px -3px #0000007d;
   }

</style>