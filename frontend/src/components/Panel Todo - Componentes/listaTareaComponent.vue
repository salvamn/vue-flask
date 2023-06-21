<template>

    <div v-for = "tarea in tareas" v-bind:key="tarea.id">

        {{ tarea.titulo }}
        {{ tarea.descripcion }}

    </div>


</template>








<script>


export default{

    methods:{
        tareas() {
           return this.$store.state.listarTarea;
        }
    }

}



</script>










<style scoped>

</style>