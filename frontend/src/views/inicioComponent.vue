<template>


    <!--<span>Este es el inicio</span>--->
    <div id="contenedor_principal_inicio">

        <div id="contenido_principal_inicio_top">


            <span>Bienvenido a nuestra Web!</span>

            <!---<test style="position: absolute; bottom: 0;"/>-->  
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

//import test from '@/components/testComponent.vue'





</script>







<style scoped>   /* scoped quiere decir que mapea los estilos que le pondremos en este componente */
#contenedor_principal_inicio{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    position: relative;
}


#contenido_principal_inicio_top{

    display: flex;
    justify-content: center;
    align-items: center;
    width: 60%;
    background: rgba(0, 0, 0, 0.26);
    height: 30%;
    padding: 20px;
    border-radius: 10px;

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


#contenedor_secundario_inicio{
    width: 100%;
    height: 60%;
    background-color: rgba(0, 0, 0, 0.486);
}
</style>