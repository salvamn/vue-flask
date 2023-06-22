<template>



    <div id="contenedor_todo">

        <div id="contenedor_top_panel">

          <div id="contenedor_izquierdo_panel">
            <crearTarea @tarea-creada="agregarTarea"/>
          </div>
        


           <div id="contenedor_derecho_panel">
              <h1>Panel de tareas</h1>
              <!----{{ nombreUsuario }}--->
           </div>

        </div>

  
   

        <div id="contenedor_bottom_panel">
            <listarTarea :tareas="tareas" @tarea-eliminada="eliminarTarea"/>
        </div>

   


    </div>




  </template>
  





  <script>


  import crearTarea from '@/components/Peticiones HTTP/CrearTareasComponent.vue';
  import listarTarea from '@/components/Peticiones HTTP/ListarTareasComponent.vue';
  import axios from 'axios';
  //import { mapState } from 'vuex';

  export default {
    components: {
      crearTarea,
      listarTarea,
    },
    data() {
      return {
        tareas: [],
      };
    },
    mounted() {
      this.leerTareas();
    },
    methods: {

       agregarTarea(tarea) {
        this.tareas.push(tarea);
      },

       eliminarTarea(id) {
        this.tareas = this.tareas.filter((tarea) => tarea.id !== id);
      },

      async leerTareas() {
        try {
          const response = await axios.post('http://localhost:5000/leer_tareas', { nombre_usuario: 'nombre_de_usuario' });
          this.tareas = response.data;
        } catch (error) {
          console.error(error);
        }
      },

    },

    //computed:{
        //...mapState(['nombreUsuario']),
    //}



  };
  </script>

  
  

<style scoped>

#contenedor_todo {
    width: 100%;
    height: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    /*background: rgba(0, 0, 0, 0.123);*/
}

#contenedor_top_panel{
    width: 60%;
    height: 50%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-direction: row;
    /*background-color: red;*/
}

#contenedor_derecho_panel{
  width: auto;
  display: flex;
  justify-content: center;
  align-items: center;

}
#contenedor_derecho_panel h1{
  font-size: 60px;
  text-align: center;
  font-weight: bold;
}


#contenedor_izquierdo_panel{
  width: auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

#contenedor_bottom_panel{
  /*background-color: aqua;*/
    width: 100%;
    height: 30%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
}



</style>