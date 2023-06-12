<template>

    <nav id="navSito">


        <div id="contenedor_logo">

            <strike>LOGO</strike>
            
        </div>



        <div id="contenedor_rutas">

            <router-link id="rutas" to="/inicio" title="inicio">Inicio</router-link>    <!--Router link es como si fuera a href, se pone un to="/inicio" dónde lo redirije a inicio(view) logicamente-->
            <router-link id="rutas" to="/nosotros" title="nosotros">Nosotros</router-link>      <!--Router link es como si fuera a href, se pone un to="/nosotros" dónde lo redirije a nosotros(view) logicamente-->

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
    padding: 15px;
}

#navSito #contenedor_logo{
    color: white;
    font-size: 30px;
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



</style>