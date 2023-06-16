<template>

    <nav id="navSito">


        <div id="contenedor_logo">

            <img src="@/assets/img/icons/codigo.png" alt="">
            
        </div>



        <div id="contenedor_rutas">

            <router-link id="rutas" to="/Inicio" title="inicio"><img src="@/assets/img/icons/inicio.png" alt=""></router-link>  
            <router-link id="rutas" to="/login" title="inicio">Iniciar Sesion</router-link>  
            <router-link id="rutas" to="/registrar" title="registrate">Registrate</router-link>


        </div>

    </nav>



</template>





<script>




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
    font-size: 17px;
    display: flex;
    justify-content: center;
    align-items: center;
}

#rutas img{
    width: 2em;
}


</style>