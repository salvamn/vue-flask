<template>
    <section id="contenedor_principal_inicio">

        <div id="contenido_principal_inicio_top">


            <span>Bienvenido a nuestra Web!</span>

            <!---<test style="position: absolute; bottom: 0;"/>-->

        </div>


        <div id="contenido_principal_inicio_bottom">
           <img src="@/assets/img/icons_lenguajes/mysql.png" alt="">
           <img src="@/assets/img/icons_lenguajes/js.png" alt="">
           <img id="img_flask" src="@/assets/img/icons_lenguajes/flask.png" alt="">
           <img src="@/assets/img/icons_lenguajes/vue.png" alt="">
           <img src="@/assets/img/icons_lenguajes/node.png" alt="">
           <img src="@/assets/img/icons_lenguajes/python.png" alt="">
        </div>




    </section>



    <section id="contenedor_secundario_inicio">

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

    </section>
</template>





<script>
export default {
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
       /*background: #569fd3*/
       /* margin-top: 7em; */

   }


   #contenido_principal_inicio_top {
       display: flex;
       justify-content: center;
       align-items: center;
       width: 100%;
       height: 30%;
       /*background: greenyellow;*/

   }

   #contenido_principal_inicio_bottom {
       width: 100%;
       height:20%;        
       background-color: rgba(255, 0, 0, 0);
       display: flex;
       justify-content: center;
       align-items: center;

   }


   #contenido_principal_inicio_bottom img{
        width: 15rem;
        
   }

   #contenedor_principal_inicio span {
       font-size: 50px;
       color: #569fd3;
   }



   #contenedor_secundario_inicio {
       width: 100%;
       height: 100%;
       display: flex;
       justify-content: center;
       align-items: center;
   }

   #contenedor-tarjetas-proyectos {
       width: 70%;
       height: 50%;
       display: inline-flex;
       flex-direction: row;
       justify-content: space-around;
       align-items: center;
       flex-wrap: wrap;
   }

   #contenedor-tarjetas-proyectos .tarjeta {
       width: 30%;
       height: 400px;
       background-color: #242424;
       margin-bottom: 10em;
       border: 1px solid #33333375;
       border-radius: 7px;
       box-shadow: 0px 10px 15px -3px #0000007d;
   }

   /*#img_flask{
    filter: invert(100%);
   }*/
</style>