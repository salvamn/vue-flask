<template>


<section class="contenedor_general">

<div class="contenedor_izquierdo">

    <form @submit.prevent="agregarPublicacion">  <!--Fijate que "agregarPublicación esta en la mutations de STORE.JS"-->


    <textarea class="inputclass" type="text" v-model="nuevaPublicacion" placeholder="pone una publicacion"  cols="30" rows="10"> </textarea>
    <button type="submit">crea una publicacion</button>

    </form>   


</div>



<div class="contenedor_derecho">

    <!---Referencia acá donde sale el modal-->

    <resultados  v-if="publicaciones.length > 0"/>
</div>


</section>

</template>



<script>
import resultados from './ResultadosComponent.vue';
import { useStore } from 'vuex';

export default{

    components:{
        resultados,
    },





    data(){
        return{
            nuevaPublicacion: '',
        }
    },





    methods:{
        agregarPublicacion(){
            const nuevaPublicacion = {
                id: Date.now(),
                texto: this.nuevaPublicacion,
            };
            this.$store.commit('agregarPublicacion', nuevaPublicacion);  // Acá emite digamos el COMMIT al store y lo pone como nuevapublicaión
            this.nuevaPublicacion = '';
        }
    },



    setup(){
        const store = useStore();
        const publicaciones = store.state.publicaciones;


        return {
            publicaciones,
        }
    }


    


}


</script>



<style>
.contenedor_general{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.contenedor_izquierdo{
    width: 20%;
    background-color: red;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

form{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    flex-direction: column;
}

form button{
    background: aquamarine;
    color: rgb(7, 7, 7);
    outline: 0;
    border: 0;
    padding: 10px;
    border-radius: 10px;
    cursor: pointer;
}
.contenedor_derecho{
    width: 50%;
    height: 100%;
    background-color: green;
}
.inputclass::placeholder{
    color: black;
}
.inputclass{
    color: black;
}
</style>