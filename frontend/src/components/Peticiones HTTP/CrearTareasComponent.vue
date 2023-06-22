<template>
   
        <form id="contenedor_formulario_top" @submit.prevent="crearTarea">

            <div id="contenedor_inputs">
                <h2>Ingresa una tarea</h2>
                <input id="input_crear" type="text" v-model="nuevaTarea.titulo" placeholder="Ingresa la tarea" required>
                <input id="input_crear" type="text" v-model="nuevaTarea.descripcion" placeholder="Ingresa la descripción" required>
                <input id="input_crear" type="text" v-model="nuevaTarea.nombre_usuario" placeholder="Nombre de usuario" required>
            </div>

            <div id="contenedor_combo_box">
                <select id="combobox" v-model="nuevaTarea.prioridad" required>
                    <option>Alta</option>
                    <option>Media</option>
                    <option>Baja</option>
                </select>
            </div>

            <div id="contenedor_boton">
                <button type="submit">Crear Tarea</button>
            </div>

        </form>

</template>
  
<script>
import axios from 'axios';

export default {
    data() {
        return {
            nuevaTarea: {
                titulo: '',
                descripcion: '',
                prioridad: '',
                nombre_usuario: '',
            },
        };
    },
    methods: {



        async crearTarea() {
            try {
                const response = await axios.post('http://localhost:5000/crear_tarea', this.nuevaTarea);
                this.$emit('tarea-creada', response.data.tarea);
                this.nuevaTarea = {
                    titulo: '',
                    descripcion: '',
                    prioridad: '',
                    nombre_usuario: ''
                };
            } catch (error) {
                console.error(error);
            }
        },

        
    },
};
</script>


<style scoped>

#contenedor_formulario_top {
    width: 100%;
    height: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    
}

#contenedor_inputs {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

#contenedor_combo_box {
    width: 100%;
    display: inline-flex;

    /*background: red;*/
}

#contenedor_boton {
    display: inline-flex;
    justify-items:center;
    align-items: center;

}

#contenedor_boton #boton_crear_tarea {
    padding: 11px;
    outline: 0;
    border: 0;
    color: rgb(255, 255, 255);
    background: green;
    border-radius: 10px;
    cursor: pointer;
    width: 100px;
}

#contenedor_inputs input {
    box-sizing: border-box;
    background-color: #546e7a21;
    border: 1px solid #546E7A;
    border-radius: 3px;
    font-size: 1rem;
    outline: 0;
    padding: 0.8rem;
    transition: all 600ms ease;
    color: white;
    width: 300px;
}

input::placeholder {
    color: white;
}

form input:focus,
input:active {
    background: rgba(255, 255, 255, 0.932);
    color: #ffffff;
}

#contenedor_combo_box select,
option {
    padding: 2px;
    color: rgb(0, 0, 0);
}




</style>
  