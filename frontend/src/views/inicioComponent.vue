<template>




    <div id="contenedor_principal_inicio">

        <div id="contenido_principal_inicio_top">


            <span>Bienvenido a nuestra Web!</span>

            <!---<test style="position: absolute; bottom: 0;"/>-->


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
       background: rgba(0, 0, 0, 0.199);

   }


   #contenido_principal_inicio_top {

       display: flex;
       justify-content: center;
       align-items: center;
       width: 100%;
       height: 20%;
       padding: 20px;
       border-radius: 10px;
       /*background: greenyellow;*/

   }



   #contenedor_principal_inicio span {
       font-size: 50px;
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

</style>