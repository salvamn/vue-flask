<template>

    <nav id="navSito">


        <div id="contenedor_logo">

            <img src="@/assets/img/icons/codigo.png" alt="">
            
        </div>



        <div id="contenedor_rutas">

            <router-link id="rutas" to="/inicio" title="inicio"><img src="@/assets/img/icons/inicio.png" alt=""></router-link>    <!--Router link es como si fuera a href, se pone un to="/inicio" dónde lo redirije a inicio(view) logicamente-->
            <router-link id="rutas" to="/nosotros" title="nosotros"><img src="@/assets/img/icons/nosotros.png" alt=""></router-link>      <!--Router link es como si fuera a href, se pone un to="/nosotros" dónde lo redirije a nosotros(view) logicamente-->
            <router-link id="rutas" to="/tareas" title="tareas"><img src="@/assets/img/icons/tareas.png" alt=""></router-link>

        </div>

    </nav>



</template>





<script setup>





</script>







<style scoped>   /* scoped quiere decir que mapea los estilos que le pondremos en este componente */
#navSito{
    width: 100%;
    background-color: rgb(5, 5, 5);
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 5px;
    position: fixed;
    top: 0;
    z-index: 99999;
}

#navSito #contenedor_logo{
    color: white;
    font-size: 30px;
}

#navSito #contenedor_logo img{
    width: 1.5em;
    filter: invert(100%);
}

#navSito #contenedor_rutas {
    display: flex;
    gap: 40px;
    
}

#contenedor_rutas #rutas{
    text-decoration: none;
    color: white;
    font-size: 20px;
}

#rutas img{
    width: 2em;
}


</style>