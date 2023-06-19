<template>



<div>
    <input type="text" v-model="titulo" @keyup:enter="crearTarea" placeholder="Ingresa el titulo">
    <input type="text" v-model="descripcion" placeholder="Ingresa la descripcion">
    <input type="checkbox" v-model="prioridad">
 
    <button @click="crearTarea" >Crear Tarea</button>

</div>






</template>





<script>


export default{
    data(){
        return{
            titulo : '',
            descripcion : '',
            prioridad :'',
            nombre_usuario : 'seba',
        }
    },
    methods: {                              //crear_tarea
        async crearTarea(){
            const tarea = {
                titulo: this.titulo,
                descripcion: this.descripcion,
                prioridad: this.prioridad,
                nombre_usuario: this.nombre_usuario
            };
            try{
                const respuesta = await this.$store.dispatch('crearTarea', tarea);
                console.log(respuesta);
            } catch(error){
                console.error(error);
            }
        }
    }



}


</script>




<style>





</style>