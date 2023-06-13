<template>


    <!--<span>Este es el inicio</span>--->
    <div id="contenedor_principal_inicio">

        <div id="contenido_principal_inicio_top">


            <span>Bienvenido a nuestra Web!</span>

                
        </div>

        <div id="contenido_principal_inicio_bottom">
            <img src="@/assets/img/icons/flechita.png" alt="sobrenosotros">
        </div>


    </div>



    <div id="contenedor_secundario_inicio">


        <div id ="contenido_secundario_incio">




        </div>




    </div>




</template>





<script setup>   /* setup = Composition API */







</script>







<style scoped>   /* scoped quiere decir que mapea los estilos que le pondremos en este componente */
#contenedor_principal_inicio{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-image: url(@/assets/img/portadas/portada2.jpg);
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    position: relative;
}


#contenido_principal_inicio_top{

    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    background: rgba(0, 0, 0, 0.582);
    height: 30%;
    padding: 20px;

}



#contenedor_principal_inicio span{
    font-size: 50px;
}


#contenido_principal_inicio_bottom{
    position: absolute;
    bottom: 50px;
}

#contenido_principal_inicio_bottom img{
width: 3em;
cursor: pointer;
}
</style>